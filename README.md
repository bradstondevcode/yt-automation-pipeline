
# yt-automation-pipeline
Creating a set of AI powered tools to automate my Youtube creation process. Audio trimming,  audio transcription, and transcription summarization.

## Prerequisites

- Ollama Installed ([Download Ollama here](https://ollama.com/))
  - w/ Llama 3.2 Model ([Llama3.2 page](https://ollama.com/library/llama3.2))
- Google Gemini API Key ([Obtain API Key here](https://ai.google.dev/gemini-api/docs/api-key))

## Project Dependecies

### Python Version

Python Version
```commandline
python 3.10
```

### Project Library Imports & Versions

```
google-generativeai = 0.8.3
librosa = 0.10.2.post1
python-dotenv = 1.0.1
ollama = 0.3.3
openai-whisper = 20240930
soundfile = 0.12.1
```

### Using .env file
Use a .env file located in `src` folder to import Google Gemini API key. Use this format for API Key
```
GEMINI_API_KEY = "Your-Gemini-API-Key"
```


## How To Use

1. Clone `yt-automation-pipeline` repo to local machine

2. In repo, navigate to yt-automation-pipeline folder and start Python Virtual Environment

	```
	cd "...\yt-automation-pipeline"
	.venv\Scripts\activate  
	```

	If virtual environment has been successfully started you should see (.venv) at the beginning of your command prompt line:

	```
	(.venv) ...\yt-automation-pipeline\src>
	```

3. Navigate to `src` folder in command line

	```
	cd src
	```

4. Copy and paste a file you would like to trim into your `src` folder

5. Run this command in the command line to to Trim, Transcribe, and Summarize your audio file

	```commandline
	python trimtranscribesummarize.py your-audio-file-name.mp3 your-audio-file-name-trimmed.mp3 
	```
 
	Replace `your-audio-file-name.mp3` with your files name along with it's extension

	Replace `your-audio-file-name-trimmed.mp3` with your desired new file name and it's extension.

	NOTE: Current supported extensions are `.wav` and `.mp3`. Files can be either and can be converted to either type

6. Let Automation toolchain run and view results in `src` folder

## Command Line Usage

### Trim, Transcribe, and Summarize audio file

This command completes all trim, transcription, and summarization tasks 
```commandline
	python trimtranscribesummarize.py your-audio-file-name.mp3 your-audio-file-name-trimmed.mp3  
```

Example usage with test audio file (located in project `src` folder:
```commandline
python trimtranscribesummarize.py Sample-Audio-Test.mp3 Sample-Audio-Test-trimed.mp3
```
Run the following commands for available options

```commandline
python trimtranscribesummarize.py -h
```

### Transcribe Audio w/ options

Transcribe audio (no file output):
```commandline
python transcribeaudiowithwhisper.py your-audio-file.mp3
```

Transcribe audio and output text file:
```commandline
python transcribeaudiowithwhisper.py your-audio-file.mp3 -ptf
```

Transcribe audio and output .vtt file:
```commandline
python transcribeaudiowithwhisper.py your-audio-file.mp3 -vtt
```

Transcribe audio and output text, .vtt, .srt, and .json file:
```commandline
python transcribeaudiowithwhisper.py your-audio-file.mp3 -ptf -vtt -srt -json
```

Example usage with test audio file (located in project `src` folder:
```commandline
python transcribeaudiowithwhisper.py Sample-Audio-Test.mp3 -ptf -vtt -srt -json
```

Run the following commands for available options
```commandline
python transcribeaudiowithwhisper.py -h
```