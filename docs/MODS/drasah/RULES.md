# Drasah mod — Rules

## Rule 1 — Greeting

`/drasah` always answers with exactly one greeting message, mentioning
the invoking player. The greeting is chosen from the mod's greeting
catalog for the player's locale (fallback: English). The mod declares
no permission: anyone in a guild where the bot is present may use it.

Edge cases:

- Unknown locale → English greeting
- Locale variants (e.g. `fr-CA`) → treated as `fr`
