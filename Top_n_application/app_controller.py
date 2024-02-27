import model.input_checker
import model.crop_files
import model.save_features
import model.model_predict
from keras.models import load_model
import model.format_results


def controller(form_data):
    """Controller controls flow of application, will check input and format
    it, will also crop the files if they are over 30 seconds. Lastly it will
    load the model and run the file through model prediction and format
    the results of the prediction to be printed by the front end.
    form_data: user submitted file in a dictionary, with key values Audio
    File or Youtube Link and containing the respective values in each"""
    if form_data['Audio File'] != '':
        formated_file, title, unedited_title = model.input_checker.input_checker_and_formatter(form_data['Audio File']) # noqa
    else:
        formated_file, title, unedited_title = model.input_checker.input_checker_and_formatter(form_data['Youtube Link']) # noqa

    if formated_file is None and title is None and unedited_title is None:
        return None, None
    data_list = []
    results = []
    sample1, sample2 = model.crop_files.crop_file_to_30_sec(
        formated_file, title)
    if sample1 is not None and sample2 is None:
        # this case will only occur on files that are 30 seconds or less
        data_list.append(model.save_features.save_features_to_dict_single
                         (sample1))
    else:
        data_list.append(model.save_features.save_features_to_dict_single
                         (sample1))
        data_list.append(model.save_features.save_features_to_dict_single
                         (sample2))
    loaded_model = load_model(
        '/home/elvin/Top-n-Music-Genre-Classification-NN-and-CLI-App/Top_n_application/top_n_model_75.keras') # noqa
    # should be edited for whatever model is to be utilized
    if len(data_list) > 1:
        for data_lists in data_list:
            results.append(model.model_predict.model_predict(
                data_lists['features'][0], loaded_model))

        for i in range(0, len(results[0])):
            results[0][i] = (results[0][i] + results[1][i]) / 2.0
        results_dict = model.format_results.format_results(results[0][0])
    else:
        results_dict = model.format_results.format_results(results[0][0])
    return results_dict, unedited_title


if __name__ == "__main__":
    pass
