from sugarscape_env import SugarscapeEnv
from agents import Agent
import math


def test_get_vision():
    agent_1 = Agent(1)
    assert get_vision() >= 1


def test_collect_sugar():
    agent_1 = Agent(1)
    assert agent_1.collect_sugar(4)


def test_reset():
    # 10 Agents, 50 by 50 Environment
    assert reset(10, 50) != reset(20, 55)


def test__get_status():
    environment_test = SugarscapeEnv()
    environment_test.reset(10, 50)

    assert _get_status() == 'SOME AGENTS STILL ALIVE'


import pytest
pytest.main()
