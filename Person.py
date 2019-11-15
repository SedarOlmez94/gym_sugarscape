import gym
from gym import spaces
from gym import envs

class Person:
    def __init__(self, type, ID):
        self.type = type
        self.ID = ID

    def __str__(self):
        return f"Person type {self.type} and ID {self.ID}"


#env = gym.make('CartPole-v0')

# Number of discrete actions that can be applied by the agent, in this case
# it is 2 so 0 and 1 are valid actions.
# print("action space: ", env.action_space)

# the dimensions of the observational space i.e. the size of the environment window.
# print("observation: ", env.observation_space)

# The bounds of the observational space lower and upper bounds.
# print(env.observation_space.high)
# print(env.observation_space.low)


# It is important that any generic environment has a box and discrete which are
# the most common space variables.
#
# space = spaces.Discrete(8)
# x = space.sample()
#
# assert space.contains(x)
# assert space.n == 8

# print(envs.registry.all())
 robberA = Person("Robber", 101)

 print(robberA)
