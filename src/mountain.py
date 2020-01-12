import gym
from IPython import display
import matplotlib
import matplotlib.pyplot as plt
import time

if len(sys.argv) > 1:
    from spinup.utils.test_policy import load_policy, run_policy
    _, get_action = load_policy('../data/' + sys.argv[1])
    env = gym.make('MountainCarContinuous-v0')
    env.reset()
    img = plt.imshow(env.render(mode='rgb_array')) # only call this once
    for _ in range(1000):
        time.sleep(0.01)
        img.set_data(env.render(mode='rgb_array')) # just update the data
        display.display(plt.gcf())
        display.clear_output(wait=True)
        action = get_action(state)
        state, reward, done, info = env.step(action)
        env.step(action)
        if done:
            print('done')
            state = env.reset()
        print(state)

else:
    env = gym.make('MountainCarContinuous-v0')
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
