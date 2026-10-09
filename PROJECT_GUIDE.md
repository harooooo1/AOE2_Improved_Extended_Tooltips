# AOE2 Improved Extended Tooltips - Project Guide

## Project Overview

This is a tooltip modification for **Age of Empires 2: Definitive Edition** that enhances in-game tooltips with additional information, clarifications, and extended descriptions. The mod supports multiple languages with a hierarchical translation system.

**Project Maintainer:** harooooo (Discord/in-game nickname)  
**Spanish Collaborator:** hebygamer

For questions or additional information about the project, contact harooooo on Discord or in-game.

## ⚠️ Golden Rules (read first)

In October 2026 an audit found dozens of stats that had been updated in EN but never in DE/ES/IT (e.g. Cataphract +13 vs Infantry in EN but still +9 in IT, Guard Tower +7 vs Ships in EN but +6 in DE). Translated files had also drifted out of EN's entry order. These rules exist so that never happens again:

1. **EN is the source of truth.** Every change made to an EN entry must be made to the same entry in DE, ES and IT **in the same commit**. Never commit an EN-only change.
2. **Every number counts.** When a stat changes (attack, bonus, HP, LoS, time, %, cost…), search the *whole* EN file for the old value in that context. The same stat often appears in several entries (unit + upgrade tech + civ description), and each of those must be updated in all 4 languages.
3. **Translate from the current EN text**, not from the official game descriptions and not from an older translation. The mod's EN text is more detailed and more up to date than the official strings.
4. **Keep the same structure as EN:** same entry order, same blank lines, same tags, same line breaks (`\n`), same number of bullet lines.
5. **Run `python tools/validate.py` before every commit. It must pass**, apart from differences that are listed in `tools/number_exceptions.txt`. Do not add an exception to make an error go away unless the difference is only wording (e.g. "30k" vs "30.000", "2x" written as a word).

## File Structure

```
AOE2_Improved_Extended_Tooltips/
├── info.json                                    # Mod metadata
├── README.md                                    # User-facing documentation
├── PROJECT_GUIDE.md                             # This file - AI/developer guide
├── .gitignore                                   # Excludes the two dont-commit-* folders
├── dont-commit-original-game-files/             # (gitignored, maintainer's PC only) official game strings
├── dont-commit-techtree-data/                   # (gitignored) aoe2techtree data.json for stat checks
├── dont-commit-name-review/                    # (gitignored) name review lists sent to translators
├── dont-commit-changelogs/                     # (gitignored) changelog drafts for releases
├── tools/
│   ├── validate.py                              # Consistency checker - run before every commit
│   └── number_exceptions.txt                    # Known wording-only number differences
├── modes/
│   └── Pompeii/                                 # Special game mode variant
│       └── resources/en/strings/key-value/
│           └── key-value-modded-strings-utf8.txt
└── resources/
    ├── en/strings/key-value/                    # English (base/reference)
    ├── de/strings/key-value/                    # German (AI-translated)
    ├── es/strings/key-value/                    # Spanish (AI + 2 collaborators)
    ├── it/strings/key-value/                    # Italian (AI-translated)
    ├── mx/strings/key-value/                    # Mexican Spanish (copy of ES)
    ├── br/strings/key-value/                    # Brazilian Portuguese (copy of EN)
    ├── fr/strings/key-value/                    # French (copy of EN)
    ├── hi/strings/key-value/                    # Hindi (copy of EN)
    ├── jp/strings/key-value/                    # Japanese (copy of EN)
    ├── ko/strings/key-value/                    # Korean (copy of EN)
    ├── ms/strings/key-value/                    # Malay (copy of EN)
    ├── pl/strings/key-value/                    # Polish (copy of EN)
    ├── ru/strings/key-value/                    # Russian (copy of EN)
    ├── tr/strings/key-value/                    # Turkish (copy of EN)
    ├── tw/strings/key-value/                    # Traditional Chinese (copy of EN)
    ├── vi/strings/key-value/                    # Vietnamese (copy of EN)
    └── zh/strings/key-value/                    # Simplified Chinese (copy of EN)
```

## Language Hierarchy

### Primary Languages (4 languages with unique translations)

