import numpy as np

class Agent:
    def __init__(self, env, model_path=""):
        """
        Initialize the agent with the path to the trained model.
        """
        self.model_path = model_path
        self.env = env
        model_type = model_path.split('/')[-1].split('_')[0]
        if model_type == "PPO":
            from stable_baselines3 import PPO
            self.model = PPO.load(model_path)
        elif model_type == "DQN":
            from stable_baselines3 import DQN
            self.model =  DQN.load(model_path)
        elif model_type == "A2C":
            from stable_baselines3 import A2C
            self.model =  A2C.load(model_path)
        elif model_type == "DDPG":
            from stable_baselines3 import DDPG
            self.model =  DDPG.load(model_path)
        elif model_type == "HER":
            from stable_baselines3 import HER
            self.model =  HER.load(model_path)
        elif model_type == "SAC":
            from stable_baselines3 import SAC
            self.model =  SAC.load(model_path)
        elif model_type == "TD3":
            from stable_baselines3 import TD3
            self.model =  TD3.load(model_path)
        elif model_type == "TQC":
            from stable_baselines3 import TQC
            self.model =  TQC.load(model_path)
        elif model_type == "TRPO":
            from stable_baselines3 import TRPO
            self.model =  TRPO.load(model_path)
        else:
            raise ValueError(f"Unsupported model type: {model_type}")

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