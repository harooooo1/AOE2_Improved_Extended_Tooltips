# AOE2 Improved Extended Tooltips - Project Guide

## Project Overview

This is a tooltip modification for **Age of Empires 2: Definitive Edition** that enhances in-game tooltips with additional information, clarifications, and extended descriptions. The mod supports multiple languages with a hierarchical translation system.

**Project Maintainer:** harooooo (Discord/in-game nickname)  
**Spanish Collaborator:** hebygamer

For questions or additional information about the project, contact harooooo on Discord or in-game.

## File Structure

```
AOE2_Improved_Extended_Tooltips/
├── info.json                                    # Mod metadata
├── README.md                                    # User-facing documentation
├── PROJECT_GUIDE.md                             # This file - AI/developer guide
├── .gitignore                                   # Excludes original game files
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

### Secondary Languages (13 languages - English copies)

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

Each language file follows this structure:

```
ID "Tooltip text with formatting"
```

### Example Entry

```
26106 "Longship\n<GREY>Viking Unique Unit (requires Castle)\n<DEFAULT><LINE>Strong anti-ship unit. Capable against buildings.\nStrong vs. Ships.\nWeak vs. Melee attacks.\n<i>Armor classes:</i> Ship\n<i>Attack bonuses:</i> +4 Fishing Ship, +4 Sailing Ship, +4 Ship, +9 Mameluke, +6 Building, +5 Camel"
```

### Formatting Tags

- `\n` - Line break
- `<GREY>` - Grey flavor text (unit name, class)
- `<DEFAULT>` - Returns to default white text color
- `<LINE>` - Horizontal separator line
- `<i>text</i>` - Italic text
- `<b>text</b>` - Bold text

### Tag Positioning Rules

The `<GREY><DEFAULT>` tag pair separates **flavor text** (unit type, requirements) from **gameplay information** (stats, bonuses).

**Correct positioning:**
```
"Unit Name\n<GREY>Description\n<DEFAULT><LINE>Stats and info\nConditional info"
```

**Important:** When a unit has conditional or special behavior text, the `<GREY><DEFAULT>` should come **before** that conditional text, not at the very end. This keeps flavor separate from mechanics.

Example:
```
✓ CORRECT: "...<DEFAULT><LINE>...\n(Conversion time doubled when garrisoned)\nStats here"
✗ WRONG:   "...<LINE>...\n(Conversion time doubled when garrisoned)\nStats here<GREY><DEFAULT>"
```

## Update Workflow

### Standard Update Process

When a new Age of Empires 2: Definitive Edition patch is released:

#### Step 1: Update English (EN) File
1. Open `resources/en/strings/key-value/key-value-modded-strings-utf8.txt`
2. Identify entries that need changes based on patch notes
3. Update tooltip text, stats, bonuses, or descriptions
4. Verify formatting and tag placement

#### Step 2: Update German (DE) File
1. Open `resources/de/strings/key-value/key-value-modded-strings-utf8.txt`
2. Apply equivalent changes to the same entry IDs
3. Use AI translation if needed, but verify against official German game terminology

#### Step 3: Update Spanish (ES) File
1. Open `resources/es/strings/key-value/key-value-modded-strings-utf8.txt`
2. Apply equivalent changes to the same entry IDs
3. Use AI translation, respecting collaborator style when applicable
4. Note: For DLC content not touched by collaborators, pure AI translation is acceptable

#### Step 4: Update Italian (IT) File
1. Open `resources/it/strings/key-value/key-value-modded-strings-utf8.txt`
2. Apply equivalent changes to the same entry IDs
3. Use AI translation, but verify against official Italian game terminology

#### Step 5: Sync English Copies
Copy the updated EN file to all secondary language folders:
- `resources/br/strings/key-value/key-value-modded-strings-utf8.txt`
- `resources/fr/strings/key-value/key-value-modded-strings-utf8.txt`
- `resources/hi/strings/key-value/key-value-modded-strings-utf8.txt`
- `resources/jp/strings/key-value/key-value-modded-strings-utf8.txt`
- `resources/ko/strings/key-value/key-value-modded-strings-utf8.txt`
- `resources/ms/strings/key-value/key-value-modded-strings-utf8.txt`
- `resources/pl/strings/key-value/key-value-modded-strings-utf8.txt`
- `resources/ru/strings/key-value/key-value-modded-strings-utf8.txt`
- `resources/tr/strings/key-value/key-value-modded-strings-utf8.txt`
- `resources/tw/strings/key-value/key-value-modded-strings-utf8.txt`
- `resources/vi/strings/key-value/key-value-modded-strings-utf8.txt`
- `resources/zh/strings/key-value/key-value-modded-strings-utf8.txt`

#### Step 6: Sync Spanish to Mexican Spanish
Copy the updated ES file to:
- `resources/mx/strings/key-value/key-value-modded-strings-utf8.txt`

#### Step 7: Git Operations
1. Review changes with `git diff`
2. Stage changed files: `git add resources/`
3. Commit with descriptive message: `git commit -m "Update tooltips for [patch/feature name]"`
4. Push to repository: `git push`

## Translation Guidelines

### Using Official Game Translations

When updating tooltips for new units, technologies, or civilizations, **always reference the official Age of Empires 2: DE translations** from the game files. This ensures consistency with the base game.

**DO NOT** invent translations or rely purely on AI without verification for proper nouns (unit names, technology names, civilization names).

### Translation Verification Process

1. Check the `dont-commit-original-game-files/` folder for official translations (this folder is gitignored)
2. Search for the English term in official game files
3. Find corresponding DE/ES/IT translations
4. Use official translations for proper nouns
5. Use AI-assisted translation for descriptive text and stats

### Example: Viking Sagas DLC

When the Viking Sagas DLC was added:
- **EN:** "Household Troops" → **DE:** "Hausmacht" (official, not "Herdtruppe")
- **EN:** "Jomsviking" → **DE:** "Jomswikinger" (official)
- **EN:** "Jomsviking" → **ES:** "Vikingo de Jomsborg" (official)
- **EN:** "Household Troops" → **IT:** "Fanteria domestica" (official, not "Truppa del Focolare")

### AI Translation Quality Notes

- **German translations:** Generally reliable for game terminology
- **Spanish translations:** Mix of collaborator style + AI, pay attention to consistency
- **Italian translations:** Verify technical terms against official sources

## Common Update Types

### 1. New Unit/Technology Additions

When adding a new unit or technology:
1. Get the entry ID from the game files
2. Write the English tooltip following existing format
3. Translate to DE/ES/IT using official terms + AI for descriptions
4. Sync to all other languages

### 2. Balance Changes

When stats change:
1. Update numerical values in EN
2. Update DE/ES/IT with same numerical values (no translation needed for numbers)
3. Update any changed descriptive text
4. Sync copies

### 3. Tag Repositioning

When moving `<GREY><DEFAULT>` tags:
1. Identify the conditional/special behavior text
2. Move `<GREY><DEFAULT>` before that text
3. Apply to all 4 primary languages (EN/DE/ES/IT)
4. Sync copies

### 4. Armor Class Changes

When armor classes are added/removed:
1. Update the `<i>Armor classes:</i>` line in EN
2. Translate the armor class name for DE/ES/IT
3. Sync copies

Example: Removing "Unique Unit" armor class:
```
Before: "<i>Armor classes:</i> Ship, Unique Unit"
After:  "<i>Armor classes:</i> Ship"
```

### 5. Civilization Descriptions

When adding civilization description entries (IDs like 120209-120211):
1. Write full civilization description in EN
2. Translate to DE/ES/IT
3. Maintain entry alignment (ensure proper spacing/ordering)
4. Sync copies

## Entry Organization

Entries should be organized logically with spacing for readability:

- **Empty row before major sections** (e.g., between 120208 and 120209)
- **Group related entries together** (e.g., all unique techs, all university techs)
- **Maintain consistent ordering** across all language files

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

## Special Considerations

### Pompeii Mode

The `modes/Pompeii/` folder contains a variant for a special game mode. This typically mirrors the main EN file but may have mode-specific changes.

Update this file separately when needed, but it's not part of the standard sync process.

### .gitignore

The `.gitignore` file excludes:
```
dont-commit-original-game-files/
```

**Important:** This folder with original game files only exists on the project maintainer's (harooooo's) PC. It contains reference files from the official Age of Empires 2: DE installation for translation verification purposes, but these files should never be committed to the repository due to copyright/licensing restrictions.

If you need access to official game translations for verification and don't have these files, contact harooooo for assistance.

## Troubleshooting

### Common Issues

**Issue:** Translations don't match official game
- **Solution:** Check `dont-commit-original-game-files/` for official translations

**Issue:** Tags not rendering correctly in-game
- **Solution:** Verify tag syntax: `<GREY>`, `<DEFAULT>`, `<LINE>`, `\n` for line breaks

**Issue:** Inconsistent formatting across languages
- **Solution:** Compare EN file structure, ensure all languages match the same formatting pattern

**Issue:** Synced files out of date
- **Solution:** After updating EN/DE/ES/IT, always sync BR/FR/HI/JP/KO/MS/PL/RU/TR/TW/VI/ZH from EN, and MX from ES

## Version Control Best Practices

1. **Descriptive commit messages:** Clearly state what was changed and why
2. **Group related changes:** All language updates for a single feature should be in one commit
3. **Review before committing:** Use `git diff` to verify all changes are intentional
4. **Never commit original game files:** Keep those in the gitignored folder only

## Quick Reference Commands

### Syncing Files (PowerShell)

```powershell
# Sync EN to all EN-copy languages
$enFile = "resources\en\strings\key-value\key-value-modded-strings-utf8.txt"
$enCopyLangs = @("br", "fr", "hi", "jp", "ko", "ms", "pl", "ru", "tr", "tw", "vi", "zh")
foreach ($lang in $enCopyLangs) {
    Copy-Item $enFile "resources\$lang\strings\key-value\key-value-modded-strings-utf8.txt"
}

# Sync ES to MX
Copy-Item "resources\es\strings\key-value\key-value-modded-strings-utf8.txt" "resources\mx\strings\key-value\key-value-modded-strings-utf8.txt"
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

1. **Always update all 4 primary languages** (EN, DE, ES, IT) for any tooltip changes
2. **Sync copies after primary updates** (EN → 13 languages, ES → MX)
3. **Use official game translations** for proper nouns (verify in original game files)
4. **Maintain formatting consistency** across all language files
5. **Position tags correctly** (`<GREY><DEFAULT>` before conditional/special text)
6. **Commit and push** after completing a logical set of changes

This mod requires careful attention to multi-language consistency and adherence to official Age of Empires 2: DE terminology for the best user experience.
