from fastapi import APIRouter
from pydantic import BaseModel

from app.services.remediation_service \
    import RemediationService

router = APIRouter()


class FixRequest(BaseModel):

    host: str

    username: str

    password: str

    finding_id: str


@router.post("/fix")
def fix_finding(
    payload: FixRequest
):

    result = \
        RemediationService().fix_finding(

            payload.host,

            payload.username,

            payload.password,

            payload.finding_id
        )

    return result