import argparse

# CREATING CMD LINE INTERFACE FOR extract_audio_from_video function
"""
Use Command Line to Extract Audio from a audio file

Args:
    input_video_file (str): Path to the input audio file.
    output_audio_file (str): Path to the input audio file.

Usage (cmd):
    python extractaudiofromvideo.py <input_video_file> <output_audio_file>
    Example:
        python extractaudiofromvideo.py your-video-file.mp4 your-audio-file.mp3
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trim desired audio file")
    parser.add_argument("input_video_file", type=str, help="Path to the input video file")
    parser.add_argument("output_audio_file", type=str, help="Path to the output audio file")
    args = parser.parse_args()

    if not args.input_video_file or not args.output_audio_file:
        parser.print_help()
        exit(1)

    try:
        # Import here to save unnecessary library load if cmd call is incorrect
        from funcs import MoviePyFuncs as mf

        mf.extract_audio(args.input_video_file, args.output_audio_file)
    except Exception as e:
        print(f"Error: {e}")