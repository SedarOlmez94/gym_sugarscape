import gym
from gym import error, spaces, utils
from gym.utils import seeding
import logging
import numpy
import sys
import random
from agents import Agent

numpy.set_printoptions(threshold=sys.maxsize)
logger = logging.getLogger(__name__)

class SugarscapeEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    ACTIONS = ["N", "E", "S", "W", "EAT"]
    random.seed(9001)

    # Define action and observation space
    # They must be gym.spaces objects
    # Example when using discrete actions:


    def __init__(self):
        super(SugarscapeEnv, self).__init__()
        self.action_space = spaces.Discrete(5) #Replace with number of applicable actions
        self.observation_space = spaces.Discrete(2500)


    def step(self, action):
        #Execute one time step within the environment
        """
        Parameters
        ----------
        action :

        Returns
        -------
        ob, reward, episode_over, info : tuple
            ob (object) :
                an environment-specific object representing your observation of
                the environment.
            reward (float) :
                amount of reward achieved by the previous action. The scale
                varies between environments, but the goal is always to increase
                your total reward.
            episode_over (bool) :
                whether it's time to reset the environment again. Most (but not
                all) tasks are divided up into well-defined episodes, and done
                being True indicates the episode has terminated. (For example,
                perhaps the pole tipped too far, or you lost your last life.)
            info (dict) :
                 diagnostic information useful for debugging. It can sometimes
                 be useful for learning (for example, it might contain the raw
                 probabilities behind the environment's last state change).
                 However, official evaluations of your agent are not allowed to
                 use this for learning.
        """
        print("")


    def _step(self, action):
        # agent takes an action
        self._take_action(action)

        self.status = self.env.step()
        reward = self._get_reward()
        ob = self.env.getState()
        episode_over = self.status != hfo_py.IN_GAME
        return ob, reward, episode_over, {}

    def _take_action(self, action):
        """ Converts the action space into an HFO action. """

        for i in

        # action_type = ACTION_LOOKUP[action[0]]
        # if action_type == hfo_py.DASH:
        #     self.env.act(action_type, action[1], action[2])
        # elif action_type == hfo_py.TURN:
        #     self.env.act(action_type, action[3])
        # elif action_type == hfo_py.KICK:
        #     self.env.act(action_type, action[4], action[5])
        # else:
        #     print('Unrecognized action %d' % action_type)
        #     self.env.act(hfo_py.NOOP)

    def _get_reward(self):
        """ Reward is given for scoring a goal. """
        if self.status == hfo_py.GOAL:
            return 1
        else:
            return 0

    def reset(self):
        # Set of initialised variables for each agent.
        self.growth_rate = 1
        self.environment = numpy.empty((50,50), dtype=numpy.object)
        #self.environment.fill(0)
        list_of_agents = []
        number_of_agents = 0
        test_loop = 0

        # Creating 250 agent objects and putting them into the list_of_agents array.
        for i in range(250):
            list_of_agents.append(Agent(i))

        # Looping though the environment and adding random values between 0 and 4
        # This will be sugar levels.
        for i in range(50):
            for j in range(50):
                self.environment[i, j] = random.randrange(0, 4)

        # Looping 250 times over the environment and randomly placing agents on 0 sugar cells.
        while(number_of_agents != 250):
            x = random.randrange(50)
            y = random.randrange(50)
            if(self.environment[x, y] == 0):
                self.environment[x, y] = list_of_agents[number_of_agents].get_visual()
                number_of_agents = number_of_agents + 1


        print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in self.environment]))


    def render(self, mode = 'human'):
        # Render the environment to the screen.
        print("")

    def close(self):
        print("")

    def _get_reward(self):
        """
        Get a reward for XY.
        """
        if self.status == something:
            return 1
        elif self.status == ABC:
            return self.somestate ** 2
        else:
            return 0

x = SugarscapeEnv()
x.reset()
