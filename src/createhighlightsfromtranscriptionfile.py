import argparse

# CREATING CMD LINE INTERFACE FOR transcribe_audio_with_whisper function
"""
Use Command Line to Trim, Transcribe, and Summarize audio file

Args:
    transcription_vtt_file (str): Path to the input audio file.
    highlights_file (str): Path to the input audio file.

Usage (cmd):
    python createhighlightsfromtranscriptionfile.py <transcription_vtt_file> <highlights_file>
    Example:
        python createhighlightsfromtranscriptionfile.py your-transcript-file.vtt your-highlights-file.txt
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create highlights from VTT transcript")
    parser.add_argument("transcription_vtt_file", type=str, help="Path to the input .vtt file")
    parser.add_argument("highlights_file", type=str, help="Path to the output highlights txt file")
    args = parser.parse_args()

    if not args.transcription_vtt_file or not args.highlights_file:
        parser.print_help()
        exit(1)

    try:
        # Import here to save unnecessary library load if cmd call is incorrect
        import GeminiFuncs as gf
        gf.create_highlights_from_transcription_file(args.transcription_vtt_file, args.highlights_file)
    except Exception as e:
        print(f"Error: {e}")