from typing import Optional
from pydantic import BaseModel


# Shared properties
class StudentBase(BaseModel):
    code: int
    first_name: str
    last_name: str
    program: int
    sede: int
    jornada: str
    type_doc: str
    document: str
    bajos_rendimientos: bool
    per_matriculados: int
    per_cancelados: int
    m_tesis: bool
    m_activo: bool
    m_periodo_activo: str
    m_grado: bool
    sexo: str
    birth_date: str
    estrato: int


# Properties to receive on item creation
class StudentCreate(StudentBase):
    pass


# Properties to receive on item update
class StudentUpdate(StudentBase):
    pass

# Properties shared by models stored in DB
class StudentInDBBase(StudentBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Properties to return to client
class Student(StudentInDBBase):
    pass


# Properties properties stored in DB
class StudentInDB(StudentInDBBase):
    pass
