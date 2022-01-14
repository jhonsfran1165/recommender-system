from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.db.mixin_class import CommonColumnsMixin


# TODO: map transactions table with matriculados information
class Student(Base, CommonColumnsMixin):
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    first_name = Column(
        String,
        doc="Name of the student",
        comment="Name of the student"
    )

    last_name = Column(
        String,
        doc="Last name of the student",
        comment="Last name of the student"
    )

    program = Column(
        Integer,
        index=True,
        doc="Program",
        comment="Program"
    )

    sede = Column(
        Integer,
        index=True,
        doc="Sede",
        comment="Sede"
    )

    jornada = Column(
        String,
        doc="Jornada",
        comment="Jornada"
    )

    type_doc = Column(
        String,
        doc="type_doc",
        comment="type_doc"
    )

    document = Column(
        Integer,
        doc="Document",
        comment="Document"
    )

    bajos_rendimientos = Column(
        Boolean,
        doc="bajos_rendimientos",
        comment="bajos_rendimientos"
    )

    per_matriculados = Column(
        Integer,
        doc="per_matriculados",
        comment="per_matriculados"
    )

    per_cancelados = Column(
        Integer,
        doc="per_cancelados",
        comment="per_cancelados"
    )

    m_tesis = Column(
        Boolean,
        doc="m_tesis",
        comment="m_tesis"
    )

    m_activo = Column(
        Boolean,
        doc="m_activo",
        comment="m_activo"
    )

    m_periodo_activo = Column(
        String,
        doc="m_periodo_activo",
        comment="m_periodo_activo"
    )

    m_grado = Column(
        Boolean,
        doc="m_grado",
        comment="m_grado"
    )

    sexo = Column(
        String,
        doc="sexo",
        comment="sexo"
    )

    birth_date = Column(
        String,
        doc="Fecha_nacimiento",
        comment="Fecha_nacimiento"
    )

    estrato = Column(
        Integer,
        doc="estrato",
        comment="estrato"
    )

    def __str__(self):
        return self.id
