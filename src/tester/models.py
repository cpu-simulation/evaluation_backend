from sqlalchemy.orm import Mapped, MappedColumn, relationship
from typing import List
from sqlalchemy.sql import func
from sqlalchemy import types, Enum, JSON, DateTime, Column
from sqlalchemy import ForeignKey
import uuid, enum
from config import Base


class Scenario(Base):
    __tablename__ = "scenarios"
    id: Mapped[int] = MappedColumn(primary_key=True)
    name: Mapped[str] = MappedColumn()
    weight: Mapped[int] = MappedColumn()
    results: Mapped[List["Result"]] = relationship()
    steps: Mapped[List["ScenarioStep"]] = relationship()

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
    id: Mapped[int] = MappedColumn(primary_key=True)
    scenario_id: Mapped[int] = MappedColumn(ForeignKey("scenarios.id"))
    scenario: Mapped["Scenario"] = relationship(back_populates="steps")
    name: Mapped[str] = MappedColumn()
    type: Mapped[Enum] = MappedColumn(Enum(TypeEnum))
    input: Mapped[JSON] = MappedColumn(type_=JSON)
    output: Mapped[JSON] = MappedColumn(type_=JSON)

    def __repr__(self):
        return f"<ScenarioStep:{self.name}>"


class Team(Base):
    __tablename__ = "teams"

    id: Mapped[uuid.UUID] = MappedColumn(
        "team_id",
        types.Uuid,
        primary_key=True,
    )
    name: Mapped[str] = MappedColumn()
    members: Mapped[JSON] = MappedColumn(type_=JSON)
    results: Mapped[List["Result"]] = relationship(back_populates="team")

    def __repr__(self):
        return f"<Team(id={self.id}, name={self.name})>"


class Result(Base):
    class StatusEnum(enum.Enum):
        W = "W"
        F = "F"
        P = "P"

    __tablename__ = "results"

    id: Mapped[uuid.UUID] = MappedColumn(
        "result_id", types.Uuid, primary_key=True, default=uuid.uuid4
    )
    team_id: Mapped[uuid.UUID] = MappedColumn(ForeignKey("teams.team_id"))
    team: Mapped["Team"] = relationship(back_populates="results")
    scenario_id: Mapped[int] = MappedColumn(ForeignKey("scenarios.id"))
    status: Mapped[Enum] = MappedColumn(Enum(StatusEnum))
    average_time: Mapped[int] = MappedColumn()
    score: Mapped[int] = MappedColumn()
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )

    def __repr__(self) -> str:
        return f"<Result team={self.team.name}, scenario={self.scenario_id}, score={self.score}>"
