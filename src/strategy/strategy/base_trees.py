from strategy.behaviour import BlackBoard, Sequence, Selector, TaskStatus
from strategy.actions.state_behaviours import InState, ChangeState
from strategy.actions.game_behaviours import IsBehindBall, IsTheWayFree, IsInsideMetaRange
from strategy.actions.movement_behaviours import *
from strategy.strategy_utils import GameStates, BehavioralStates
from strategy.actions.decorators import UseFrontHead
from utils.linalg import Vec2D
from strategy.acceptance_radius import AcceptanceRadiusEnum

import json

seconds = 3

class Penalty(Sequence):
    def __init__(self, name='Penalty'):
        super().__init__(name)

        check_state = InState('CheckPenaltyState', BehavioralStates.PENALTY)
        self.add_child(check_state)

        check_if_behind_ball = Selector("CheckIfBehindBall")
        is_behind = IsBehindBall("Check", 40)
        change_state = ChangeState("ReturnToNormal", BehavioralStates.NORMAL)

        check_if_behind_ball.add_child(is_behind)
        check_if_behind_ball.add_child(change_state)

        self.add_child(check_if_behind_ball)

        charge_with_ball = ChargeWithBall("ChargeWithFreeWay", 255)

        self.add_child(charge_with_ball)


class FreeBall(Sequence):
    def __init__(self, name='FreeBall'):
        super().__init__(name)

        check_state = InState('CheckFreeBallState', BehavioralStates.FREE_BALL)
        self.add_child(check_state)

        check_if_behind_ball = Selector("CheckIfBehindBall")
        is_behind = IsBehindBall("Check", 30)
        change_state = ChangeState("ReturnToNormal", BehavioralStates.NORMAL)

        check_if_behind_ball.add_child(is_behind)
        check_if_behind_ball.add_child(change_state)

        self.add_child(check_if_behind_ball)
        self.add_child(GoToBallUsingMove2Point(speed=75, acceptance_radius=AcceptanceRadiusEnum.NORMAL.value))
        charge_with_ball = ChargeWithBall("ChargeWithFreeWay", 255)
        self.add_child(charge_with_ball)


class Meta(Sequence):
    def __init__(self, name: str = "Meta"):
        super().__init__(name)

        check_state = InState("CheckMetaState", BehavioralStates.META)
        self.add_child(check_state)

        # meta = Selector("IsInsideMetaRange")
        # in_range_and_behind_the_ball = Sequence("InRangeAndBehindTheBall")
        # is_behind_the_ball = IsBehindBall("BehindTheBall", 40)
        # inside_meta_range = IsInsideMetaRange('MetaDist', 30)
        # in_range_and_behind_the_ball.add_child(is_behind_the_ball)
        # in_range_and_behind_the_ball.add_child(inside_meta_range)
        # meta.add_child(in_range_and_behind_the_ball)

        # change_state = ChangeState("ReturnToNormal", BehavioralStates.NORMAL)
        # meta.add_child(change_state)
        # # TODO: Não usa charge?
        # self.add_child(meta)
        # # charge_with_ball = GoToAttackGoalUsingUnivector("FollowGoal",
        # #                                                 acceptance_radius=5, speed_prediction=False)
        # # charge_with_ball = ChargeWithBall("Charge", 200)
        # # TODO: Verificar acceptance_radius
        # charge_with_ball = GoToBallUsingMove2Point(speed=255, 
        # acceptance_radius=AcceptanceRadiusEnum.SMALL.value)
        # self.add_child(charge_with_ball)
        move_to_position = GoToPositionUsingUnivector(position=None, acceptance_radius=AcceptanceRadiusEnum.DEFAULT.value)
        self.add_child(move_to_position)

    def run(self, blackboard: BlackBoard):
        # log_warn(f'{blackboard.robot.role} --> {self.children[1].position}')
        positions = {   
            "ATTACK":
            [
                {
                    "id": 0,
                    "role": "goalkeeper",
                    "x": -0.7,
                    "y": 0,
                    "orientation": 0
                },
                {
                    "id": 1,
                    "role": "defender",
                    "x": -0.4,
                    "y": 0,
                    "orientation": 0
                },
                {
                    "id": 2,
                    "role": "attacker",
                    "x": -0.25,
                    "y": 0,
                    "orientation": 0
                }

            ],
            "DEFENCE":
            [
                {
                    "id": 0,
                    "role": "goalkeeper",
                    "x": -0.7,
                    "y": 0,
                    "orientation": 0
                },
                {
                    "id": 1,
                    "role": "defender",
                    "x": -0.35,
                    "y": 0,
                    "orientation": 0
                },
                {
                    "id": 2,
                    "role": "attacker",
                    "x": -0.07,
                    "y": -0,
                    "orientation": 0
                }
            ]
        }

        team_side = blackboard.robot.team_color
        team_color = blackboard.robot.team_color
        advantage_team = blackboard.robot.advantage_team

        if team_color == advantage_team:
            advantage = "ATTACK"
        else:
            advantage = "DEFENCE"

        position = positions[advantage][blackboard.robot.role]['x'], positions[advantage][blackboard.robot.role]['y']
        self.children[1].position = Vec2D.from_array(position)
        return super().run(blackboard)
        


class Stopped(Sequence):
    def __init__(self, name: str = 'Stopped'):
        super().__init__(name)

        self.add_child(InState('CheckStoppedState', BehavioralStates.STOPPED))
        self.add_child(UpdateOrientationStopAction('Wait'))


class FreeWayAttack(Sequence):
    def __init__(self, name: str = "FreeWayAttack"):
        super().__init__(name)

        self.add_child(IsBehindBall("CheckIfBehindTheBall", 60))
        # self.add_child(IsTheWayFree("CheckIfTheWayIsFree", 5))
        charge_with_ball = ChargeWithBall("ChargeWithFreeWay", 255)
        self.add_child(charge_with_ball)


class AutomaticPosition(Sequence):
    def __init__(self, name='AutomaticPosition'):
        super().__init__(name)

        check_state = InState('CheckAutomaticPositionState', BehavioralStates.AUTOMATIC_POSITION)
        self.add_child(check_state)

        # sleep = Sleep(seconds)
        # self.add_child(sleep)
        
        move_to_position = GoToPositionUsingUnivector(position=None, 
        acceptance_radius=AcceptanceRadiusEnum.DEFAULT.value)
        # change_state = ChangeState("ReturnToStopped", BehavioralStates.STOPPED)

        self.add_child(move_to_position)
        # self.add_child(change_state)

    def run(self, blackboard: BlackBoard):
        # log_warn(f'{blackboard.robot.role} --> {self.children[1].position}')
        available_positions = list(blackboard.automatic_positions.values())
        position = available_positions[blackboard.current_automatic_position][f'{blackboard.robot.role}']['pos1']
        self.children[1].position = Vec2D.from_array(position)
        return super().run(blackboard)
    
# class Position(Selector):
#     def __init__(self, name: str = "Position"):
#         super().__init__(name)
#         self.add_child(Penalty("Penalty"))
#         self.add_child(FreeBall("FreeBall"))
#         self.add_child(Meta("Meta"))

#     # def run(self):


# alterar o BaseTree antes de testar
class BaseTree(Selector):
    def __init__(self, name: str = "BaseTree"):
        super().__init__(name)
        
        # self.automatic_position = automatic_position

        # self.add_child(AutomaticPosition())
        self.add_child(Stopped("Stopped"))
        self.add_child(Penalty("Penalty"))
        self.add_child(FreeBall("FreeBall"))
        self.add_child(Meta("Meta"))