# finding.py
from pydantic import BaseModel
from typing import List


class Finding(BaseModel):

    id: int

    finding_id: str

    title: str

    severity: str

    risk_score: int

    category: str

    description: str

    impact: str

    evidence: str

    remediation: str

    references: List[str]

    compliance: List[str]

    tags: List[str]

    server: str

    status: str