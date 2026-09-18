# Testing strategy

This page defines how Kingdoms is tested: the `MockDiscord` in-memory
platform, the test pyramid, and the rules that keep tests fast and
hermetic. `MockDiscord` is tracked by kingdoms-services#2; this page is the
strategy its implementation and all later test work must follow. It will be
enriched with concrete examples as the code lands in `kingdoms-services`.

## 1. Principle: no test touches the real Discord API

Discord is an external, rate-limited, hard-to-reproduce dependency. Every
test runs against in-process fakes:

- **`MockDiscord`** — a full in-memory `IPlatform` implementation: channels,
  roles, DMs, and message history in plain Python structures
- **In-memory MongoDB substitute** — same interface as the persistence
  layer, no server needed
- **In-memory Redis substitute** — same interface as `StateService`, TTLs
  simulated with a controllable clock

Real-API verification (token present, intents correct) is a one-off smoke
check run manually against a throwaway guild, never part of CI.

## 2. Test pyramid

| Level | Scope | Runs on | Tools |
| ----- | ----- | ------- | ----- |
| Unit | Core services, models, pure functions (`ChannelService` resolution, workflow transitions) | Every push/PR | pytest |
| Integration | Multi-component flows: `WorkflowEngine` + `ChannelService` + `StateService` + stores | Every push/PR | pytest + `MockDiscord` |
| Workflow E2E | Complete user journeys (register a player, report a match) driven only through `MockDiscord` interactions | Every push/PR | pytest |
| Manual smoke | Real Discord connection, slash command registration | Before release, by hand | — |

## 3. MockDiscord

`MockDiscord` implements `IPlatform` in memory and additionally exposes the
**observer side** tests need: a way to drive interactions and inspect what
the bot did.

### Capabilities (contract for kingdoms-services#2)

- Channel creation/lookup by category, mirroring guild structure
- Role assignment and membership tracking
- DM and message capture (content, embeds, components) in inspectable
  history
- Interaction simulation: button click, select choice, modal submission,
  slash-command invocation — each producing the same core events as the
  real adapter
- A controllable clock for TTL and workflow-timeout tests

### Test-driving pattern

```text
mock = MockDiscord(clock=FakeClock())
bot = build_bot(platform=mock, stores=in_memory_stores())
bot.start()

# drive a full user journey through interactions only
session = mock.user("player1").slash_command("register")
session.answer_modal({"pseudo": "Player1"})
session.click_button("confirm")

# assert on observable outcomes, not internals
assert mock.guild.role("Player").has_member("player1")
assert mock.dms_to("player1").last_content_contains("registration confirmed")
```

### What MockDiscord must NOT do

- Reimplement game logic or workflow semantics — it is a platform, not an
  oracle
- Share state between tests — each test builds a fresh instance
- Paper over adapter bugs: the Discord adapter and `MockDiscord` implement
  the same `IPlatform` interface; divergences found in production are
  reproduced as tests at the `IPlatform` level first

## 4. What each layer tests

- **Core services** — state transitions, persistence round-trips,
  channel-resolution order, lock behavior, restart recovery
- **Mods/workflows** — journey outcomes: final state in MongoDB, roles
  assigned, messages sent, i18n of every user-facing string (English
  default, French available —
  [ADR-0008](../DECISIONS/008-i18n-system.md))
- **Adapters** — conversions between platform objects and core models
  (`IMessage`, `IChannel`, `IUser`)
- **Config** — every YAML file parses and validates against its schema

## 5. Rules

1. Tests never sleep on wall-clock time; timeouts are tested with the
   controllable clock
2. One assertion focus per test; journeys are split into ordered test
   cases that rebuild state explicitly rather than depending on execution
   order
3. User-facing strings are asserted through locale keys or localized
   content, never raw hardcoded text
4. CI (lint, test) runs on every PR in `kingdoms-services` and
   `kingdoms-infra`; docs validation runs on every PR in this repo
   (`.github/workflows/check-docs.yml`)

## See also

- [core.md](core.md) — core services design
- [mods.md](mods.md) — mod system design
- [discord.md](discord.md) — Discord platform guide
- [ADR-0001](../DECISIONS/001-multi-platform-architecture.md) —
  `IPlatform` abstraction, the seam that makes this strategy possible
