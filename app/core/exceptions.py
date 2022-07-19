from pydantic import BaseModel


class ModelError404(BaseModel):
    detail: str
