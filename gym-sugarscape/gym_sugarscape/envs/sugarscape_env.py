import gym
from gym import error, spaces, utils
from gym.utils import seeding
import logging
import numpy

logger = logging.getLogger(__name__)

class SugarscapeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    ACTIONS = ["N", "E", "S", "W", "EAT"]

    # Define action and observation space
    # They must be gym.spaces objects
    # Example when using discrete actions:
    action_space = spaces.Discrete(5)#Replace with number of applicable actions
    observation_space = spaces.Discrete(2500)

    def __init__(self):
        super(SugarscapeEnv, self).__init__()
        # Set of initialised variables for each agent.
        self.max_age = (0, 100)
        self.max_metabolic_rate = (1, 4)
        self.s_wealth = (5, 25)
        self.growth_rate = 1
        self.max_vision_distance = (1, 6)

        environment = numpy.arange(
            self.observation_space.n
        ).reshape((50, 50))

        environment[-1, -1] = 0
        self.P = numpy.zeros((self.action_space.n,
                                self.observation_space.n,
                                self.observation_space.n))
        self.P[:, 0, 0] = 1

        print(environment)

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
        #Reset the state of the environment to an initial state.
        print("")

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
