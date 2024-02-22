from numpy import reshape
import keras # noqa # pylint: disable=unused-import


def model_predict(feature, model):
    """Calls the given model to predict and returns a results list.
    Note, only one 30 second sample should be fed at a time as it
    uses predict on batch."""
    results = model.predict_on_batch(x=reshape(feature, (1, 9723)))
    # shape should be what the model is set to
    return results


if __name__ == "__main__":
    pass
