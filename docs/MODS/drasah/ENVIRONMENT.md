# Drasah mod — Environment

## Configuration

The mod is declared in `kingdoms-services/config/mods/drasah.yaml`:

| Key | Type | Description |
| --- | ---- | ----------- |
| `id` | slug | `drasah` |
| `enabled` | bool | Whether the mod (and its command) is loaded |
| `commands` | list | `drasah` |

## Channels and roles

None: the mod is stateless and needs no channels or roles.

## Localization

Command name/description: `commands.drasah_name` /
`commands.drasah_description` in `config/locales/<locale>.yaml`.
Greeting texts live in the mod module (`kingdoms/discord/drasah.py`).
