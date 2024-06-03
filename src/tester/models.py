from sqlalchemy.orm import (
    Mapped,
    MappedColumn,
)
from config import Base

class Scenario(Base):
    __tablename__ ='scenarios'
    id: Mapped[int] = MappedColumn(primary_key=True)
    name: Mapped[str] = MappedColumn()
    weight: Mapped[int] = MappedColumn()

    def __repr__(self):
        return f"<Scenario(id={self.id}, name={self.name}, weight={self.weight})>"
    