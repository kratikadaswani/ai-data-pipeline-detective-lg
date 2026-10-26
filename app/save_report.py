
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from schemas import IncidentReport


def save_incident(report: IncidentReport) -> Path:
    output_dir = Path("data/incidents")
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"incident_{timestamp}_{uuid4().hex[:8]}.json"
    )

    output_path = output_dir / filename

    output_path.write_text(
        report.model_dump_json(indent=2),
        encoding="utf-8"
    )

    return output_path
