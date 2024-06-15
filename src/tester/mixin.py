import json
from models import Team, Scenario, Result
from models.step_handlers import Handler
from config import Session
import uuid
import logging

logger = logging.getLogger(__name__)

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
        logger.info(f"TEST {team}, with {scenario}")
        steps = scenario.steps
        k = 0 
        time = 0
        for step in steps:
            try:
                handler = Handler(step)
                valid, step_time = handler.run()
                if not valid:
                    break
                k += 1
                time += step_time
            except Exception as e:
                #FIXME: Log the exception and then break
                raise e
        r = Result()
        r.scenario_id = scenario.id
        r.team_id = team.id
        r.score = (100* k)/steps.__len__()
        r.average_time = time/k if k !=0 else 1000000
        r.status = Result.StatusEnum.P if k == steps.__len__() else Result.StatusEnum.F
        return r
