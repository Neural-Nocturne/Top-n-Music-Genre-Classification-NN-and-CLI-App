import validators
import os
from model.input_format_mp3 import input_fortmater_mp3
from model.input_fortmat_mp4 import input_fortmater_mp4
from model.get_youtube_file import get_youtube_audio_file


def input_checker_and_formatter(user_input: str):
    """Will check input and format it appropriately, if user_input
    is a link it will download the youtube link and also format it.
    user_input: string of the file path or url provided by user. """
    formatted_file = ""
    title = ""
    unedited_title = ""
    if user_input.endswith('.mp3'):
        formatted_file = input_fortmater_mp3(user_input)
        title = user_input.removesuffix(".mp3")
        unedited_title = title
    elif user_input.endswith('.mp4'):
        formatted_file = input_fortmater_mp4(user_input)
        title = user_input.removesuffix(".mp4")
        unedited_title = title
    elif user_input.endswith('wav'):
        formatted_file = user_input
        title = user_input.removesuffix(".wav")
        unedited_title = title
    elif validators.url(user_input):  # tested
        retrived_file, title, unedited_title = get_youtube_audio_file(user_input) # noqa
        formatted_file = input_fortmater_mp4(os.path.basename(retrived_file))
    else:
        print('Error file type not accepted')
        return None, None, None
    # the calling function should interpret as an error and handle it
    return formatted_file, title,  unedited_title


if __name__ == "__main__":
    pass
