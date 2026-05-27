from sqlalchemy.orm \
    import Session

from datetime \
    import datetime

from app.db.models.credentials \
    import Credential

from app.core.crypto \
    import encrypt, decrypt


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
                sudo_enabled,

            created_at=
                datetime.utcnow()
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

    def get_credential_by_id(
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

            return None

        #
        # Attach decrypted password
        #
        credential.password = decrypt(
            credential.encrypted_password
        )

        return credential

    def delete_credential(
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

        if credential:

            db.delete(credential)

            db.commit()