from app.crud.base import CRUDBase
from app.models import Student
from app.schemas import StudentCreate, StudentUpdate


from typing import Any, Optional, TypeVar
from sqlalchemy.orm import Session
from app.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)

# TODO: check this out
class CRUDStudent(CRUDBase[Student, StudentCreate, StudentUpdate]):
    def get_by_student_code(self, db: Session, code: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.code == code).first()




student = CRUDStudent(Student)
