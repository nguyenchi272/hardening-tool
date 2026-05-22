from app.db.database \
    import engine

from app.db.models.asset \
    import Asset

from app.db.models.scan \
    import Scan

from app.db.models.finding \
    import FindingRecord

from app.db.database \
    import Base


Base.metadata.create_all(
    bind=engine
)

print("DB initialized")