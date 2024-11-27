import argparse

# CREATING CMD LINE INTERFACE FOR trim_video_clip function
"""
Trim video clip from given Start time and given End time

Args:
    input_video_file (str): Path of input video file.
    output_video_file (str): Path of output video file.
    start_time (float): Start time of video clip where to begin trimming.
    end_time (float): End time of video clip where to end trimming.

Usage (cmd):
    python trimvideoclip.py <input_video_file>
    Example:
        python trimvideoclip.py your-audio-file.mp4
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trim desired audio file")
    parser.add_argument("input_video_file", type=str, help="Path to the input video file")
    parser.add_argument("output_video_file", type=str, help="Path to the output video file")
    parser.add_argument("start_time", type=float, help="Starting time in seconds on where to begin trimming.")
    parser.add_argument("end_time", type=float, help="End time in seconds on where to end trimming.")
    args = parser.parse_args()

    if not args.input_video_file or not args.start_time or not args.start_time or not args.end_time:
        parser.print_help()
        exit(1)

    try:
        # Import here to save unnecessary library load if cmd call is incorrect
        from funcs import MoviePyFuncs as mf

        mf.trim_video_clip(args.input_video_file, args.output_video_file, args.start_time, args.end_time)
    except Exception as e:
        print(f"Error: {e}")