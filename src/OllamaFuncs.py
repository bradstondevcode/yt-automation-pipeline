import ollama
import SetupPrompts as s_prompts
# ollama runs at http://localhost:11434

def summarize_transcription(transcription_result,filename):
    """
    Use Whisper to transcribe audio and create a .vtt and .srt transcription file for captioning.

    Args:
        transcription_result (object): Transcription data object from Whisper
        filename (str): Name of output audio file.
    Returns:
        response(object): response data object from Llama
    """

    print("=============================================/n")
    print("Summary of audio transcription results")
    print("=============================================/n")

    response = ollama.chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': s_prompts.summary_prompt + transcription_result["text"],
        },
    ])

    with open(filename + '-ytsummary.txt', 'w') as file:
        file.write(response['message']['content'])

    print("=============================================/n")
    print(response['message']['content'])
    print("=============================================/n")

    return response