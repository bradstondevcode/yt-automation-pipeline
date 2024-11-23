import argparse

# CREATING CMD LINE INTERFACE FOR transcribe_audio_with_whisper function
"""
Use Command Line to Trim, Transcribe, and Summarize audio file

Args:
    input_file (str): Path to the input audio file.
    ptf (bool): If transcription should be printed to file.

Usage (cmd):
    python trimvideoclip.py <input_video_file>
    Example:
        python trimvideoclip.py your-audio-file.mp4
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trim desired audio file")
    parser.add_argument("input_video_file", type=str, help="Path to the input video file")
    parser.add_argument("output_video_file", type=str, help="Path to the output video file")
    args = parser.parse_args()

    if not args.input_video_file or not args.output_video_file:
        parser.print_help()
        exit(1)

    try:
        # Import here to save unnecessary library load if cmd call is incorrect
        import MoviePyFuncs as mf
        mf.trim_movie(args.input_video_file, args.output_video_file)
    except Exception as e:
        print(f"Error: {e}")