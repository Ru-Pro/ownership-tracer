# Ownership Tracer

Find out who owns a Russian public company from official open sources, with a source link for every fact.
A skill for Claude and for ChatGPT.

**Tutorial:** [How to Trace the Owners of a Russian Public Company](TUTORIAL_URL)

## Download

Download **one** file, for the assistant you use:

| You use | Download | Install |
|---|---|---|
| **Claude** (Claude Code) | [e-disclosure-shareholders.zip](https://github.com/Ru-Pro/ownership-tracer/releases/latest/download/e-disclosure-shareholders.zip) | Claude → Customize → Skills → + → Upload a skill ([guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude)) |
| **ChatGPT** (Business, Enterprise, Edu, Healthcare) | [e-disclosure-chatgpt.zip](https://github.com/Ru-Pro/ownership-tracer/releases/latest/download/e-disclosure-chatgpt.zip) | ChatGPT → Plugins → Skills → Create → Upload from your computer ([guide](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)) |

Do not use the green **Code → Download ZIP** button: that is the source code, not a skill.

## What it does

- Collects ownership disclosures of a company from e-disclosure.ru and the other accredited disclosure
  agencies (AK&M, PRIME, SKRIN, AZIPI).
- Extracts every stake: holder, direct or indirect control, stake before and after, date, control chain.
- Continues the chains through the Russian company register (ЕГРЮЛ): LLC participants, pledges of stakes,
  directors.
- Adds financial statements of the chain companies (ГИР БО) and Moscow Exchange data: shares outstanding,
  stake values, large negotiated deals.
- Screens everyone in the structure against sanctions lists (OpenSanctions).
- Writes the answer in Russian or English, with a link to the source of every fact.

## Repository layout

| Path | Content |
|---|---|
| `scripts/` | all scripts (one copy, shared by both skills) |
| `skills/claude/` | Claude skill: `SKILL.md`, user guides in Russian and English |
| `skills/chatgpt/` | ChatGPT skill: `SKILL.md`, `references/METHOD.md` |
| `tutorial/` | the tutorial and SEO texts for the website |
| `build.py` | builds both ZIPs into `dist/` |

## Releasing a new version

1. Build the archives: `python3 build.py` (they appear in `dist/`).
2. On GitHub: **Releases → Draft a new release**, create a new tag (for example `v1.1`), paste the text
   of `RELEASE_NOTES.md`, attach both ZIPs from `dist/`, and publish.

The download links above always point to the latest release, so the README and the tutorial do not need
changing.

## Data and licences

The repository contains code only, no collected data. The tool uses public information: issuer
disclosures, the Federal Tax Service register and financial statements, Moscow Exchange market data.
Sanctions data comes from OpenSanctions under CC BY-NC 4.0: non-commercial use, credit OpenSanctions in
publications.

Русская версия: [README.ru.md](README.ru.md)
