# asset.py
from sqlalchemy \
    import Column, Integer, String
from sqlalchemy.orm \
    import relationship

from app.db.database \
    import Base


class Asset(Base):

    __tablename__ = "assets"
    scans = relationship(
        "Scan"
    )

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    hostname = Column(String)

    ip_address = Column(String)

    os = Column(String)

    status = Column(String)