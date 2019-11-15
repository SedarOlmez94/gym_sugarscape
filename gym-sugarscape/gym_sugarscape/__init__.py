from gym.envs.registration import register

register(
    id='sugarscape-v0',
    entry_point='gym_sugarscape.envs:SugarscapeEnv',
)
register(
    id='sugarscape-extrahard-v0',
    entry_point='gym_sugarscape.envs:SugarscapeExtraHardEnv',
)
