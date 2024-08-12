from sqlalchemy.orm import (
    Mapped,
    DeclarativeBase,
    MappedAsDataclass,
)
from sqlalchemy.schema import PrimaryKeyConstraint


class Base(
    DeclarativeBase,
    MappedAsDataclass,
):
    pass


class Scenario(Base):
    __tablename__ = "scenarios"
    __table_args__ = PrimaryKeyConstraint(name=id)
    name: Mapped[str]
    weight: Mapped[int]
    id: Mapped[int]

    def __repr__(self):
        return f"<Scenario(id={self.id}, name={self.name}, weight={self.weight})>"
