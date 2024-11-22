
# yt-automation-pipeline
Creating a set of AI powered tools to automate my Youtube creation process. Audio trimming,  audio transcription, and transcription summarization.


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

	```
	python trimtranscribesummarize.py your-audio-file-name.mp3 your-audio-file-name-trimmed.mp3 
	```

	Replace `your-audio-file-name.mp3` with your files name along with it's extension

	Replace `your-audio-file-name-trimmed.mp3` with your desired new file name and it's extension.

	NOTE: Current supported extensions are `.wav` and `.mp3`. Files can be either and can be converted to either type

6. Let Automation toolchain run and view results in `src` folder