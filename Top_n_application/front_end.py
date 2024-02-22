from flask import Flask, render_template, redirect, request
from app_controller import controller

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/results', methods=['POST'])
def data():
    if request.method == 'POST':
        form_data = request.form
        results_dict, unedited_title = controller(form_data=form_data)
        if results_dict is None and unedited_title is None:
            return redirect('/')
        # Return statement occurs only if a file of a non-supported type is
        # submitted.
        # Front end should give some form of message to user of error.
        return render_template('results.html',
                               form_data=results_dict,
                               song_title=unedited_title)


if __name__ == "__main__":
    app.run(host='localhost', port=5002)
