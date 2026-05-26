from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session \
    import get_db

from app.models.credential \
    import (
        CredentialCreate
    )

from app.services.credential_service \
    import CredentialService

router = APIRouter()


@router.post("/credentials")
def create_credential(
    payload: CredentialCreate,
    db: Session = Depends(get_db)
):

    credential = \
        CredentialService() \
            .create_credential(

                db,

                payload.name,

                payload.username,

                payload.password,

                payload.sudo_enabled
            )

    return {

        "id": credential.id,

        "name": credential.name,

        "username":
            credential.username,

        "sudo_enabled":
            credential.sudo_enabled
    }


@router.get("/credentials")
def get_credentials(
    db: Session = Depends(get_db)
):

    credentials = \
        CredentialService() \
            .get_credentials(db)

    return [

        {
            "id": c.id,
            "name": c.name,
            "username": c.username,
            "sudo_enabled":
                c.sudo_enabled
        }

        for c in credentials
    ]