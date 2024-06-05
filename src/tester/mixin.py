import json
from models import Team, Scenario, Result
from config import Session
import uuid

class ConsumerMixin:
    def callback(self, body):
        message = json.loads(body)
        id = message["team_id"]
        id = uuid.UUID(id) 
        team = Session.query(Team).filter_by(id=id).first()
        scenarios = Session.query(Scenario).all()
        for scenario in scenarios:
            result = self.__test(team=team, scenario=scenario)
            Session.add(result)
        Session.commit()

    def __test(self, team:Team, scenario:Scenario )-> Result:
        print(f"TEST {team}, with {scenario}")
        print(scenario.steps)
        print("NOT IMPLEMENTED")
        r = Result()
        r.scenario_id = scenario.id
        r.score = 100
        r.team_id = team.id
        r.average_time = 12
        r.status = Result.StatusEnum.P
        return r