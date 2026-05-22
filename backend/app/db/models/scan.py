# scan.py
from sqlalchemy \
    import Column
from sqlalchemy.orm \
    import relationship
from sqlalchemy \
    import Integer
from sqlalchemy \
    import String
from sqlalchemy \
    import DateTime
from sqlalchemy \
    import ForeignKey

from datetime \
    import datetime

from app.db.database \
    import Base


class Scan(Base):

    __tablename__ = "scans"
    asset = relationship(
    "Asset"
    )

    findings = relationship(
        "FindingRecord"
    )

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    asset_id = Column(
        Integer,
        ForeignKey("assets.id")
    )

    status = Column(String)

    started_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    completed_at = Column(
        DateTime,
        nullable=True
    )