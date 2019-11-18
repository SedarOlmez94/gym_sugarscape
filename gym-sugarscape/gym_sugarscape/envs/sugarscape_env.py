import gym
from gym import error, spaces, utils
from gym.utils import seeding
import logging

logger = logging.getLogger(__name__)

class SugarscapeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    ACTIONS = ["N", "E", "S", "W", "EAT"]

    def __init__(self, max_file=None, environment_size=None, enable_render = True):
        super(SugarscapeEnv, self).__init__()
        self.viewer = None
        self.enable_render = enable_render
        self.max_age = (0, 100)
        self.max_metabolic_rate = (1, 4)
        self.s_wealth = (5, 25)
        self.growth_rate = 1
        self.max_vision_distance = (1, 6)

    # Define action and observation space
    # They must be gym.spaces objects
    # Example when using discrete actions:
    self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)#Replace with number of applicable actions
    # Example for using image as input:
    self.observation_space = spaces.Box(low=0, high=255, shape=
        (HEIGHT, WIDTH, N_CHANNELS), dtype=np.uint8)

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
        self._take_action(action)
        self.status = self.env.step()
        reward = self._get_reward()
        ob = self.env.getState()
        episode_over = self.status != hfo_py.IN_GAME
        return ob, reward, episode_over, {}

    def reset(self):
        #Reset the state of the environment to an initial state.
        print("")

    def render(self, mode = 'human'):
        # Render the environment to the screen.
        print("")

    def close(self):
        pass()

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
