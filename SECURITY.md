# Security

## Credentials

This repository must never contain API keys, client secrets, access tokens,
passwords, private keys, or populated environment files.

Use local environment variables for any future external service. The
.env.example file must contain names and comments only, never working values.

## Research data

Do not commit raw or derived research records, including:

- platform usernames or content identifiers;
- transcripts or captions;
- Label Studio or Sketch Engine exports;
- corpus splits;
- spaCy DocBin files;
- model predictions; or
- spreadsheets containing annotations.

Only aggregate, non-identifying results should be published here.

## Reporting a problem

If a credential or sensitive record is committed, revoke the credential first.
Removing the latest copy is not sufficient because Git retains earlier
versions. Rewrite the affected history or replace the repository with a clean
snapshot before making it public.

