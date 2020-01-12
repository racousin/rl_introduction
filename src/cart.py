import gym
from IPython import display
import matplotlib
import matplotlib.pyplot as plt
import time
import sys

env = gym.make('CartPole-v0')
if len(sys.argv) > 1:
    from spinup.utils.test_policy import load_policy, run_policy
    _, get_action = load_policy('../data/' + sys.argv[1])
    state = env.reset()
    img = plt.imshow(env.render(mode='rgb_array')) # only call this once
    for _ in range(5000):
        time.sleep(0.01)
        img.set_data(env.render(mode='rgb_array')) # just update the data
        display.display(plt.gcf())
        display.clear_output(wait=True)
        action = get_action(state)
        state, reward, done, info = env.step(action)
        if done:
            state =env.reset() 
            print('done')
        env.step(action)
        print(state)

else:
    env.reset()
    img = plt.imshow(env.render(mode='rgb_array')) # only call this once
    for _ in range(5000):
        time.sleep(0.01)
        img.set_data(env.render(mode='rgb_array')) # just update the data
        display.display(plt.gcf())
        display.clear_output(wait=True)
        action = env.action_space.sample()
        state, reward, done, info = env.step(action)
        env.step(action)
        print(state)
        if state[0] < -4 or state[0] > 4:
            env.reset()
