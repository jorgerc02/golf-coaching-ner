"""Build a case-insensitive spaCy matcher from user-supplied terms."""

from collections.abc import Iterable

import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span


Term = tuple[str, str]


def build_dictionary_matcher(
    terms: Iterable[Term],
    language: str = "en",
) -> tuple[spacy.language.Language, PhraseMatcher]:
    """Return a blank spaCy pipeline and a matcher.

    Each item in terms is a pair of text and entity label. The caller is
    responsible for supplying terms they are authorised to use.
    """

    nlp = spacy.blank(language)
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

    grouped_terms: dict[str, list[str]] = {}
    for text, label in terms:
        clean_text = text.strip()
        clean_label = label.strip().upper()
        if clean_text and clean_label:
            grouped_terms.setdefault(clean_label, []).append(clean_text)

    for label, values in grouped_terms.items():
        patterns = [nlp.make_doc(value) for value in sorted(set(values))]
        matcher.add(label, patterns)

    return nlp, matcher


def find_entities(
    nlp: spacy.language.Language,
    matcher: PhraseMatcher,
    text: str,
) -> list[Span]:
    """Find non-overlapping dictionary matches in text."""

    doc = nlp(text)
    spans = [
        Span(doc, start, end, label=nlp.vocab.strings[match_id])
        for match_id, start, end in matcher(doc)
    ]
    return spacy.util.filter_spans(spans)

