import argparse

# CREATING CMD LINE INTERFACE FOR transcribe_audio_with_whisper function
"""
Use Command Line to Transcribe audio with Whisper

Args:
    input_file (str): Path to the input audio file.
    print_to_file (bool): If transcription should be printed to .txt file (optional).
    create_vtt (bool): If transcription should be printed to .vtt file (optional).
    create_srt (bool): If transcription should be printed to .srt file (optional).
    create_json (bool): If transcription should be printed to .json file (optional).

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
        from funcs import WhisperFuncs as wf

        wf.transcribe_audio_with_whisper(args.input_file,"", args.ptf, args.vtt, args.srt, args.json)
    except Exception as e:
        print(f"Error: {e}")