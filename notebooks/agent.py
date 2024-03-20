import numpy as np
from stable_baselines3 import PPO

class Agent:
    def __init__(self):
        """
        Initialize the agent with the path to the trained model.
        """
        self.model = PPO.load('model.zip')

    def choose_action(self, observation):
        """
        Given an observation, use the model to choose the best action.
        
        Parameters:
        - observation: The current observation from the environment.
        
        Returns:
        - action: The action chosen by the model.
        """
        action, _states = self.model.predict(observation, deterministic=True)
        return action