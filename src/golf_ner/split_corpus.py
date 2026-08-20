"""Create deterministic grouped train, development, and test splits."""

import random
from collections.abc import Iterable
from typing import Any


def grouped_split(
    records: Iterable[dict[str, Any]],
    group_key: str,
    seed: int = 42,
    train_ratio: float = 0.8,
    development_ratio: float = 0.1,
) -> dict[str, list[dict[str, Any]]]:
    """Split records while keeping every source group in one partition."""

    groups: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        group = str(record[group_key])
        groups.setdefault(group, []).append(record)

    group_names = sorted(groups)
    random.Random(seed).shuffle(group_names)

    train_end = round(len(group_names) * train_ratio)
    development_end = train_end + round(
        len(group_names) * development_ratio
    )
    selected = {
        "train": group_names[:train_end],
        "development": group_names[train_end:development_end],
        "test": group_names[development_end:],
    }

    return {
        split_name: [
            record
            for group in split_groups
            for record in groups[group]
        ]
        for split_name, split_groups in selected.items()
    }

