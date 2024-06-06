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
        steps = scenario.steps
        k = 0 
        time = 0
        for step in steps:
            step.add_eng()
            try:
                t = step.apply()
                k += 1
                time += t
            except:
                break
        r = Result()
        r.scenario_id = scenario.id
        r.team_id = team.id
        r.score = (100* k)/steps.__len__()
        r.average_time = time/k if k !=0 else 1000000
        r.status = Result.StatusEnum.P if k == steps.__len__() else Result.StatusEnum.F
        return r