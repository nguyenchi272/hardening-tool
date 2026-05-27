from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session \
    import get_db

from app.models.credential \
    import (
        CredentialCreate
    )

from app.services.credential_service \
    import CredentialService
from app.db.models.asset import Asset
from app.db.models.credentials import Credential

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

@router.delete("/credentials/{credential_id}")
def delete_credential(
    credential_id: int,
    db: Session = Depends(get_db)
):

    #
    # Check assets using credential
    #
    asset_using = (
        db.query(Asset)
        .filter(
            Asset.credential_id == credential_id
        )
        .first()
    )

    if asset_using:

        raise HTTPException(
            status_code=400,
            detail=(
                "Credential is assigned "
                "to one or more assets"
            )
        )

    credential = (
        db.query(Credential)
        .filter(
            Credential.id == credential_id
        )
        .first()
    )

    if not credential:

        raise HTTPException(
            status_code=404,
            detail="Credential not found"
        )

    db.delete(credential)

    db.commit()

    return {
        "status": "deleted"
    }