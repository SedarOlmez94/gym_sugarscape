from sugarscape_env import SugarscapeEnv
"""
Example scenario run of model
"""
x = SugarscapeEnv()
x._reset(10, 50) # 50 by 50 grid and 10 agents.
print(x._step('N'))
