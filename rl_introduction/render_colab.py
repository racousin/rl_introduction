import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
import imageio
from IPython import display as ipythondisplay
from pyvirtualdisplay import Display
import cv2

virtual_display = Display(visible=0, size=(1400, 900))
virtual_display.start()

# Function to save frames and display as video
def save_video_of_model(exp_name, env_name, frames, fps, scale=2):
    path = f"{exp_name}.mp4"
    writer = imageio.get_writer(path, fps=fps)
    for frame in frames:
        # Resize frame if environment is Pong or FrozenLake
        if env_name in ['PongNoFrameskip-v4', 'FrozenLake-v1']:
            frame = cv2.resize(frame, None, fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)
        writer.append_data(frame)
    writer.close()
    return path

# Function to display video
def display_video(path):
    ipythondisplay.display(ipythondisplay.Video(path, embed=True))


def exp_render(env_config):
    virtual_display = Display(visible=0, size=(1400, 900))
    virtual_display.start()
    # Setup the virtual display
    virtual_display = Display(visible=0, size=(1400, 900))
    virtual_display.start()
    env = gym.make(env_config["name"], render_mode='rgb_array')
    observation = env.reset()[0]
    done = False
    step = 0
    frames = []


    while step < env_config["nb_step"]:  # Limit steps to avoid long loops
        if "agent" in env_config:
            action = env_config["agent"].act(observation)
        else:
            action = env.action_space.sample()
        observation, reward, done, info, _ = env.step(action)
        step += 1
        if done:
          rend = env.render()
          frames += [rend] * env_config["fps"]
          observation = env.reset()
          done = False


        frames.append(env.render())


    env.close()
    

    video_path = save_video_of_model(env_config["name"], env_config["name"], frames, env_config["fps"])
    display_video(video_path)
    virtual_display.stop()