1. **English (EN)** - Base reference language
   - Location: `resources/en/strings/key-value/key-value-modded-strings-utf8.txt`
   - Origin: Homebrewed by project maintainer (harooooo)
   - Role: Source of truth for all updates

2. **German (DE)** - Fully AI-translated from English
   - Location: `resources/de/strings/key-value/key-value-modded-strings-utf8.txt`
   - Origin: AI-generated translations

3. **Spanish (ES)** - AI-translated with human collaborator input
   - Location: `resources/es/strings/key-value/key-value-modded-strings-utf8.txt`
   - Origin: Mix of AI translations + human collaborator **hebygamer** (note: Viking Sagas DLC and some other content was AI-translated)
   - Special: Copied to MX folder

4. **Italian (IT)** - Fully AI-translated from English
   - Location: `resources/it/strings/key-value/key-value-modded-strings-utf8.txt`
   - Origin: AI-generated translations

### Secondary Languages (12 languages - English copies)

These folders contain exact copies of the English (EN) file:
- BR (Brazilian Portuguese)
- FR (French)
- HI (Hindi)
- JP (Japanese)
- KO (Korean)
- MS (Malay)
- PL (Polish)
- RU (Russian)
- TR (Turkish)
- TW (Traditional Chinese)
- VI (Vietnamese)
- ZH (Simplified Chinese)

### Mexican Spanish (MX)

- Exact copy of Spanish (ES) file
- Updated whenever ES is updated

## File Format

Each language file is UTF-8 **with BOM** and uses **CRLF** line endings. Every entry is one line:

```
ID "Tooltip text with formatting"
```

Lines starting with `//` are comments. A comment may also follow an entry on the same line (e.g. `... //britons`). Blank lines are only for readability and must match EN.

### Example Entry

```
26106 "Build <b>Longship<b> (<cost>, Time: 25s)\nFast and powerful warship, strong in masses. Fires a volley of 4 arrows, each dealing full attack damage. Weak vs Caravels. <GREY><DEFAULT>Attack Delay: 0, Accuracy: 100%, LoS: 8\nArmor Class: Ship, Long-range Warship\nAttack Bonus: +1 vs Long-range Warships, 2 vs Rams\n<hp> <attack> <armor> <piercearmor> <range> <MATERIAL=StatIconsMovementSpeed,1> 1.46 <MATERIAL=StatIconsReloadTime,1> 3"
```

Typical unit entry layout: `Create/Build <b>Name<b> (<cost>, Time: Xs)` → description → `<GREY><DEFAULT>` + conditional/extra info → `Armor Class:` line → `Attack Bonus:` line → stat icon line.

### Formatting Tags

- `\n` - Line break (literally backslash + n inside the quotes, not a real new line)
- `<b>` - Toggles bold. The **same** tag opens and closes: `<b>Longship<b>` (there is no `</b>`)
- `<GREY><DEFAULT>` - Always used together; marks the start of conditional/extra info
- `<cost>`, `<hp>`, `<attack>`, `<armor>`, `<piercearmor>`, `<range>`, `<garrison>` - Filled in by the game with the unit's live values
- `<MATERIAL=IconName,1>` - Inline icon (e.g. `StatIconsMovementSpeed`, `StatIconsReloadTime`, `StatIconsAge3`)
- `•` - Bullet character used in civ descriptions and some lists

Translations must contain exactly the same tags and `\n` line breaks, in the same order, as EN (`tools/validate.py` checks this).

### Writing Conventions

- **Group targets that share the same number:** "+4 vs Gunpowder, Monks" instead of "+4 vs Gunpowder, +4 vs Monks"; "+3 vs Elephants, Buildings".
- **"extra"** marks a bonus that stacks on another one the target also gets, e.g. "+15 vs Cavalry, +15 extra vs Elephants" (elephants are cavalry too).
- **Age-dependent values** are written with slashes plus the ages, e.g. "+3/4 vs Ships in Castle/Imperial Age".
- **Upgrades and techs list only what changes**, not stats that stay the same (e.g. Thalassocracy lists the Harbor's extra HP/armor/range/LoS, not its attack, which equals the Dock's).

### Tag Positioning Rules

