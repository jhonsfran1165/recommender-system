from datetime import datetime

from sqlalchemy.orm import Session

from app import crud, schemas
from app.utils import read_in_chunks
from app.db import base  # noqa: F401

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def load_student(db: Session) -> None:
    chunk_iter = read_in_chunks("etl/matriculados_pregrado_modified.csv", header=0, sep='*')

    for chunk in chunk_iter:
        for index, row in chunk.iterrows():
            try:
                m_bajos = True if row['m_bajos'] == 't' else False
                m_tesis = True if row['m_tesis'] == 't' else False
                m_activo = True if row['m_activo'] == 't' else False
                m_grado = True if row['m_grado'] == 't' else False

                code = int(row['codigo'])
                nombre = row['nombre']
                apellidos = row['apellidos']
                programa = int(row['programa'])
                sede = int(row['sede'])
                jornada = row['jornada']
                tipo_doc = row['tipo_doc']
                doc = row['doc']
                per_matriculados = int(row['per_matriculados'])
                per_cancelados = int(row['per_cancelados'])
                m_periodo_activo = row['m_periodo_activo']
                sexo = row['sexo']
                fecha_nacimiento = row['Fecha_nacimiento']
                estrato = int(row['Estrato'])

            except ValueError as error:
                print("The transaction can't be transformed... skipping", error)

            try:
                student_in = schemas.StudentCreate(
                    code=code,
                    first_name=nombre,
                    last_name=apellidos,
                    program=programa,
                    sede=sede,
                    jornada=jornada,
                    type_doc=tipo_doc,
                    document=doc,
                    bajos_rendimientos=m_bajos,
                    per_matriculados=per_matriculados,
                    per_cancelados=per_cancelados,
                    m_tesis=m_tesis,
                    m_activo=m_activo,
                    m_periodo_activo=m_periodo_activo,
                    m_grado=m_grado,
                    sexo=sexo,
                    birth_date=fecha_nacimiento,
                    estrato=estrato
                )

                student_in_db = crud.student.create(db, obj_in=student_in)  # noqa: F841

                print("Student added", code)

            except Exception as inst:
                print("There was an error inserting the student", inst)
                raise
