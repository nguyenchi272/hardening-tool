from sqlalchemy.orm import Session

from app.db.models.credentials \
    import Credential

from app.core.crypto \
    import decrypt


class CredentialResolver:

    def resolve(
        self,
        db: Session,
        credential_id: int
    ):

        credential = db.query(
            Credential
        ).filter(
            Credential.id ==
                credential_id
        ).first()

        if not credential:

            raise Exception(
                "Credential not found"
            )

        password = decrypt(
            credential.encrypted_password
        )

        return {

            "username":
                credential.username,

            "password":
                password,

            "sudo_enabled":
                credential.sudo_enabled
        }