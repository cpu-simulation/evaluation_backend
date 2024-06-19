import json
from core.exceptions import MyBaseException
from models import Team, Scenario, Result
from .step_handlers import Handler
from config import Session
import uuid
import logging

logger = logging.getLogger(__name__)

class ConsumerMixin:
    def callback(self, body):

        try:
            message = json.loads(body)
            team = self.find_team(id=message["team_id"])
            scenarios = Session.query(Scenario).all()
            results: list[Result] = []

            for scenario in scenarios:
                result = self.__test(
                    team=team,
                    scenario=scenario
                    )
                results.append(result)

            score = self.calculate_score_by_results(results)
            self.insert_to_influx(team, score)
            self.insert_to_mysql(results=results)

        except Exception as e:
            return e

    def calculate_score_by_results(self, results):
        score = 0
        for r in results: score+=r.score
        return score

    def insert_to_influx(self, team, score):
        ... # TODO

    def insert_to_mysql(self, results):
        logger.info("commit results of team to mysql")
        Session.add_all(results)
        Session.commit()

    def find_team(self, id) -> Team:
        logger.info(f"query mysql for team with id={id}")
        id = uuid.UUID(id)
        team = Session.query(Team).filter_by(id=id).first()
        return team

    def __test(self,
               team:Team,
               scenario:Scenario
               )-> Result:
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
            
            except MyBaseException as e:
                
                logger.log(
                    e.level,
                    "A base exception raised while running a step. error=%s",
                    e.msg
                    )
                break

            except Exception as e:
                logger.error(
                    f"failed to run an step test with as step={step.__str__()}, e={e}"
                    )
                    
                raise e

        r = Result()
        r.scenario_id = scenario.id
        r.team_id = team.id
        r.score = (100* k)/steps.__len__()
        r.average_time = time/k if k !=0 else 1000000
        r.status = Result.StatusEnum.P\
            if k == steps.__len__() \
            else Result.StatusEnum.F
        return r
