from moviepy import *

def trim_movie(input_clip_file, output_clip_file):
    """
        Trim video clip

        Args:
            input_clip_file (str): Path of input video file.
            output_clip_file (str): Path of output video file.

        Returns:
            trimmed_clip (object): Trimmed video clip
        """

    clip = VideoFileClip(input_clip_file).with_subclip(10, 20)

    video = CompositeVideoClip([clip])

    video.write_videofile(input_clip_file)


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
