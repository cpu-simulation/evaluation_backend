from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa
from .models import Scenario, Team, ScenarioStep


class DataBaseInterface:
    @staticmethod
    def find_team_by_id(Session:sessionmaker, team_id) -> Team|None:
        with Session.begin() as session:
            query = sa.select(Team).where(Team.id==team_id)
            team = session.scalars(query).first()
            if not team:
                raise Exception("team not found")
            
            session.expunge(team)
            
        return team
            

    @staticmethod
    def find_scenarios(Session: sessionmaker) -> list[Scenario]:
        with Session.begin() as session:
            query = sa.select(Scenario)
            scenarios = session.scalars(query).all()
            session.expunge_all()
            scenarios = list(scenarios)
        return scenarios

    @staticmethod
    def find_scenario_steps(Session:sessionmaker ,scenario_id):
        with Session.begin() as session:
            query = sa.select(ScenarioStep).where(ScenarioStep.scenario_id==scenario_id).order_by(ScenarioStep.step)
            scenario_steps = list(session.scalars(query).all())
            session.expunge_all()
        return scenario_steps