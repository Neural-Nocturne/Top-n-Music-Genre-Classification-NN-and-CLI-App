import os
import ffmpeg # noqa # pylint: disable=unused-import


def input_fortmater_mp4(file: str):
    """Will convert mp4 to wav file. Note: old file will be
    deleted after conversion."""
    file_renamed_mp3 = file.replace('.mp4', '.mp3')
    file_renamed_wav = file.replace('.mp4', '.wav')
    command2mp3 = "ffmpeg -i " + file + " " + file_renamed_mp3
    command2wav = "ffmpeg -i " + file_renamed_mp3 + " " + file_renamed_wav
    os.system(command2mp3)
    os.system("rm " + file)
    os.system(command2wav)
    os.system("rm " + file_renamed_mp3)
    return file_renamed_wav


if __name__ == "__main__":
    pass
