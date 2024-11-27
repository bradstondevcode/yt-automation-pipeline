from moviepy import *
import json
from . import GenFuncs as gf


def trim_video_clip(input_video_file, output_video_file, start_time, end_time):
    """
        Trim video clip from given Start time and given End time

        Args:
            input_video_file (str): Path of input video file.
            output_video_file (str): Path of output video file.
            start_time (float): Start time of video clip where to begin trimming.
            end_time (float): End time of video clip where to end trimming.

        Returns:
            trimmed_clip (object): Trimmed video clip
        """

    clip = VideoFileClip(input_video_file).with_subclip(start_time, end_time)

    video = CompositeVideoClip([clip])

    video.write_videofile(output_video_file)


def trim_video_from_json(input_video_file, json_file):
    """
        Trim video file into specified highlight clips from give JSON file

        Args:
            input_video_file (str): Path of input video file.
            json_file (str): Path of json file
        """

    filename = input_video_file[:-4]

    with open(json_file, 'r') as f:
        json_data = json.load(f)

    for highlight in json_data:
        current_topic = highlight['topic']
        current_start_time_str = highlight['startTime']
        current_end_time_str = highlight['endTime']
        print("=====================")

        current_start_time = gf.convert_vtt_timestamp_to_seconds(current_start_time_str)
        current_end_time = gf.convert_vtt_timestamp_to_seconds(current_end_time_str)

        print(f"Start Time: {current_start_time}")
        print(f"Start Time: {current_end_time}")
        print("=====================")

        clip = VideoFileClip(input_video_file).with_subclip(current_start_time, current_end_time)
        video = CompositeVideoClip([clip])
        video.write_videofile(filename + current_topic + ".mp4")

    print(" Video Trimming Completed!")


def extract_audio(input_clip_path, output_audio_file):
    """Extracts audio from a video file and saves it as a separate audio file.

    Args:
        input_clip_path: Path to the input video file.
        output_audio_file: Path to the output audio file.
    """

    # Load the video file
    video_clip = VideoFileClip(input_clip_path)

    # Extract the audio from the video clip
    audio_clip = video_clip.audio

    # Write the audio to a file
    audio_clip.write_audiofile(output_audio_file)

    # Close the video and audio clips
    video_clip.close()
    audio_clip.close()

    return output_audio_file
