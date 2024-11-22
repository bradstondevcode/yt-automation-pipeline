import librosa
import numpy as np
import soundfile as sf
import whisper
import ollama
import google.generativeai as genai
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values
# loading variables from .env file
# ollama runs at http://localhost:11434

import SetupPrompts as s_prompts

from whisper.utils import get_writer

load_dotenv()
model = whisper.load_model("turbo")
genai.configure(api_key=os.environ["GEMINI_API_KEY"])









#Converts Whisper transcription results to a .vtt file.
def whisper_to_vtt(result, output_dir, input_audio):
    """
    Converts Whisper transcription results to a .vtt file.

    Args:
        result: The transcription result from the Whisper model.
        output_dir: The dir of the output .vtt file.
    """

    # Set some initial options values
    options = {
        'max_line_width': None,
        'max_line_count': None,
        'highlight_words': False
    }

    vtt_writer = get_writer("vtt", output_dir)
    vtt_writer(result, input_audio, options)

# Converts Whisper transcription into desired file format.
def whisper_to_file_format(result, output_dir, input_audio,output_format):
    """
    Converts Whisper transcription into desired file format.

    Args:
        result: The transcription result from the Whisper model.
        output_dir: The dir of the output .vtt file.
        input_audio: The audio file that it will reference.
        output_format: The desired output format.
    """

    # Set some initial options values
    options = {
        'max_line_width': None,
        'max_line_count': None,
        'highlight_words': False
    }

    vtt_writer = get_writer(output_format, output_dir)
    vtt_writer(result, input_audio, options)


# Splices out silent/low volume sections from an audio file.
def splice_silent_sections(input_file, output_file):
    silence_threshold_rms=0.001
    min_silence_len=10
    sample_rate=44100
    """
    Splices out silent/low volume sections from an audio file.

    Args:
        input_file (str): Path to the input audio file.
        output_file (str): Path to the output audio file.
        silence_threshold_rms (float, optional): RMS amplitude threshold for silence. Defaults to 0.01.
        min_silence_len (int, optional): Minimum length of a silent segment to be spliced out, in samples. Defaults to 1000 samples.
        sample_rate (int, optional): Sample rate of the audio. Defaults to 22050 Hz.
    """

    # Load the audio file
    y, sr = librosa.load(input_file, sr=sample_rate)

    # Calculate the RMS amplitude of each frame
    frame_size = 1024
    hop_length = 512
    rms = librosa.feature.rms(y=y, frame_length=frame_size, hop_length=hop_length)[0]

    # Identify silent segments
    silent_segments = []
    current_silent_segment = []
    for i, r in enumerate(rms):
        if r < silence_threshold_rms:
            current_silent_segment.append(i)
        else:
            if len(current_silent_segment) >= min_silence_len:
                silent_segments.append(current_silent_segment)
            current_silent_segment = []

    # Splice out silent segments
    spliced_audio = []
    last_end = 0
    for segment in silent_segments:
        start_sample = segment[0] * hop_length
        end_sample = (segment[-1] + 1) * hop_length
        spliced_audio.extend(y[last_end:start_sample])
        last_end = end_sample
    spliced_audio.extend(y[last_end:])

    # Write the spliced audio to a new file
    sf.write(output_file, np.array(spliced_audio), sr)

    print("=============================================/n")
    print(f"Audio file has been saved at {output_file}.")
    print("=============================================/n")

    result = model.transcribe(output_file,language="english", verbose= True)
    whisper_to_file_format(result,"",output_file,"vtt")
    whisper_to_file_format(result, "", output_file, "txt")
    # whisper_to_vtt(result, "", output_file)

    filename =  output_file[:-3]

    print("=============================================/n")
    print("Summary of audio transcription results")
    print("=============================================/n")

    response = ollama.chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': s_prompts.summary_prompt +  result["text"],
        },
    ])

    with open( filename + '-ytsummary.txt', 'w') as file:
        file.write(response['message']['content'])

    print("=============================================/n")
    print(response['message']['content'])
    print("=============================================/n")

    gem_model = genai.GenerativeModel("gemini-1.5-flash")
    chat = gem_model.start_chat()
    first_response = chat.send_message(s_prompts.timestamp_prompt + result["text"])

    # gem_response = gem_model.generate_content( s_prompts.timestamp_prompt + result["text"] )

    with open( filename + '-timestamps.txt', 'w') as file:
        file.write(first_response.text)

    print("=============================================/n")
    print(first_response.text)
    print("=============================================/n")

    second_response = chat.send_message(s_prompts.blog_summary + result["text"])

    with open( filename + '-summaryone.txt', 'w') as file:
        file.write(second_response.text)

    print("=============================================/n")
    print(second_response.text)
    print("=============================================/n")

    third_response = chat.send_message(s_prompts.refine_blog_summary)

    with open( filename + '-summarytwo.txt', 'w') as file:
        file.write(third_response.text)

    print("=============================================/n")
    print(third_response.text)
    print("=============================================/n")

# CREATING CMD LINE INTERFACE
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python trimaudiosilence.py <input_file> <output_file>")
        exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        # print(s_prompts.timestamp_prompt)
        # gem_model = genai.GenerativeModel("gemini-1.5-flash")
        # response = gem_model.generate_content("Write a story about a magic backpack.")
        # print(response.text)
        splice_silent_sections(input_file, output_file)
    except Exception as e:
        print(f"Error: {e}")








