#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"

__doc__ = r"""
"""
import subprocess
from pathlib import Path
from typing import Optional

from draugr.ffmpeg_utilities.extract import AUDIO_FORMAT
from warg import Number, ensure_existence, identity

__all__ = ["merge_frames"]


def get_frame_format(frames_dir: Path, formats=(".jpg", ".png")) -> str:
    """

    :param frames_dir:
    :type frames_dir:
    :return:
    :rtype:
    """
    for file_ in frames_dir.iterdir():
        if file_.is_file():
            suffix = file_.suffix.lower()
            if suffix in formats:
                return suffix


def merge_frames(
    frames_dir: Path,
    merge_audio: bool = True,
    audio_dir: Optional[Path] = None,
    merge_dir: Optional[Path] = None,
    merge_rate: Number = 25,
    ffmpeg_path: Path = "ffmpeg",
) -> None:
    """merges frame in to video

    :param frames_dir:
    :type frames_dir:
    :param merge_audio:
    :type merge_audio:
    :param audio_dir:
    :type audio_dir:
    :param merge_dir:
    :type merge_dir:
    :param merge_rate:
    :type merge_rate:
    :param ffmpeg_path:
    :type ffmpeg_path:
    """
    postfix = ""  # "_00"
    vid_dir = frames_dir.parent

    if audio_dir is None:
        audio_dir = vid_dir / "audio"

    if merge_dir is None:
        merge_dir = ensure_existence(vid_dir / "merge", sanitisation_func=identity)

    shortname = vid_dir.name

    # a = f"{shortname}-%05d{postfix}{get_frame_format(frames_dir)}"  # 05d is for 5 digits in ids
    # a = "brandt.mp4-%*_00.png"
    a = f"%05d{get_frame_format(frames_dir)}"
    temp_out = str(merge_dir / "temp.mp4")
    subprocess.call(
        [
            str(ffmpeg_path),
            "-r",
            str(merge_rate),
            "-pattern_type",
            "glob",
            "-i",
            str(frames_dir / f"*{get_frame_format(frames_dir)}"),
            "-y",
            "-c:v",
            "libx264",
            "-vf",
            "fps=25,format=yuv420p",
            temp_out,
        ]
    )

    a = []

    if merge_audio:
        sound_dir = (audio_dir / "track").with_suffix(f".{AUDIO_FORMAT.lstrip('.')}")
        if sound_dir.exists():
            a.extend(["-i", str(sound_dir)])
        else:
            print(f"No audio found in {sound_dir}")

    subprocess.call(
        [
            str(ffmpeg_path),
            "-i",
            temp_out,
            *a,
            "-vcodec",
            "copy",
            "-acodec",
            "copy",
            "-y",
            str((merge_dir / "out").with_suffix(f".{'mp4'.lstrip('.')}")),
        ]
    )


if __name__ == "__main__":
    merge_frames(
        Path.home() / "DataWin" / "frames",
        ffmpeg_path=Path.home()
        / "OneDrive - Alexandra Instituttet"
        / "Applications"
        / "ffmpeg-5.0-essentials_build"
        / "bin"
        / "ffmpeg.exe",
    )
