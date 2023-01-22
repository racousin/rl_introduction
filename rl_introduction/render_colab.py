from IPython.core.display import Video, display
from colabgymrender.recorder import Recorder
from moviepy.editor import *
import time
import cv2
import gym
import os

os.environ["SDL_VIDEODRIVER"] = "dummy"


class Recorder(gym.Wrapper):
    def __init__(
        self,
        env,
        directory,
        auto_release=True,
        size=None,
        fps=None,
        rgb=True,
        slow_coeff=1,
    ):
        super(Recorder, self).__init__(env)
        self.directory = directory
        self.auto_release = auto_release
        self.active = True
        self.rgb = rgb
        self.slow_coeff = slow_coeff

        if not os.path.exists(self.directory):
            os.mkdir(self.directory)

        if size is None:
            self.env.reset()
            self.size = self.env.render(mode="rgb_array").shape[:2][::-1]
        else:
            self.size = size

        if fps is None:
            if "video.frames_per_second" in self.env.metadata:
                self.fps = self.env.metadata["video.frames_per_second"]
            else:
                self.fps = 30
        else:
            self.fps = fps

    def pause(self):
        self.active = False

    def resume(self):
        self.active = True

    def _start(self):
        self.cliptime = time.time()
        self.path = f"{self.directory}/{self.cliptime}.mp4"
        fourcc = cv2.VideoWriter_fourcc(*"MP4V")
        self._writer = cv2.VideoWriter(self.path, fourcc, self.fps, self.size)

    def _write(self):
        if self.active:
            frame = self.env.render(mode="rgb_array")
            if self.rgb:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            for i in range(self.slow_coeff):
                self._writer.write(frame)

    def release(self):
        self._writer.release()

    def reset(self, *args, **kwargs):
        observation = self.env.reset(*args, **kwargs)
        self._start()
        self._write()
        return observation

    def step(self, *args, **kwargs):
        data = self.env.step(*args, **kwargs)
        self._write()

        if self.auto_release and data[2]:
            self.release()

        return data

    def play(self):
        start = time.time()
        filename = "temp-{start}.mp4"
        clip = VideoFileClip(self.path)
        clip.write_videofile(filename, progress_bar=False, verbose=False)
        display(Video(filename, embed=True))
        os.remove(filename)


def gym_render(
    env_name="FrozenLake-v1",
    directory="./video",
    size=None,
    fps=None,
    slow_coeff=2,
    agent="random",
    max_step=500,
):
    env = gym.make(env_name)
    directory = directory
    env = Recorder(env, directory, slow_coeff=slow_coeff, size=size, fps=fps)
    state = env.reset()
    done = False
    while not done or max_step > 0:
        if agent == "random":
            action = env.action_space.sample()
        else:
            action = agent.act(state)
        state, reward, done, info = env.step(action)
        max_step -= 1

    return env.play()
