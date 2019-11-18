import gym
from gym import error, spaces, utils
from gym.utils import seeding
import logging
import numpy
import sys
import random
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

    def reset(self):
        # Set of initialised variables for each agent.
        self.growth_rate = 1
        self.environment = numpy.arange(2500).reshape(50, 50)
        self.environment.fill(0)
        self.agents = 250

        for i in range(50):
            for j in range(50):
                self.environment[i, j] = random.randrange(0, 4)

        return self._next_observation()

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
