import librosa
import numpy as np
import soundfile as sf

input_file_name = "your-file-name" # Insert name of file to trim silence
input_file = input_file_name + ".wav" # Change file type if needed (E.G. ".wav", ".mp3")

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

# Example usage:
output_file =  input_file_name + "_spliced.wav" # Append sliced to file name for clarity on output file
splice_silent_sections(input_file, output_file)