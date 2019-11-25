from sugarscape_env import SugarscapeEnv
from agents import Agent
import math

import pytest
pytest.main()


def test_get_vision():
    agent_1 = Agent(1)
    assert agent_1.get_vision() >= 1


def test__get_status():
    environment_test = SugarscapeEnv()
    environment_test.reset(10, 50)
    environment_test.step('N')

    assert environment_test._get_status() == 'SOME AGENTS STILL ALIVE'
