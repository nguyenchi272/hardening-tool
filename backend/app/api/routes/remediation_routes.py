from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session \
    import get_db
from app.db.models.asset \
    import Asset
from app.models.fix import FixRequest
from app.services.credential_service import CredentialService
from app.services.remediation_service import RemediationService

router = APIRouter()


@router.post("/fix")
def fix_finding(
    payload: FixRequest,
    db: Session = Depends(get_db)
):

    asset = db.query(
        Asset
    ).filter(
        Asset.id ==
        payload.asset_id
    ).first()

    if not asset:

        return {
            "error":
                "Asset not found"
        }

    credential = \
        CredentialService() \
            .get_credential_by_id(
                db,
                asset.credential_id
            )

    if not credential:

        return {
            "error":
                "Credential not found"
        }

    result = \
        RemediationService().fix_finding(

            asset.ip_address,

            credential.username,

            credential.password,

            payload.finding_id
        )
    
    print(payload)

    return result