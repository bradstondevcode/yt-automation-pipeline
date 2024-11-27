import argparse

def trim_transcribe_summarize(audio_input_file, audio_output_file):
    """
    Starts the entire process of trimming audio file, transcribing it and making different summaries.

    Args:
        audio_input_file (str): Path to the input audio file.
        audio_output_file (str): Path to the output audio file.
    """

    print("Trimming transcribe summarize...")
    filename = audio_output_file[:-3]

    # Splice out unwanted silence and low volume areas in audio_input_file
    audio_splice_result = af.splice_silent_sections(audio_input_file, audio_output_file)

    # Transcribe trimmed/spliced audio using OpenAI Whisper (print .txt & .vtt file)
    transcription_result = wf.transcribe_audio_with_whisper(audio_splice_result, "",True, True)

    # Create Summary of transcript using Meta LLama
    transcript_summary = of.summarize_transcription(transcription_result, filename, True)

    # Create timestamp format that can be used on YouTube with Google Gemini
    custom_timestamps= gf.create_custom_timestamps_from_transcription(transcription_result, filename, True).text

    # Create summary of transcript for blog template (first attempt)
    blog_template = gf.create_blog_summary_from_transcription(transcription_result, filename, True).text

    # Create summary of transcript for blog template (second attempt to ensure paragraph style text only)
    refined_blog = gf.refine_blog_summary(filename, True).text


# CREATING CMD LINE INTERFACE FOR trimtranscribesummarize function
"""
Use Command Line to Trim, Transcribe, and Summarize audio file

Args:
    input_file (str): Path to the input audio file.
    output_file (str): Path to the output audio file.
    
Usage (cmd):
    python trimtranscribesummarize.py <input_file> <output_file>
    Example:
        python trimtranscribesummarize.py your-audio-file.wav your-trimmed-audio-file.mp3 
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trim, Transcribe, and Summarize audio file")
    parser.add_argument("input_file", type=str, help="Path to the input audio file")
    parser.add_argument("output_file", type=str, help="Path to the output audio file")
    args = parser.parse_args()

    if not args.input_file:
        parser.print_help()
        exit(1)

    try:
        # Import here to save unnecessary library load if cmd call is incorrect
        from funcs import GeminiFuncs as gf, OllamaFuncs as of, WhisperFuncs as wf, AudioFuncs as af

        trim_transcribe_summarize(args.input_file, args.output_file)
    except Exception as e:
        print(f"Error: {e}")








