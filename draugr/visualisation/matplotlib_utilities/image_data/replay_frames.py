#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 10/12/2019
           """

from typing import Sequence

from matplotlib import animation, pyplot

from draugr.python_utilities.platform_context import in_ipynb

__all__ = ["replay_frames"]


def replay_frames(
    frames: Sequence, interval: int = 100, is_ipython: bool = in_ipynb
) -> None:
    """
    Displays a list of frames as a gif, with controls
    """
    # pyplot.figure(figsize=(frames[0].shape[1] / 72.0, frames[0].shape[0] / 72.0), dpi = 72)
    patch = pyplot.imshow(frames[0])
    pyplot.axis("off")

    def animate(start_episode):
        """description"""
        patch.set_data(frames[start_episode])

    anim = animation.FuncAnimation(
        pyplot.gcf(), animate, frames=len(frames), interval=interval
    )
    if is_ipython:
        from IPython.display import display

        display(anim)
    else:
        pyplot.show()


if __name__ == "__main__":

    def main() -> None:
        """
        :rtype: None
        """
        import gym

        env = gym.make("Pendulum-v1")
        state = env.reset()

        frames = []
        done = False
        while not done:
            frames.append(env.render("rgb_array"))

            state, reward, done, info = env.step(env.action_space.sample())
        env.close()

        replay_frames(frames)

    main()
