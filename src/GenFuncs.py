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