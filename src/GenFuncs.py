def read_vtt_file(vtt_file_path):
  """
  Reads a .vtt file and returns its content as a string.

  Args:
    vtt_file_path: Path to the .vtt file.

  Returns:
    A string containing the content of the .vtt file.
  """

  with open(vtt_file_path, 'r', encoding='utf-8') as file:
    return file.read()


def convert_vtt_timestamp_to_seconds(timestamp_str):
  """Converts a string in format MM:SS.MS to total seconds.

  Args:
      timestamp_str: A string representing time in MM:SS.MS format.

  Returns:
      A float representing the total time in seconds.

  Raises:
      ValueError: If the input string is not in the correct format.
  """
  try:
    minutes, seconds_ms = timestamp_str.split(":")
    seconds, milliseconds = seconds_ms.split(".")
  except ValueError:
    raise ValueError("Invalid time format. Please use MM:SS.MS")

  # Convert each part to float and calculate total seconds
  total_seconds = float(minutes) * 60 + float(seconds) + float(milliseconds) / 1000
  return total_seconds