from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pk", "rb"))

@app.route('/')
def forest_fire():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict_data():
    values = [int(x) for x in request.form.values()]
    values = [np.array(values)]
    predict = model.predict(values)
    if predict[0] == 0:
        return render_template('index.html', pred="Your forest will not catch fire.")
    else:
        return render_template('index.html', pred="Your forest can catch fire!")

if __name__ == '__main__':
    app.run(debug=True)



