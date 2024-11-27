import argparse

# CREATING CMD LINE INTERFACE FOR transcribe_audio_with_whisper function
"""
        Trim video file into specified highlight clips from give JSON file

        Args:
            input_clip_file (str): Path of input video file.
            json_file (str): Path of json highlight file

Usage (cmd):
    python trimvideofromjson.py <input_video_file> <json_file>
    Example:
        python trimvideofromjson.py your-audio-file.mp4 json_file
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trim desired audio file")
    parser.add_argument("input_video_file", type=str, help="Path to the input video file")
    parser.add_argument("json_file", type=str, help="Path to the json highlight file")
    args = parser.parse_args()

    if not args.input_video_file or not args.json_file:
        parser.print_help()
        exit(1)

    try:
        # Import here to save unnecessary library load if cmd call is incorrect
        from funcs import MoviePyFuncs as mf

        mf.trim_video_from_json(args.input_video_file, args.json_file)
    except Exception as e:
        print(f"Error: {e}")