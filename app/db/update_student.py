from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app import crud, schemas
from app.utils import read_in_chunks
from app.db import base  # noqa: F401

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def update_student(db: Session) -> None:
    chunk_iter = read_in_chunks("etl/matriculados_pregrado_modified.csv", header=0, sep='*')

    for chunk in chunk_iter:
        for index, row in chunk.iterrows():
            try:
                code = int(row['codigo'])
                m_bajos = True if row['m_bajos'] == 't' else False
                m_tesis = True if row['m_tesis'] == 't' else False
                m_activo = True if row['m_activo'] == 't' else False
                m_grado = True if row['m_grado'] == 't' else False

            except ValueError as error:
                print(
                    "The transaction can't be transformed... skipping",
                    error
                )

            try:
                student = crud.student.get_by_student_code(
                    db,
                    code=code
                )

                print(student)

                if student is not None:
                    update_student = schemas.StudentUpdate(
                        code=code,
                        bajos_rendimientos=m_bajos,
                        m_tesis=m_tesis,
                        m_activo=m_activo,
                        m_grado=m_grado,
                    )

                    crud.student.update(
                        db, db_obj=student, obj_in=update_student
                    )  # noqa: F841

                    print("Student updated", code)

            except Exception as inst:
                print("There was an error updating the student", inst)
                raise
