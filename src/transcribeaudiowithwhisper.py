import argparse



# CREATING CMD LINE INTERFACE FOR transcribe_audio_with_whisper function
"""
Use Command Line to Trim, Transcribe, and Summarize audio file

Args:
    input_file (str): Path to the input audio file.
    ptf (bool): If transcription should be printed to file.

Usage (cmd):
    python transcribeaudiowithwhisper.py <input_file> <-ptf>
    Example:
        python transcribeaudiowithwhisper.py your-audio-file.wav -ptf 
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe desired audio file")
    parser.add_argument("input_file", type=str, help="Path to the input audio file")
    parser.add_argument("-ptf", action="store_true", default=False, help="Print transcription to file")
    parser.add_argument("-vtt", action="store_true", default=False, help="Create VTT transcription file")
    parser.add_argument("-srt", action="store_true", default=False, help="Create SRT transcription file")
    parser.add_argument("-json", action="store_true", default=False, help="Create JSON transcription file")
    args = parser.parse_args()

    if not args.input_file:
        parser.print_help()
        exit(1)

    try:
        # Import here to save unnecessary library load if cmd call is incorrect
        import WhisperFuncs as wf
        wf.transcribe_audio_with_whisper(args.input_file, args.ptf, args.vtt, args.srt, args.json)
    except Exception as e:
        print(f"Error: {e}")