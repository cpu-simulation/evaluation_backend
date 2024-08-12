import enum

from sqlalchemy import JSON, Enum
from sqlalchemy.orm import (
    Mapped,
    DeclarativeBase,
    MappedAsDataclass,
)
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint


class Base(
    DeclarativeBase,
    MappedAsDataclass,
):
    pass


class Scenario(Base):
    __tablename__ = "scenarios"
    __table_args__ = (
        PrimaryKeyConstraint(),
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
        PrimaryKeyConstraint(),
        ForeignKeyConstraint()
    )
    
    id: Mapped[int]
    name: Mapped[str]
    type: Mapped[Enum[TypeEnum]]
    input: Mapped[JSON]
    output: Mapped[JSON]
    scenario_id: Mapped[int]

    def __repr__(self):
        return f"<ScenarioStep:{self.name}>"

