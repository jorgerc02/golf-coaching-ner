# Methodology overview

The dissertation investigates whether a domain-specific NER system can identify
technical golf-coaching concepts more reliably than a general-purpose language
pipeline.

The research workflow is:

1. collect authorised English-language coaching material;
2. filter for technically relevant golf instruction;
3. define and revise an annotation schema;
4. manually annotate development and evaluation samples;
5. extract candidate terminology for a controlled thesaurus;
6. build a rule-based spaCy baseline;
7. compare the baseline with statistical and transformer approaches; and
8. evaluate using entity-level precision, recall, and F1.

## Annotation principles

- Annotate only the text span that expresses the entity.
- Label FAULT only when the fault is explicit.
- Keep technical concepts separate from ball flight and contact outcomes.
- Resolve ambiguous terms from their sentence context.
- Keep the evaluation set manually reviewed and separate from weak labels.

## Reproducibility boundary

The public repository documents the process and reusable code structure. It
does not reproduce the private corpus. Results should be reported as aggregate
metrics rather than individual platform records.

