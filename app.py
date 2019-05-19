from flask import Flask, request, render_template
import numpy as np


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        choices = list(request.form.values())
        choice = np.random.choice(choices).capitalize()
        choice_string = ', '.join(str(x).lower() for x in choices)
        print(choices)
        return render_template('decision.html',
                               choice=choice,
                               choice_string=choice_string
                               )
    return render_template('page.html')


if __name__ == "__main__":
    app.run()


