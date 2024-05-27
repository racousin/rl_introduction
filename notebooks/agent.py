import numpy as np

class Agent:
    def __init__(self, env):
        """
        Initialize the agent with the path to the trained model.
        """
        self.env = env
        from stable_baselines3 import PPO
        self.model =  PPO.load("jojo")

    def choose_action(self, observation, action_mask=None):
        """
        Given an observation, use the model to choose the best action.
        
        Parameters:
        - observation: The current observation from the environment.
        
        Returns:
        - action: The action chosen by the model.
        """
        action, _states = self.model.predict(observation, deterministic=True)
        return action