from sqlalchemy \
    import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.orm \
    import relationship

from app.db.database \
    import Base

class Credential(Base):

    __tablename__ = "credentials"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(String)

    username = Column(String)

    encrypted_password = Column(String)

    ssh_key = Column(Text)

    sudo_enabled = Column(Boolean)

    created_at = Column(DateTime)