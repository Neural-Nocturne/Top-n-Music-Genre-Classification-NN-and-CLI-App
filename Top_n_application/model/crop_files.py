from pydub import AudioSegment
import os


def crop_file_to_30_sec(audio_file_path, out_name):
    """Will crop files to two 30 second segments if song is above 30 seconds
    Line above return statement will delete old file path after cropping"""
    t1 = 10000
    t2 = 40000
    t3 = 60000
    t4 = 90000
    waveFile = AudioSegment.from_wav(audio_file_path)
    if waveFile.duration_seconds <= 30:
        return audio_file_path, None
    waveFile1 = waveFile[t1:t2]
    waveFile2 = waveFile[t3:t4]
    waveFile1.export(out_name + '.1.wav', format="wav")
    waveFile2.export(out_name + '.2.wav', format="wav")
    os.system("rm " + audio_file_path)
    return out_name + '.1.wav', out_name + '.2.wav'


if __name__ == "__main__":
    pass