`<GREY><DEFAULT>` separates the **general description** from **conditional or special information** (e.g. "Charged attack doesn't work vs buildings", "Gains +5 HP in Imperial Age (civ bonus)"). It goes directly **before** that conditional text, separated from the previous sentence by a space (not `\n`).

```
✓ CORRECT: "...Weak vs archers at long range. <GREY><DEFAULT>Charged attack doesn't work vs buildings.\nAttack Delay: 0.7, LoS: 5..."
✗ WRONG:   "...Weak vs archers at long range. Charged attack doesn't work vs buildings.\nAttack Delay: 0.7, LoS: 5...<GREY><DEFAULT>"
```

When a tag is moved in EN, move it in DE/ES/IT in the same commit.

## Update Workflow

### Standard Update Process

When a new Age of Empires 2: Definitive Edition patch is released:

#### Step 1: Update English (EN) File
1. Open `resources/en/strings/key-value/key-value-modded-strings-utf8.txt`
2. Identify entries that need changes based on patch notes
3. Update tooltip text, stats, bonuses, or descriptions
4. **Search the whole file for every changed stat.** One change usually touches several entries, e.g. a Cataphract buff appears in the Cataphract (26101), Elite Cataphract (26451), Elite Cataphract upgrade (28382) and Byzantine civ description (120156) entries
5. Verify formatting and tag placement
6. Write down the list of changed entry IDs - steps 2-4 must cover exactly the same IDs

#### Step 2: Update German (DE) File
1. Open `resources/de/strings/key-value/key-value-modded-strings-utf8.txt`
2. Apply the equivalent change to **every** entry ID from step 1
3. Use AI translation if needed, but verify against official German game terminology

#### Step 3: Update Spanish (ES) File
1. Open `resources/es/strings/key-value/key-value-modded-strings-utf8.txt`
2. Apply the equivalent change to **every** entry ID from step 1
3. Use AI translation, respecting collaborator style when applicable
4. Note: For DLC content not touched by collaborators, pure AI translation is acceptable

#### Step 4: Update Italian (IT) File
1. Open `resources/it/strings/key-value/key-value-modded-strings-utf8.txt`
2. Apply the equivalent change to **every** entry ID from step 1
3. Use AI translation, but verify against official Italian game terminology

#### Step 5: Sync Copies and Validate (mandatory)
```
python tools/validate.py --sync
```
- `--sync` copies EN to the 12 EN-copy languages (BR, FR, HI, JP, KO, MS, PL, RU, TR, TW, VI, ZH) and ES to MX
- The validator then checks that DE/ES/IT have the same IDs, order, tags and **numbers** as EN, and that all copies are in sync
- A line like `it 26101: numbers differ from EN -> it 26101 EN:13 TR:9` means EN says 13 where IT still says 9: fix the translation
- Only if a difference is pure wording (e.g. "30k" vs "30.000") may it be added to `tools/number_exceptions.txt` (copy the part after `->`)
- **Do not commit until it prints `OK`**

#### Step 6: Git Operations
1. Review changes with `git diff`
2. Stage changed files: `git add resources/` (plus `tools/number_exceptions.txt` if changed)
3. Commit EN + DE + ES + IT + copies together in **one** commit with a descriptive message: `git commit -m "Update tooltips for [patch/feature name]"`
4. Push to repository: `git push`

## Translation Guidelines

### Unit, Building & Tech Names

The game shows the **official** name on buttons and in the selection panel - the mod only replaces the help text. So the official names (from the game files) are the **reference**:

- **Default:** use the official name. If the official name is abbreviated to fit the UI (e.g. ES "Espad. espada larga"), use the full form.
- **Deliberate corrections are allowed** where the official name is clearly wrong or misleading (e.g. DE official "Feuerlanzenreiter" = fire lance *rider*, but the unit is infantry → the mod uses "Feuer-Lanzenträger"). Keep such established mod names.
- **Never allowed:**
  - a name that is the **official name of a different** unit/tech (e.g. ES once called the Watch Tower "Torre de guardia", which is officially the Guard Tower)
  - two different things with the **same** name (ES once used "Huaracas" for both Andean Sling and the Muisca tech)
  - a name with the **wrong meaning** (ES "Fanatismo" for Bimaristan) or a typo
