import gym
from gym import error, spaces, utils
from gym.utils import seeding
import logging
#https://towardsdatascience.com/creating-a-custom-openai-gym-environment-for-stock-trading-be532be3910e
logger = logging.getLogger(__name__)

class SugarscapeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(SugarscapeEnv, self).__init__()
    # Define action and observation space
    # They must be gym.spaces objects
    # Example when using discrete actions:
    self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)#Replace with number of applicable actions
    # Example for using image as input:
    self.observation_space = spaces.Box(low=0, high=255, shape=
        (HEIGHT, WIDTH, N_CHANNELS), dtype=np.uint8)

    def step(self, action):
        #Execute one time step within the environment
        print("")

    def reset(self):
        #Reset the state of the environment to an initial state.
        print("")

    def render(self, mode = 'human'):
        # Render the environment to the screen.
        print("")

    def close(self):
        pass()
