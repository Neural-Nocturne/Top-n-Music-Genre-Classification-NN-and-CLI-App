import os
import ffmpeg # noqa # pylint: disable=unused-import


def input_fortmater_mp3(file: str):
    """Will convert mp3 to wav file. Note: old file will be
    deleted after conversion."""
    file_renamed_wav = file.replace('.mp3', '.wav')
    command2mp3 = "ffmpeg -i " + file + " " + file_renamed_wav
    os.system(command2mp3)
    os.system("rm " + file)
    return file_renamed_wav


if __name__ == "__main__":
    pass
