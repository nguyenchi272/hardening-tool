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

    host: str

    status: str

    auto_fix_supported: bool = False

    requires_restart: bool = False

    requires_reboot: bool = False

    manual_review: bool = False