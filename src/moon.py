import gym
from IPython import display
import matplotlib
import matplotlib.pyplot as plt
import time
import sys
from tensorflow.keras.models import Model, load_model
import numpy as np

if len(sys.argv) > 1:
    model = load_model('../src/models/test')
    env = gym.make('LunarLander-v2')
    state = env.reset()
    img = plt.imshow(env.render(mode='rgb_array')) # only call this once
    for _ in range(1000):
        time.sleep(0.01)
        img.set_data(env.render(mode='rgb_array')) # just update the data
        display.display(plt.gcf())
        display.clear_output(wait=True)
        predicted_Q = model.predict(state.reshape(1,-1))[0]
        action = np.argmax(predicted_Q)
        state, reward, done, info = env.step(action)
        env.step(action)
        if done:
            state = env.reset()
            print('done')
        print(state)
else:
    env = gym.make('LunarLander-v2')
    env.reset()
    img = plt.imshow(env.render(mode='rgb_array')) # only call this once
    for _ in range(1000):
        time.sleep(0.01)
        img.set_data(env.render(mode='rgb_array')) # just update the data
        display.display(plt.gcf())
        display.clear_output(wait=True)
        action = env.action_space.sample()
        state, reward, done, info = env.step(action)
        env.step(action)
        if done:
            print('done')
            env.reset()
        print(state)
