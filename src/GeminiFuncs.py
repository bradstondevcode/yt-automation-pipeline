import os
from dotenv import load_dotenv
import google.generativeai as genai
import SetupPrompts as s_prompts

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
gem_model = genai.GenerativeModel("gemini-1.5-flash")
chat = gem_model.start_chat()

#TODO: Add ability to create custom timestamps from transcription file
#TODO: Add ability to create blog summary from transcription file

def create_custom_timestamps_from_transcription(transcription_result, filename):
    """
    Create a custom timestamps text and file from transcription result.

    Args:
        transcription_result (object): Transcription data object from Whisper
        filename (str): Name of output audio file.
    Returns:
        first_response (object): response data object from Google Gemini
    """

    first_response = chat.send_message(s_prompts.timestamp_prompt + transcription_result["text"])

    with open(filename + '-timestamps.txt', 'w') as file:
        file.write(first_response.text)

    print("=============================================/n")
    print(first_response.text)
    print("=============================================/n")

    return first_response

def create_blog_summary_from_transcription(transcription_result, filename):
    """
    First attempt at creating a transcript summary in blog style text  and file from transcription result.

    Args:
        transcription_result (object): Transcription data object from Whisper
        filename (str): Name of output audio file.
    Returns:
        second_response (object): response data object from Google Gemini
    """
    second_response = chat.send_message(s_prompts.blog_summary + transcription_result["text"])

    with open(filename + '-summaryone.txt', 'w') as file:
        file.write(second_response.text)

    print("=============================================/n")
    print(second_response.text)
    print("=============================================/n")

    return second_response

def refine_blog_summary(filename):
    """
        Refined summary using instructions to make blog summary and file based on first blog summary attempt.

        Args:
            filename (str): Name of output audio file.
        Returns:
            second_response (object): response data object from Google Gemini
        """
    third_response = chat.send_message(s_prompts.refine_blog_summary)

    with open(filename + '-summarytwo.txt', 'w') as file:
        file.write(third_response.text)

    print("=============================================/n")
    print(third_response.text)
    print("=============================================/n")

    return third_response