- **One name per thing:** the unit/tech's own tooltip, its upgrade tooltip and the civ description must all use the same name.
- **Do not invent** names with AI. New names come from the official files, or are agreed with the language's reviewer.
- Name changes in DE/ES/IT are reviewed by native speakers first (ES: hebygamer). Review lists live in the gitignored `dont-commit-name-review/` folder.

### Translation Verification Process

1. Check the `dont-commit-original-game-files/` folder for official translations (this folder is gitignored)
2. Search for the English term in official game files
3. Find corresponding DE/ES/IT translations
4. Use the official name for proper nouns, unless the language file already has an established deliberate name for it (see above)
5. Use AI-assisted translation for descriptive text and stats

### Example: Viking Sagas DLC

When the Viking Sagas DLC was added:
- **EN:** "Household Troops" → **DE:** "Hausmacht" (official, not "Herdtruppe")
- **EN:** "Jomsviking" → **DE:** "Jomswikinger" (official)
- **EN:** "Jomsviking" → **ES:** "Vikingo de Jomsborg" (official)
- **EN:** "Household Troops" → **IT:** "Fanteria domestica" (official, not "Truppa del Focolare")

### AI Translation Quality Notes

- **German translations:** Descriptions are fine, but many unit/tech **names** were invented by AI instead of taken from the game (e.g. Keep "Bergfried" vs official "Hauptturm"). A cleanup of ~60 names is pending a native speaker's review - don't add new invented names.
- **Spanish translations:** Mix of collaborator style + AI. Some names differ between a unit's tooltip and the civ descriptions; these are under review with hebygamer.
- **Italian translations:** Verify technical terms against official sources; a name review is pending.

## Common Update Types

### 1. New Unit/Technology Additions

When adding a new unit or technology:
1. Get the entry ID from the game files
2. Write the English tooltip following existing format
3. Translate to DE/ES/IT using official terms + AI for descriptions
4. Sync to all other languages

### 2. Balance Changes

When stats change:
1. Update numerical values in EN - in **every** entry that mentions the stat (unit, elite unit, upgrade tech, civ description)
2. Update DE/ES/IT with same numerical values in the same entries (no translation needed for numbers)
3. Update any changed descriptive text; if a mechanic was removed in EN (e.g. Chieftains no longer generating gold), remove that sentence from the translations too
4. Run `python tools/validate.py --sync` - it must print `OK`

### 3. Tag Repositioning

When moving `<GREY><DEFAULT>` tags:
1. Identify the conditional/special behavior text
2. Move `<GREY><DEFAULT>` before that text
3. Apply to all 4 primary languages (EN/DE/ES/IT)
4. Sync copies

### 4. Armor Class Changes

When armor classes are added/removed:
1. Update the `Armor Class:` line in EN
2. Update the same line in DE (`Rüstungsklasse:`), ES (`Clase de Armadura:`) and IT (`Classe di corazza:`) using the official armor class names
3. Run `python tools/validate.py --sync`

Example: Removing "Unique Unit" armor class:
```
Before: "\nArmor Class: Ship, Long-range Warship, Unique Unit\n"
After:  "\nArmor Class: Ship, Long-range Warship\n"
```

### 5. Civilization Descriptions

When adding civilization description entries (IDs like 120209-120211):
1. Write full civilization description in EN
2. Translate the **mod's EN text** to DE/ES/IT - do not copy the official game civ description, it is less detailed and often outdated (e.g. the official Saracen text still says "Markets cost -100 wood" / "+2 attack vs. buildings")
3. Keep the same bullets and line breaks as EN (one `•` line per unique unit/tech, same order)
4. Maintain entry alignment (ensure proper spacing/ordering)
5. Run `python tools/validate.py --sync`

Civ bonuses also change in balance patches. When one does, update the civ description (1201xx) **and** the related unit/tech entries in all 4 languages.

## Entry Organization

Entries should be organized logically with spacing for readability:

- **Empty row before major sections** (e.g., between 120208 and 120209)
- **Group related entries together** (e.g., all unique techs, all university techs)
- **Maintain consistent ordering** across all language files - DE/ES/IT must have the same entry order and blank lines as EN. When EN is reorganized, reorganize DE/ES/IT in the same commit (the validator reports "entry order differs from EN")

