from sqlalchemy.orm import Session
import sqlalchemy as sa
from .models import Scenario, Team


class DataBaseInterface:
    @staticmethod
    def find_team_by_id(session:Session, team_id) -> Team|None:
        with session.begin():
            query = sa.select(Team).where(Team.id==team_id)
            team = session.scalars(query).first()
            session.expunge(team)
        return team

    @staticmethod
    def find_scenarios(session: Session) -> list:
        ...   
    