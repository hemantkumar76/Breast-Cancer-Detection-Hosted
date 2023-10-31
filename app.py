from flask import Flask, request, url_for, redirect, render_template, jsonify
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("breast_cancer.pkl", "rb"))


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    int_features = [
        int(data["clumpThickness"]),
        int(data["uniformityCellSize"]),
        int(data["uniformityCellShape"]),
        int(data["marginalAdhesion"]),
        int(data["singleEpithelialCellSize"]),
        int(data["bareNuclei"]),
        int(data["blandChromatin"]),
        int(data["normalNucleoli"]),
        int(data["mitoses"]),
    ]
    final = [np.array(int_features)]
    prediction = model.predict(final)
    if prediction[0] == 2:
        return jsonify(result="You have Benign")
    elif prediction[0] == 4:
        return jsonify(result="You have Malignant")
    else:
        return jsonify(result="Error in Prediction")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
