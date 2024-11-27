import os
import re
from dotenv import load_dotenv
import google.generativeai as genai
from . import SetupPrompts as s_prompts
from . import GenFuncs as gen_funcs

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
gem_model = genai.GenerativeModel("gemini-1.5-flash")
chat = gem_model.start_chat()

#TODO: Add ability to create custom timestamps from transcription file thru command line
#TODO: Add ability to create blog summary from transcription file thru command line

def create_custom_timestamps_from_transcription(transcription_result, filename, print_to_file=False):
    """
    Create a custom timestamps text and file from transcription result.

    Args:
        transcription_result (object): Transcription data object from Whisper
        filename (str): Name of output audio file.
        print_to_file (bool): Set true if output should be printed to file.
    Returns:
        first_response (object): response data object from Google Gemini
    """

    first_response = chat.send_message(s_prompts.timestamp_prompt + transcription_result["text"])

    if print_to_file:
        with open(filename + '-timestamps.txt', 'w') as file:
            file.write(first_response.text)

    print("=============================================/n")
    print(first_response.text)
    print("=============================================/n")

    return first_response

def create_blog_summary_from_transcription(transcription_result, filename, print_to_file=False):
    """
    First attempt at creating a transcript summary in blog style text  and file from transcription result.

    Args:
        transcription_result (object): Transcription data object from Whisper
        filename (str): Name of output audio file.
        print_to_file (bool): Set true if output should be printed to file.
    Returns:
        second_response (object): response data object from Google Gemini
    """
    second_response = chat.send_message(s_prompts.blog_summary + transcription_result["text"])

    if print_to_file:
        with open(filename + '-summaryone.txt', 'w') as file:
            file.write(second_response.text)

    print("=============================================/n")
    print(second_response.text)
    print("=============================================/n")

    return second_response

def refine_blog_summary(filename, print_to_file=False):
    """
        Refined summary using instructions to make blog summary and file based on first blog summary attempt.

        Args:
            filename (str): Name of output audio file.
            print_to_file (bool): Set true if output should be printed to file.
        Returns:
            second_response (object): response data object from Google Gemini
        """
    third_response = chat.send_message(s_prompts.refine_blog_summary)

    if print_to_file:
        with open(filename + '-summarytwo.txt', 'w') as file:
            file.write(third_response.text)

    print("=============================================/n")
    print(third_response.text)
    print("=============================================/n")

    return third_response

def create_highlights_from_transcription_file(transcription_vtt_file):
    """
        Refined summary using instructions to make blog summary and file based on first blog summary attempt.

        Args:
            transcription_vtt_file (str): Name of output audio file.
        Returns:
            second_response (object): response data object from Google Gemini
        """

    transcription_vtt_str = gen_funcs.read_vtt_file(transcription_vtt_file)

    filename = transcription_vtt_file[:-4]
    response = gem_model.generate_content(s_prompts.transcript_highlight_prompt + transcription_vtt_str)

    # Clean output to remove JSON Markup text (if it exists)
    reg_pattern = r"```json|```"
    cleaned_json_text = re.sub(reg_pattern, "", response.text)

    with open(filename + '-highlight.json', 'w') as file:
        file.write(cleaned_json_text)

    print("=============================================/n")
    print(response.text)
    print("=============================================/n")
    print("=============================================/n")
    print(cleaned_json_text)
    print("=============================================/n")

    return response