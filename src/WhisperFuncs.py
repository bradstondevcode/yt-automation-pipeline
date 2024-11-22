import whisper
from whisper.utils import get_writer

model = whisper.load_model("turbo")

# Converts Whisper transcription into desired file format.
def whisper_to_file_format(result, output_dir, input_audio, output_format):
    """
    Converts Whisper transcription into desired file format.

    Args:
        result: The transcription result from the Whisper model.
        output_dir: The dir of the output  file.
        input_audio: The audio file that it will reference.
        output_format: The desired output format.
            options: "vtt", "srt", "txt", "json"
    """

    # Set some initial options values
    options = {
        'max_line_width': None,
        'max_line_count': None,
        'highlight_words': False
    }

    vtt_writer = get_writer(output_format, output_dir)
    vtt_writer(result, input_audio, options)

# Use Whisper to transcribe audio and create .txt transcription file if desired.
def transcribe_audio_with_whisper(audio_file, print_to_file=False):
    """
    Use Whisper to transcribe audio and create .txt transcription file if desired.

    Args:
        audio_file (str): Path to the output audio file.
        print_to_file (bool): Set true if output should be printed to file.
    Returns:
        result (object): Transcription data object from Whisper
    """

    # Retrieve transcript of audio file from Whisper
    result = model.transcribe(audio_file, language="english", verbose=True)

    if print_to_file:
        print("=============================================/n")
        print("Printing Transcript to file...")
        print("=============================================/n")
        # Convert transcript to .srt file
        whisper_to_file_format(result, "", audio_file, "txt")

    return result