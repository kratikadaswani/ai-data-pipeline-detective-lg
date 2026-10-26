
from enum import Enum
from pydantic import BaseModel, Field


class Severity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class PipelineType(str, Enum):
    SPARK = "Spark"
    KAFKA = "Kafka"
    AIRFLOW = "Airflow"
    OTHER = "Other"


class IncidentReport(BaseModel):
    pipeline: PipelineType = Field(
        description="Pipeline technology being investigated"
    )

    error_type: str = Field(
        description="Error category or exception name"
    )

    severity: Severity = Field(
        description="Estimated incident severity"
    )

    summary: str = Field(
        description="Short explanation of the observed failure"
    )

    probable_causes: list[str] = Field(
        description="Possible causes supported by the available log"
    )

    evidence: list[str] = Field(
        description="Relevant exact excerpts from the supplied log"
    )

    recommended_actions: list[str] = Field(
        description="Safe diagnostic checks to investigate the issue"
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description=(
            "Model-estimated confidence between 0 and 1. "
            "This is not a calibrated probability."
        )
    )

    needs_more_information: bool = Field(
        description="Whether the available evidence is insufficient"
    )
