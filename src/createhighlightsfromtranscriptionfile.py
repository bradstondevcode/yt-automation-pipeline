import argparse

# CREATING CMD LINE INTERFACE FOR create_highlights_from_transcription_file function
"""
Use Command Line to Trim, Transcribe, and Summarize audio file

Args:
    transcription_vtt_file (str): Path to the input audio file.

Usage (cmd):
    python createhighlightsfromtranscriptionfile.py <transcription_vtt_file>
    Example:
        python createhighlightsfromtranscriptionfile.py your-transcript-file.vtt
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create highlights from VTT transcript")
    parser.add_argument("transcription_vtt_file", type=str, help="Path to the input .vtt file")
    args = parser.parse_args()

    if not args.transcription_vtt_file:
        parser.print_help()
        exit(1)

    try:
        # Import here to save unnecessary library load if cmd call is incorrect
        from funcs import GeminiFuncs as gf

        gf.create_highlights_from_transcription_file(args.transcription_vtt_file)
    except Exception as e:
        print(f"Error: {e}")