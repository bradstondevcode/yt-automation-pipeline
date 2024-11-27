import argparse

def full_video_automation_pipeline(input_video_file):
    print("Full Video Automation Pipeline")

    """
        Start process of trimming audio file, transcribing it, making different summaries, and creating highlight clips

        Args:
            input_video_file (str): Path to the video file.
    """

    print(f"Starting Full Video Automation Pipeline for {input_video_file}")

    # Remove extension from input_video_file path
    filename = input_video_file[:-4]

    # Extract audio from given video file
    extracted_audio = mpf.extract_audio(input_video_file, filename + "-extracted-audio.mp3")

    # Transcribe trimmed/spliced audio using OpenAI Whisper (print .txt & .vtt file)
    transcription_result = wf.transcribe_audio_with_whisper(extracted_audio, filename, True, True)

    # Create Summary of transcript using Meta LLama
    transcript_summary = of.summarize_transcription(transcription_result, filename, True)

    # Create timestamp format that can be used on YouTube with Google Gemini
    custom_timestamps = gemf.create_custom_timestamps_from_transcription(transcription_result, filename).text

    # Create summary of transcript for blog template (first attempt)
    blog_template = gemf.create_blog_summary_from_transcription(transcription_result, filename).text

    # Create summary of transcript for blog template (second attempt to ensure paragraph style text only)
    refined_blog = gemf.refine_blog_summary(filename).text

    # Create a JSON file that holds the highlights and timecodes for creating video highlight clips
    highlight_text = gemf.create_highlights_from_transcription_file(filename +".vtt").text

    # Trim the video into highlight clips
    mpf.trim_video_from_json(input_video_file, filename + "-highlight.json",)


# CREATING CMD LINE INTERFACE FOR full_video_automation_pipeline function
"""
Use Command Line to start process of trimming audio file, transcribing it, making different summaries, and creating highlight clips

Args:
    input_video_file (str): Path to the video file.

Usage (cmd):
    python fullvideoautomationpipeline.py <input_video_file>
    Example:
        python fullvideoautomationpipeline.py your-transcript-file.mp4
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start process of trimming audio file, transcribing it, making different summaries, and creating highlight clips")
    parser.add_argument("input_video_file", type=str, help="Path to the input video file")
    args = parser.parse_args()

    if not args.input_video_file:
        parser.print_help()
        exit(1)

    try:
        # Import here to save unnecessary library load if cmd call is incorrect
        from funcs import GeminiFuncs as gemf, OllamaFuncs as of, WhisperFuncs as wf, MoviePyFuncs as mpf

        full_video_automation_pipeline(args.input_video_file)
    except Exception as e:
        print(f"Error: {e}")