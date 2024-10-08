#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 28-03-2021
           """

import time

import numpy
from draugr import PROJECT_APP_PATH
from draugr.torch_utilities import (
    TensorBoardPytorchWriter,
    to_tensor,
)
from draugr.torch_utilities.tensors.dimension_order import (
    nhwc_to_nchw_tensor,
)
from draugr.torch_utilities.writers.tensorboard.tensorboard_pytorch_writer import (
    VideoInputDimsEnum,
)
from trolls.render_mode import RenderModeEnum

if __name__ == "__main__":

    def main() -> None:
        """
        :rtype: None
        """
        import gym

        env = gym.make("Pendulum-v1")
        state = env.reset()

        with TensorBoardPytorchWriter(
            PROJECT_APP_PATH.user_log / "Tests" / "Writers"
        ) as writer:
            frames = []
            done = False

            start = time.time()
            while not done:
                frames.append(env.render(mode=RenderModeEnum.rgb_array.value))
                state, reward, done, info = env.step(env.action_space.sample())
            fps = len(frames) / (time.time() - start)

            env.close()
            video_array = numpy.array(frames)
            print(video_array.shape)
            writer.video(
                "replay05",
                nhwc_to_nchw_tensor(to_tensor(video_array)).unsqueeze(0),
                frame_rate=fps,
            )
            writer.video(
                "replay06",
                video_array,
                0,
                input_dims=VideoInputDimsEnum.thwc,
                frame_rate=fps,
            )
            writer.video(
                "replay08",
                numpy.stack([video_array, video_array]),
                0,
                input_dims=VideoInputDimsEnum.nthwc,
                frame_rate=fps,
            )

    main()
