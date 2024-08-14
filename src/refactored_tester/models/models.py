import enum
from typing import NewType
from uuid import UUID as PYTHON_UUID

from sqlalchemy import types as t
from sqlalchemy.orm import (
    Mapped,
    DeclarativeBase,
    MappedAsDataclass,
)
from sqlalchemy.schema import (
    PrimaryKeyConstraint, 
    ForeignKeyConstraint, 
    UniqueConstraint
    )

UUID_FIELD = NewType("UUID_FIELD", PYTHON_UUID)
JSON_FIELD = NewType("JSON_FIELD", dict)

class Base(
    DeclarativeBase,
    MappedAsDataclass,
):
    type_annotation_map = {
        UUID_FIELD: t.UUID,
        JSON_FIELD: t.JSON,
    }


class Scenario(Base):
    __tablename__ = "scenarios"
    __table_args__ = (
        PrimaryKeyConstraint("id"),
        )
    id: Mapped[int]
    name: Mapped[str]
    weight: Mapped[int]

    def __repr__(self):
        return f"<Scenario(id={self.id}, name={self.name}, weight={self.weight})>"



class ScenarioStep(Base):
    class TypeEnum(enum.Enum):
        M_R = "Memory Read"
        M_W = "Memory Write"
        R_R = "Register Read"
        R_W = "Register Write"
        C_C = "Cpu Compile"
        C_E = "Cpu Execute"

    __tablename__ = "scenario_steps"
    __table_args__ = (
        PrimaryKeyConstraint("id"),
        ForeignKeyConstraint(["scenario_id"], ["scenarios.id"], ondelete="CASCADE"),
        UniqueConstraint("step")
    )
    
    id: Mapped[int]
    name: Mapped[str]
    step: Mapped[str]
    type: Mapped[TypeEnum]
    input: Mapped[JSON_FIELD]
    output: Mapped[JSON_FIELD]
    scenario_id: Mapped[int]

    def __repr__(self):
        return f"<ScenarioStep:{self.name}>"


class Team(Base):
    __tablename__ = "teams"
    __table_args__ = (
        PrimaryKeyConstraint("id"),
    )

    id: Mapped[UUID_FIELD]
    name: Mapped[str]
    members: Mapped[JSON_FIELD]

    def __repr__(self):
        return f"<Team(id={self.id}, name={self.name})>"
