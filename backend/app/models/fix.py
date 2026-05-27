from pydantic \
    import BaseModel


class FixRequest(BaseModel):

    asset_id: int

    finding_id: str