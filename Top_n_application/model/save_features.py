import numpy as np
import librosa
import os

SAMPLE_RATE = 22050


def save_features_to_dict_single(audio_file):
    """Save features will save a single file into a feature to
    be processed by neural network model. Final result will
    be a dictionary of just the features not labels as
    they are not needed for predictions.
    Note: audio file will be deleted after processing."""
    # Functions should be altered depending on model used but the final
    # dictionary should have a features key with the value being an array
    # of the processed features. If function is updated ensure you update
    # the final shape in the model_predict function

    # dictinary to save data to return
    data_dict = {'features': []}

    # pulls out genre from audio files
    y, sr = librosa.load(audio_file, sr=SAMPLE_RATE)
    # y = numpy array of audio data
    # sr = sample rate

    # # MFCC
    mfcc = np.array(librosa.feature.mfcc(y=y, sr=sr))
    mfcc_mean = mfcc.mean(axis=1)
    mfcc_min = mfcc.min(axis=1)
    mfcc_max = mfcc.max(axis=1)
    mfcc_feature = np.concatenate((mfcc_mean, mfcc_min, mfcc_max))

    # Compute the Chromagram
    chroma = np.array(librosa.feature.chroma_stft(y=y, sr=sr))
    chroma_mean = chroma.mean(axis=1)
    chroma_min = chroma.min(axis=1)
    chroma_max = chroma.max(axis=1)
    chroma_feature = np.concatenate((chroma_mean, chroma_min, chroma_max))
    # # # Compute Tonnetz
    tonnetz = np.array(librosa.feature.tonnetz(y=y, sr=sr))
    tntz_mean = tonnetz.mean(axis=1)
    tntz_min = tonnetz.min(axis=1)
    tntz_max = tonnetz.max(axis=1)
    tntz_feature = np.concatenate((tntz_mean, tntz_min, tntz_max))

    # # # Mel Spectograms
    mel_spec = np.array(librosa.feature.melspectrogram(y=y, sr=sr))
    ms_mean = mel_spec.mean(axis=1)
    ms_min = mel_spec.min(axis=1)
    ms_max = mel_spec.max(axis=1)
    mel_spec_feature = np.concatenate((ms_mean, ms_min, ms_max))

    # STFT
    stft = np.array(np.abs(librosa.stft(y=y)))
    stft_mean = stft.mean(axis=1)
    stft_min = stft.min(axis=1)
    stft_max = stft.max(axis=1)
    stft_feature = np.concatenate((stft_mean, stft_min, stft_max))

    # # # harmonic and percussive components
    D_harmonic, D_percussive = np.array(librosa.decompose.hpss(stft, margin=4))
    D_harmonic_mean = D_harmonic.mean(axis=1)
    D_harmonic_min = D_harmonic.min(axis=1)
    D_harmonic_max = D_harmonic.max(axis=1)
    D_harmonic_feature = np.concatenate((D_harmonic_mean, D_harmonic_min,
                                         D_harmonic_max))

    D_percussive_mean = D_percussive.mean(axis=1)
    D_percussive_min = D_percussive.min(axis=1)
    D_percussive_max = D_percussive.max(axis=1)
    D_percussive_feature = np.concatenate((D_percussive_mean, D_percussive_min,
                                           D_percussive_max))

    data_dict['features'].append(np.concatenate((chroma_feature,
                                                 mel_spec_feature,
                                                 mfcc_feature,
                                                 tntz_feature,
                                                 stft_feature,
                                                 D_harmonic_feature,
                                                 D_percussive_feature)))
    os.system("rm " + audio_file)  # If testing comment this out
    return data_dict


if __name__ == "__main__":
    pass
