# Mod: Marriage (work in progress)

## Data source: princesses / queens per civilization

The marriage workflow picks bride names from a versioned data file maintained
in [kingdoms-services](https://github.com/merlin-pinpin-org/kingdoms-services):

```
kingdoms-services/config/data/marriage/princesses.yaml
```

### Schema

- `version` — integer, bumped on any breaking change to the structure.
- `civilizations.<slug>` — one entry per AoE2 civilization (French display
  names); slug is a simple lowercase slug. The removed `Indiens` civilization
  is excluded (replaced by `hindoustanis`).
- `civilizations.<slug>.display_name` — French display name.
- `civilizations.<slug>.princesses[]` — list of princess/queen entries with:
  - `name` — full name (given name + historical name).
  - `title` — historical title (queen consort, impératrice régnante, etc.).
  - `source_status` — one of:
    - `documented` — historically attested woman (written sources,
      inscriptions, chronicles).
    - `tradition` — strong oral or literary tradition, semi-legendary.
    - `legendary` — mythological or literary creation, kept for gameplay
      breadth but flagged as non-historical.

### Sourcing rules

- Every entry is a real woman from (or closely tied to) the civilization's
  historical context; fictional placeholder names are forbidden.
- Civilizations with scarce written sources (Celtes, Tupi, Maliens,
  Mapuche, Bengalis, Malais) carry fewer than 5 entries and/or rely on
  `tradition` / `legendary` entries; the `source_status` flag lets the
  marriage workflow filter or weight names by reliability if desired.
- Minimum guarantee per civilization: 3 entries.

### Consumption

Mods and services load the file read-only at startup or on demand; any
change to the schema must bump `version` and be reflected on this page.
