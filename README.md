# Golf Coaching NER

A data-free reference implementation for identifying domain-specific concepts
in golf coaching language.

This repository accompanies a master's dissertation on domain-specific Named
Entity Recognition (NER). It documents the methodology and contains small,
reusable Python modules for:

- splitting a text corpus without mixing source groups;
- converting Label Studio span annotations into a simple format; and
- building a case-insensitive spaCy dictionary matcher.

## Entity schema

| Entity | Purpose |
| --- | --- |
| FAULT | Explicitly stated swing or shot faults |
| SWING_PHASE | Phases or positions within the golf swing |
| BALL_FLIGHT | Descriptions of ball-flight behaviour |
| CONTACT_OUTCOME | Impact and strike outcomes |
| DRILL | Practice drills or exercises |
| TECHNICAL_CONCEPT | Technical variables such as low point or club path |

## Repository structure

    config/                  Entity schema only
    docs/                    Methodology and data-governance notes
    src/golf_ner/            Harmless, data-independent Python modules

## Data availability

No TikTok records, video identifiers, usernames, transcripts, annotations,
credentials, model outputs, or proprietary datasets are included.

The original research data is deliberately kept outside this public repository
because access, redistribution, privacy, and platform requirements must be
handled separately. Anyone using these modules must supply data they are
authorised to process.

## Installation

    python -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt

On Windows PowerShell:

    py -m venv .venv
    .\.venv\Scripts\Activate.ps1
    py -m pip install -r requirements.txt

## Security

The code does not contain API calls or require credentials. Local datasets,
environment files, access tokens, annotations, models, and generated outputs
are excluded by the gitignore rules.

See SECURITY.md and docs/data-governance.md before adapting the project.

## Status

This is a portfolio and methodology repository. It is intentionally not a
complete reproduction package because the underlying research corpus is not
redistributed.

