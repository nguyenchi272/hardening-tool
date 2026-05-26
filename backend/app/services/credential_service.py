from sqlalchemy.orm import Session

from app.db.models.credentials import Credential

from app.core.crypto import encrypt


class CredentialService:

    def create_credential(
        self,
        db: Session,
        name: str,
        username: str,
        password: str,
        sudo_enabled: bool
    ):

        credential = Credential(

            name=name,

            username=username,

            encrypted_password=
                encrypt(password),

            sudo_enabled=
                sudo_enabled
        )

        db.add(credential)

        db.commit()

        db.refresh(credential)

        return credential

    def get_credentials(
        self,
        db: Session
    ):

        return db.query(
            Credential
        ).all()