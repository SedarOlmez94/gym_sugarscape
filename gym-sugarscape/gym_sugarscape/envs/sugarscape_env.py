import gym
from gym import error, spaces, utils
from gym.utils import seeding
import logging
import numpy
import sys
import random
from contextlib import closing
from six import StringIO
from gym.envs.toy_text import discrete
from agents import Agent


numpy.set_printoptions(threshold=sys.maxsize)
logger = logging.getLogger(__name__)
ACTIONS = ["STATIONARY", "N", "E", "S", "W", "EAT"]
list_of_agents = []
list_of_agents_shuffled = {}
number_of_agents = 0



class SugarscapeEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    random.seed(9001)
    # Define action and observation space
    # They must be gym.spaces objects
    # Example when using discrete actions:


    def __init__(self):
        super(SugarscapeEnv, self).__init__()
        self.action_space = spaces.Discrete(5) #Replace with number of applicable actions
        self.observation_space = spaces.Discrete(2601)
        self.current_step = 0


    def _step(self, action):
        # Execute one time step within the environment
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
        self.current_step += 1
        self._agents_die(10) # Have any agents died? If so replace the dead ones with new ones.
        self.status = self._get_status() # Are all agents still alive or have they all died?
        reward = self._get_reward() # Have all agents been able to get some sugar?
        ob = self._get_state() # what is the current state of the environment
        episode_over = self.status == 'ALL AGENTS DEAD'
        return ob, reward, episode_over, {}


    def _take_action(self, action):
        """ One action is performed """
        global list_of_agents, ACTIONS, list_of_agents_shuffled, number_of_agents
        agents_iteration = 0

        #while (number_of_agents != 10): #CHANGE TO 250
        for x in range(51):
            for y in range(51):
                #while number_of_agents in range(10):
                # FOR EACH CELL, CHECK IF AN AGENT OUT OF THE 250 IS STANDING IN THAT CELL.
                if agents_iteration < 10:

                    if(self.environment[x, y] == 'X' and list_of_agents_shuffled[agents_iteration].get_ID() == agents_iteration):
                        #print(f"agend ID: {list_of_agents_shuffled[agents_iteration].get_ID()} and iteration {agents_iteration}")
                        random_action = random.randrange(1, 4)
                        #current_cell_sugar = self.environment[x, y]

                        # Once the agent has been identified in the environment we set the applicable moves and vision variables
                        vision_of_agent = list_of_agents_shuffled[agents_iteration].get_vision()
                        move_south = self.environment[(x - vision_of_agent) % 51, y]
                        move_north = self.environment[(x + vision_of_agent) % 51, y]
                        move_east = self.environment[x, (y + vision_of_agent) % 51]
                        move_west = self.environment[x, (y - vision_of_agent) % 51]

                        # If moving south, north, east or west means coming into contact with another agent
                        # Set that locations sugar to 0
                        if(isinstance(self.environment[(x - vision_of_agent) % 51, y], str)):
                            move_south = int(0)
                        if(isinstance(self.environment[(x + vision_of_agent) % 51, y], str)):
                            move_north = int(0)
                        if(isinstance(self.environment[x, (y + vision_of_agent) % 51], str)):
                            move_east = int(0)
                        if(isinstance(self.environment[x, (y - vision_of_agent) % 51], str)):
                            move_west = int(0)

                        #print(move_north, move_east, move_south, move_west)


                        # MOVE UP (N)
                        if(action == ACTIONS[1]):
                            if((move_north >= move_south) and
                                (move_north >= move_east) and
                                (move_north >= move_west)):
                                print(f"{ACTIONS[1]}, {ACTIONS[5]} by agent: {list_of_agents_shuffled[agents_iteration].get_ID()}")
                                # AGENT COLLECTS SUGAR.
                                list_of_agents_shuffled[agents_iteration].collect_sugar(move_north)
                                # CALCULATE AGENT SUGAR HEALTH
                                list_of_agents_shuffled[agents_iteration].calculate_s_wealth()
                                # SUGAR AT LOCATION NOW SET TO 0
                                self.environment[(x + vision_of_agent) % 51, y] = 0
                                self.environment_duplicate[(x + vision_of_agent) % 51, y] = 0
                                #MOVE AGENT TO NEW LOCATION.
                                self.environment[(x + vision_of_agent) % 51, y] = list_of_agents_shuffled[agents_iteration].get_visual()
                                self.environment_duplicate[(x + vision_of_agent) % 51, y] = list_of_agents_shuffled[agents_iteration]
                                # SET PREVIOUS POSITION CELL TO 0 sugar
                                self.environment[x, y] = 0
                                self.environment_duplicate[x, y] = 0
                                # ADD ACTIONS TO ENV ACT

                            else:
                                self._random_move(agents_iteration, move_south, move_east, move_north, move_west, x, y, vision_of_agent)


                        # MOVE DOWN (S)
                        if(action == ACTIONS[3]):
                            if((move_south >= move_north) and
                                (move_south >= move_east) and
                                (move_south >= move_west)):
                                print(f"{ACTIONS[3]}, {ACTIONS[5]} by agent: {list_of_agents_shuffled[agents_iteration].get_ID()}")
                                # AGENT COLLECTS SUGAR.
                                list_of_agents_shuffled[agents_iteration].collect_sugar(move_south)
                                # CALCULATE AGENT SUGAR HEALTH
                                list_of_agents_shuffled[agents_iteration].calculate_s_wealth()
                                # SUGAR AT LOCATION NOW SET TO 0
                                self.environment[(x - vision_of_agent) % 51, y] = 0
                                self.environment_duplicate[(x - vision_of_agent) % 51, y] = 0
                                #MOVE AGENT TO NEW LOCATION.
                                self.environment[(x - vision_of_agent) % 51, y] = list_of_agents_shuffled[agents_iteration].get_visual()
                                self.environment_duplicate[(x - vision_of_agent) % 51, y] = list_of_agents_shuffled[agents_iteration]
                                # SET PREVIOUS POSITION CELL TO 0 sugar
                                self.environment[x, y] = 0
                                self.environment_duplicate[x, y] = 0
                                # ADD ACTIONS TO ENV ACT

                            else:
                                self._random_move(agents_iteration, move_south, move_east, move_north, move_west, x, y, vision_of_agent)


                        # MOVE LEFT (W)
                        if(action == ACTIONS[4]):
                            if((move_west >= move_south) and
                                (move_west >= move_east) and
                                (move_west >= move_north)):
                                print(f"{ACTIONS[4]}, {ACTIONS[5]} by agent: {list_of_agents_shuffled[agents_iteration].get_ID()}")
                                # AGENT COLLECTS SUGAR.
                                list_of_agents_shuffled[agents_iteration].collect_sugar(move_west)
                                # CALCULATE AGENT SUGAR HEALTH
                                list_of_agents_shuffled[agents_iteration].calculate_s_wealth()
                                # SUGAR AT LOCATION NOW SET TO 0
                                self.environment[x, (y - vision_of_agent) % 51] = 0
                                self.environment_duplicate[x, (y - vision_of_agent) % 51] = 0
                                #MOVE AGENT TO NEW LOCATION.
                                self.environment[x, (y - vision_of_agent) % 51] = list_of_agents_shuffled[agents_iteration].get_visual()
                                self.environment_duplicate[x, (y - vision_of_agent) % 51] = list_of_agents_shuffled[agents_iteration]
                                # SET PREVIOUS POSITION CELL TO 0 sugar
                                self.environment[x, y] = 0
                                self.environment_duplicate[x, y] = 0
                                # ADD ACTIONS TO ENV ACT

                            else:
                                self._random_move(agents_iteration, move_south, move_east, move_north, move_west, x, y, vision_of_agent)


                        # MOVE RIGHT (E)
                        if(action == ACTIONS[2]):
                            if((move_east >= move_south) or
                                (move_east >= move_west) or
                                (move_east >= move_north)):
                                print(f"{ACTIONS[2]}, {ACTIONS[5]} by agent: {list_of_agents_shuffled[agents_iteration].get_ID()}")
                                # AGENT COLLECTS SUGAR.
                                list_of_agents_shuffled[agents_iteration].collect_sugar(move_east)
                                # CALCULATE AGENT SUGAR HEALTH
                                list_of_agents_shuffled[agents_iteration].calculate_s_wealth()
                                # SUGAR AT LOCATION NOW SET TO 0
                                self.environment[x, (y + vision_of_agent) % 51] = 0
                                self.environment_duplicate[x, (y + vision_of_agent) % 51] = 0
                                #MOVE AGENT TO NEW LOCATION.
                                self.environment[x, (y + vision_of_agent) % 51] = list_of_agents_shuffled[agents_iteration].get_visual()
                                self.environment_duplicate[x, (y + vision_of_agent) % 51] = list_of_agents_shuffled[agents_iteration]
                                # SET PREVIOUS POSITION CELL TO 0 sugar
                                self.environment[x, y] = 0
                                self.environment_duplicate[x, y] = 0
                                # ADD ACTIONS TO ENV ACT

                            else:
                                self._random_move(agents_iteration, move_south, move_east, move_north, move_west, x, y, vision_of_agent)

                        agents_iteration = agents_iteration + 1


    def _random_move(self, agents_iteration, move_south, move_east, move_north, move_west, x, y, vision_of_agent):
        global list_of_agents, ACTIONS, list_of_agents_shuffled, number_of_agents
        random_move = random.randrange(1, 4)


        if random_move == 1:
            print(f"{ACTIONS[1]}, {ACTIONS[5]} by agent: {list_of_agents_shuffled[agents_iteration].get_ID()}")
            list_of_agents_shuffled[agents_iteration].collect_sugar(move_north)
            list_of_agents_shuffled[agents_iteration].calculate_s_wealth()
            self.environment[(x + vision_of_agent) % 51, y] = 0
            self.environment_duplicate[(x + vision_of_agent) % 51, y] = 0
            self.environment[(x + vision_of_agent) % 51, y] = list_of_agents_shuffled[agents_iteration].get_visual()
            self.environment_duplicate[(x + vision_of_agent) % 51, y] = list_of_agents_shuffled[agents_iteration]
            self.environment[x, y] = 0
            self.environment_duplicate[x, y] = 0


        elif random_move == 2:
            print(f"{ACTIONS[2]}, {ACTIONS[5]} by agent: {list_of_agents_shuffled[agents_iteration].get_ID()}")
            list_of_agents_shuffled[agents_iteration].collect_sugar(move_east)
            list_of_agents_shuffled[agents_iteration].calculate_s_wealth()
            self.environment[x, (y + vision_of_agent) % 51] = 0
            self.environment_duplicate[x, (y + vision_of_agent) % 51] = 0
            self.environment[x, (y + vision_of_agent) % 51] = list_of_agents_shuffled[agents_iteration].get_visual()
            self.environment_duplicate[x, (y + vision_of_agent) % 51] = list_of_agents_shuffled[agents_iteration]
            self.environment[x, y] = 0
            self.environment_duplicate[x, y] = 0


        elif random_move == 3:
            print(f"{ACTIONS[3]}, {ACTIONS[5]} by agent: {list_of_agents_shuffled[agents_iteration].get_ID()}")
            list_of_agents_shuffled[agents_iteration].collect_sugar(move_south)
            list_of_agents_shuffled[agents_iteration].calculate_s_wealth()
            self.environment[(x - vision_of_agent) % 51, y] = 0
            self.environment_duplicate[(x - vision_of_agent) % 51, y] = 0
            self.environment[(x - vision_of_agent) % 51, y] = list_of_agents_shuffled[agents_iteration].get_visual()
            self.environment_duplicate[(x - vision_of_agent) % 51, y] = list_of_agents_shuffled[agents_iteration]
            self.environment[x, y] = 0
            self.environment_duplicate[x, y] = 0


        else:
            print(f"{ACTIONS[4]}, {ACTIONS[5]} by agent: {list_of_agents_shuffled[agents_iteration].get_ID()}")
            list_of_agents_shuffled[agents_iteration].collect_sugar(move_west)
            list_of_agents_shuffled[agents_iteration].calculate_s_wealth()
            self.environment[x, (y - vision_of_agent) % 51] = 0
            self.environment_duplicate[x, (y - vision_of_agent) % 51] = 0
            self.environment[x, (y - vision_of_agent) % 51] = list_of_agents_shuffled[agents_iteration].get_visual()
            self.environment_duplicate[x, (y - vision_of_agent) % 51] = list_of_agents_shuffled[agents_iteration]
            self.environment[x, y] = 0
            self.environment_duplicate[x, y] = 0


    def _get_reward(self):
        """
        If all agents have positive s_wealth then reward 1 else 0
        therefore, the Q-learning algorithm will try learn how each agent can
        move to have positive s_wealth each iteration.
        """
        global number_of_agents

        while(number_of_agents != 10):

            if (list_of_agents_shuffled[number_of_agents].get_s_wealth() > 0):
                return 1
            else:
                return 0

            number_of_agents = number_of_agents + 1


    def _reset(self):
        # Reset the state of the environment to an initial state
        self.growth_rate = 1
        self.environment = numpy.empty((51,51), dtype=numpy.object)
        self.environment_duplicate = numpy.empty((51,51), dtype=numpy.object)

        #self.environment.fill(0)
        number_of_agents = 0
        test_loop = 0
        global list_of_agents
        global list_of_agents_shuffled


        # Creating 250 agent objects and putting them into the list_of_agents array.
        for i in range(10): #CHANGE TO 250
            list_of_agents.append(Agent(i))


        # Looping though the environment and adding random values between 0 and 4
        # This will be sugar levels.
        for i in range(51):
            for j in range(51):
                self.environment[i, j] = random.randrange(0, 4)


        # Looping 250 times over the environment and randomly placing agents on 0 sugar cells.
        while(number_of_agents != 10): #CHANGE TO 250
            x = random.randrange(51)
            y = random.randrange(51)
            if(self.environment[x, y] == 0):
                self.environment[x, y] = list_of_agents[number_of_agents].get_visual()
                self.environment_duplicate[x, y] = list_of_agents[number_of_agents]
                # Added the agent objects have been placed down randomly onto the environment from first to last.
                list_of_agents_shuffled[number_of_agents] = list_of_agents[number_of_agents]
                number_of_agents = number_of_agents + 1


    def _close(self):
        print("")


    def _get_status(self):
        """
            count the environment cells. If there are no X's on the environment
            then count these cells, if the total number of cells in the environment
            is the max size of the cells then all agents have died, else some agents
            are still alive.
        """
        counter = 0
        for i in range(51):
            for j in range(51):
                if(self.environment[i, j] != 'X'):
                    counter = counter + 1

        if(counter == 2601):
            return 'ALL AGENTS DEAD'
        else:
            return 'SOME AGENTS STILL ALIVE'


    def _get_state(self):
        # Render the environment to the screen.
        return self.environment


    def _agents_die(self, number_of_agents_in_list):
        """
            total_simulation_runs increments by 1 each iteration of the simulation
            when the total_simulation_runs == agents.age then agent dies and
            a new agent appears in a random location on the environment.
            number_of_agents_in_list: the number of agents created in the environment originally.
            random_ID = a new ID for the newly created agent.
            agent_to_die = the agent whose age is == the frame number
            agent_dead = boolean if agent has died.
        """

        random_ID = random.randrange(20, 100)
        agent_to_die = None
        agent_dead = False

        # Remove the agents from the dictionary
        for i in range(number_of_agents_in_list):
            if (list_of_agents_shuffled[i].get_age() == self.current_step):
                """Remove the agent from the list of agents"""
                agent_to_die = list_of_agents_shuffled[i].get_ID()
                del list_of_agents_shuffled[i]
                del list_of_agents[i]
                # An agent is being deleted from the environment.
                agent_dead = True
                number_of_agents_in_list = number_of_agents_in_list - 1


        if(agent_dead == True):
            print("AGENT DEAD!")
            # Remove the agent from the list.
            for i in range(number_of_agents_in_list):
                if agent_to_die == list_of_agents[i].get_ID():
                    del list_of_agents[i]
            # Create a new agent and add it to the list_of_agents list.
            list_of_agents.append(Agent(random_ID))
            # Add new agent to dictionary.
            list_of_agents_shuffled[number_of_agents_in_list] = list_of_agents[number_of_agents_in_list]


            # Replace the agent in the Environment with the new agent.
            for x in range(51):
                for y in range(51):
                    if(self.environment[x, y] == 'X' and self.environment_duplicate[x, y].get_ID() == agent_to_die):
                        # Add new agent to environment where old agent died.
                        self.environment[x, y] = list_of_agents[number_of_agents_in_list].get_visual()
                        self.environment_duplicate[x, y] = list_of_agents[number_of_agents_in_list]


            number_of_agents_in_list += 1

            print(f"size of list: {len(list_of_agents)} and size of dictionary {len(list_of_agents_shuffled)}")




x = SugarscapeEnv()
x._reset()
x._step('N')
x._step('E')
x._step('S')
x._step('N')
x._step('E')
x._step('S')
x._step('N')
x._step('E')
x._step('S')
x._step('N')
x._step('E')
x._step('S')
x._step('N')
x._step('E')
x._step('S')
x._step('N')
x._step('E')
x._step('S')
x._step('N')
x._step('N')
x._step('E')
x._step('S')
x._step('N')
x._step('E')
x._step('S')
x._step('N')
