from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.db.database import Base


class Asset(Base):

    __tablename__ = "assets"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    credential_id = Column(
        Integer,
        ForeignKey("credentials.id")
    )

    hostname = Column(String)

    ip_address = Column(String)

    os = Column(String)

    status = Column(String)

    scans = relationship(
        "Scan",
        back_populates="asset"
    )

    credential = relationship(
        "Credential"
    )