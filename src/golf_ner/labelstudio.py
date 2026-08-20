"""Convert a generic Label Studio span export into simple records."""

from typing import Any


def convert_task(task: dict[str, Any]) -> dict[str, Any]:
    """Convert one task without retaining Label Studio user metadata."""

    text = str(task.get("data", {}).get("text", ""))
    annotations = task.get("annotations") or []
    spans: list[dict[str, Any]] = []

    for annotation in annotations:
        for result in annotation.get("result", []):
            value = result.get("value", {})
            labels = value.get("labels") or []
            if not labels:
                continue
            spans.append(
                {
                    "start": int(value["start"]),
                    "end": int(value["end"]),
                    "label": str(labels[0]),
                }
            )

    return {"text": text, "entities": spans}