### Example Organization Pattern

```
120208 "Previous entry"

120209 "Section start - Civilization A"
120210 "Civilization B"
120211 "Civilization C"

28051 "Technology section header"
... (related techs)

528005 "Another logical grouping"
```

## Game Mechanics Notes

Things that are not obvious from the game files but affect the numbers in tooltips:

### Infantry Line of Sight (Tracking)

Every unit with the **Infantry** armor class gets **+2 LoS** from **Tracking**, an invisible technology that is researched automatically and for free when reaching the Feudal Age. The mod's LoS values for infantry therefore already include this +2:

- Units available from the Feudal Age onward show the final value, e.g. Man-at-Arms `LoS: 6` (4 base + 2 Tracking)
- Units available in the Dark Age show it separately, e.g. Militia `LoS: 4+2`

When updating infantry LoS from patch notes or game data (which list the base value), **add the +2** - and do not "correct" an infantry LoS back down to the base value.

### Range and LoS are always stated separately

Range and LoS often change together, but **not always**, so a tooltip never relies on "range implies LoS":

- **If LoS changes, it is written out**, e.g. Fletching "+1 range, +1 LoS", Crenellations "+3 range, +3 LoS", Elite Throwing Axeman "+2 range, +2 LoS".
- **If LoS is not mentioned, it does not change.** Examples where only range goes up: Greek Fire, Elite Bolas Rider, Elite Caravel, Elite Janissary, Elite Plumed Archer, Elite Rattan Archer, Elite Jarl. No "LoS unchanged" note is needed.
- Effects that add LoS **without** range are written out too: Fletching/Bodkin Arrow/Bracer give Town Centers "+1 attack, +1 LoS (no range)"; Siege Engineers gives Rams & Siege Towers "+1 LoS".

When adding a new tech or upgrade that changes range, check the LoS effect separately (in-game or in the Advanced Genie Editor) - don't assume it.

### `*` = civ bonus already applied

When a unit or tech belongs to one civ (unique units, unique techs, civ-specific buildings) and a civ bonus of that civ **always** affects a stat, the tooltip shows the value **with the bonus applied and marked with `*`**. Examples:

- Janissary `Time: 16.8s*` (Turkish gunpowder units created faster), Jaguar Warrior `Time: 10.4s*` (Aztec military units created faster)
- Woad Raider speed `1.35*` (Celtic infantry speed), Kipchak speed `1.54*` (Cuman mounted speed)
- Longbowman `LoS: 8*` (Briton archer bonus), Grenadier `LoS: 9*` (Jurchen team bonus), Warrior Priest `LoS: 7*` (3 base + 2 Tracking + 2 Armenian infantry bonus)
- Paper Money `Time: 45s*` (60s base, shortened by the Vietnamese free Conscription)

So a value that differs from the game data **and** has a `*` is intentional. If you add or update such a value, keep the `*` - and add one wherever a civ bonus is baked in but the `*` is missing. Infantry Tracking (+2 LoS) is universal, so it does **not** get a `*`.

### Attack delay formulas

The game does not show attack delays, so they are calculated from the unit's graphics data and **rounded up** to 2 decimals:

- **Melee attack delay** = attack animation duration ÷ 2. Example: Scout Cavalry line / Steppe Lancer 1.5 ÷ 2 = 0.75; Ghulam, Kamayuk 1 ÷ 2 = 0.5; Fire Lancer 0.625 → 0.63
- **Ranged attack delay** = animation duration × frame delay ÷ frames per angle. Example: Scorpion 0.8 × 12 ÷ 60 = 0.16; Heavy Scorpion 0.8 × 6 ÷ 30 = 0.16; Hearth Troop javelin 1.8 × 23 ÷ 45 = 0.92
- Units with both a melee and a ranged attack (secondary attack "attack B" in the data) show both: `Melee Attack Delay: X, Ranged Attack Delay: Y` (Jomsviking, Hearth Troop, Fire Lancer)

### Reference data

