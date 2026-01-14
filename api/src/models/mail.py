from pydantic import BaseModel

class Mail(BaseModel):
    to_address: str
    subject: str
    body: str
