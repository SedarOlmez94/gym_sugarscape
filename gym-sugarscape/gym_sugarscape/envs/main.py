from sugarscape_env import SugarscapeEnv
import random
from IPython.display import clear_output
import numpy as np



# alpha = 0.1
# gamma = 0.6
# epsilon = 0.1
#
# all_epochs = []
# all_penalties = []
ACTIONS = ['N', 'E', 'S', 'W']


"""
Example scenario run of model
"""
x = SugarscapeEnv()
x.reset(10, 50)
#x = SugarscapeEnv()
#x.reset(10, 50) # 50 by 50 grid and 10 agents.
# q_table = np.zeros([x.observation_space.n, x.action_space.n])
#
# # For plotting metrics
# all_epochs = []
# all_penalties = []


# for j in range(1, 1000):
#
#     x.reset(10, 50) # 50 by 50 grid and 10 agents.
#     state = x.get_state()
#
#     epochs, penalties, reward, = 0, 0, 0
#     done = False
#
#     for i in range(100):
#         if random.uniform(0, 1) < epsilon:
#             action = random.randrange(4)
#         else:
#             action = np.argmax(q_table[state])
#
#
#         next_state, reward, done, info = x.step(ACTIONS[action])
#         old_value = q_table[state, action]
#         next_max = np.max(q_table[next_state])
#
#         new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
#         q_table[state, action] = new_value
#
#         if reward == -1:
#             penalties += 1
#
#         state = next_state
#         epochs += 1
#
#
# print("Training finished.\n")
# print(q_table)
#print(x._get_P())
for i in range(10000):
    random_move = random.randrange(4)
    print(x.step(ACTIONS[random_move]))

print(x.render())
print(x._get_P())
