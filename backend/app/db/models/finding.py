# finding.py
from sqlalchemy \
    import Column
from sqlalchemy.orm \
    import relationship
from sqlalchemy \
    import Integer
from sqlalchemy \
    import String
from sqlalchemy \
    import Text
from sqlalchemy \
    import ForeignKey

from app.db.database \
    import Base


class FindingRecord(Base):

    __tablename__ = "findings"
    scan = relationship(
        "Scan"
    )

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    scan_id = Column(
        Integer,
        ForeignKey("scans.id")
    )

    finding_id = Column(String)

    title = Column(String)

    severity = Column(String)

    evidence = Column(Text)

    remediation = Column(Text)

    status = Column(String)