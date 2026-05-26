from pydantic import BaseModel


class CredentialCreate(BaseModel):

    name: str

    username: str

    password: str

    sudo_enabled: bool = False


class CredentialResponse(BaseModel):

    id: int

    name: str

    username: str

    sudo_enabled: bool