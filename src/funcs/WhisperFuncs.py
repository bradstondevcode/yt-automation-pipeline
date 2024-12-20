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
def transcribe_audio_with_whisper(audio_file, output_filename="", print_to_file=False, create_vtt=False, create_srt=False, create_json=False):
    """
    Use Whisper to transcribe audio and create .txt transcription file if desired.

    Args:
        audio_file (str): Path to the output audio file.
        output_filename (str): Path to the output file name.
        print_to_file (bool): Set true if output should be printed to file.
        create_vtt (bool): Set true to create VTT file.
        create_srt (bool): Set true to create SRT file.
        create_json (bool): Set true to create JSON file.
    Returns:
        result (object): Transcription data object from Whisper
    """

    if output_filename == "":
        output_filename = audio_file


    # Retrieve transcript of audio file from Whisper
    result = model.transcribe(audio_file, language="english", verbose=True)

    if print_to_file:
        print("=============================================/n")
        print("Printing Transcript to file...")
        print("=============================================/n")
        # Convert transcript to .txt file
        whisper_to_file_format(result, "", output_filename, "txt")

    if create_vtt:
        print("=============================================/n")
        print("Creating VTT file...")
        print("=============================================/n")
        # Convert transcript to .vtt file
        whisper_to_file_format(result, "", output_filename, "vtt")

    if create_srt:
        print("=============================================/n")
        print("Creating SRT file...")
        print("=============================================/n")
        # Convert transcript to .vtt file
        whisper_to_file_format(result, "", output_filename, "srt")

    if create_json:
        print("=============================================/n")
        print("Creating JSON file...")
        print("=============================================/n")
        # Convert transcript to .vtt file
        whisper_to_file_format(result, "", output_filename, "json")

    return result