`dont-commit-techtree-data/data.json` (gitignored) is a copy of the community data from [SiegeEngineers/aoe2techtree](https://github.com/SiegeEngineers/aoe2techtree) (`data/data.json`). It can be used to **check** base unit stats (train time, LoS, speed, reload, accuracy, attack bonuses, armor classes) - **not** as a writing format. Each unit's tooltip ID is its `LanguageNameId` + 21000 (e.g. Archer 5083 → 26083). Known gaps in that data: melee attack delays are listed as 0, scout-line LoS lacks the automatic age-up bonus, and civ bonuses are not applied.

## Special Considerations

### Pompeii Mode

The `modes/Pompeii/` folder contains a variant for a special game mode. This typically mirrors the main EN file but may have mode-specific changes.

Update this file separately when needed, but it's not part of the standard sync process.

### .gitignore

The `.gitignore` file excludes:
```
dont-commit-original-game-files/
dont-commit-techtree-data/
dont-commit-name-review/
dont-commit-changelogs/
__pycache__/
```

**Important:** The folder with original game files only exists on the project maintainer's (harooooo's) PC. It contains reference files from the official Age of Empires 2: DE installation for translation verification purposes, but these files should never be committed to the repository due to copyright/licensing restrictions.

If you need access to official game translations for verification and don't have these files, contact harooooo for assistance.

`dont-commit-techtree-data/` holds a downloaded copy of the community aoe2techtree `data.json` (see "Reference data" above). Re-download it after a game patch from `https://raw.githubusercontent.com/SiegeEngineers/aoe2techtree/master/data/data.json`.

## Troubleshooting

### Common Issues

**Issue:** Translations don't match official game
- **Solution:** Check `dont-commit-original-game-files/` for official translations

**Issue:** Tags not rendering correctly in-game
- **Solution:** Verify tag syntax: `<b>Name<b>` (same tag opens and closes), `<GREY><DEFAULT>`, `<cost>` etc., `\n` for line breaks

**Issue:** Inconsistent formatting, outdated numbers or wrong order across languages
- **Solution:** Run `python tools/validate.py` - it lists every entry that differs from EN

**Issue:** Synced files out of date
- **Solution:** Run `python tools/validate.py --sync` (EN → 12 copy languages, ES → MX)

## Version Control Best Practices

1. **Descriptive commit messages:** Clearly state what was changed and why
2. **Group related changes:** All language updates for a single feature should be in one commit
3. **Review before committing:** Use `git diff` to verify all changes are intentional
4. **Never commit original game files:** Keep those in the gitignored folder only

## Quick Reference Commands

### Syncing and Validating

```powershell
# Copy EN -> 12 EN-copy languages and ES -> MX, then check everything
python tools/validate.py --sync

# Only check (no copying)
python tools/validate.py
```

### Git Workflow

```powershell
# Stage changes
git add resources/

# Commit
git commit -m "Descriptive message"

# Push
git push
```

## Summary for AI Agents

When working on this project:

1. **Always update all 4 primary languages** (EN, DE, ES, IT) for any tooltip changes, in the same commit
2. **Update every entry a stat appears in** (unit, elite unit, upgrade tech, civ description) - search the whole EN file
3. **Translate from the current EN text**, not from the official civ descriptions or an older translation
4. **Use official names** for units/techs (verify in original game files), except established deliberate corrections; never reuse another unit's official name, and use one name per thing everywhere
5. **Maintain formatting consistency** across all language files (same order, tags, `\n`, bullets as EN)
6. **Position tags correctly** (`<GREY><DEFAULT>` before conditional/special text)
7. **Run `python tools/validate.py --sync` and make sure it prints `OK`** before committing - never silence an error by adding an exception unless the difference is pure wording
8. **Only commit and push when the maintainer asks you to**, and report what you changed per language
9. **Infantry LoS includes +2 from Tracking** (free automatic Feudal Age tech) - see "Game Mechanics Notes"
10. **`*` marks a value with a civ bonus always applied** - keep it, and add it where it's missing
11. **Range and LoS are stated separately** - if LoS changes, write it; if it isn't written, it doesn't change

This mod requires careful attention to multi-language consistency and adherence to official Age of Empires 2: DE terminology for the best user experience.
