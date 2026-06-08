from flask import Flask
from flask import render_template
from flask import request

import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load(
    "model/student_model.pkl"
)

@app.route('/')
def home():
    return render_template(
        'index.html'
    )

@app.route('/predict', methods=['POST'])
def predict():

    data = pd.DataFrame([{
        'Age': float(request.form['Age']),
        'Gender': float(request.form['Gender']),
        'Ethnicity': float(request.form['Ethnicity']),
        'ParentalEducation': float(request.form['ParentalEducation']),
        'StudyTimeWeekly': float(request.form['StudyTimeWeekly']),
        'Absences': float(request.form['Absences']),
        'Tutoring': float(request.form['Tutoring']),
        'ParentalSupport': float(request.form['ParentalSupport']),
        'Extracurricular': float(request.form['Extracurricular']),
        'Sports': float(request.form['Sports']),
        'Music': float(request.form['Music']),
        'Volunteering': float(request.form['Volunteering']),
        'GPA': float(request.form['GPA'])
    }])

    prediction = int(model.predict(data)[0])

    grade_labels = {
        0: "Excellent",
        1: "Very Good",
        2: "Good",
        3: "Average",
        4: "Needs Improvement"
    }

    return render_template(
        'result.html',
        prediction=prediction,
        performance=grade_labels[prediction]
    )

if __name__ == '__main__':
    app.run(debug=True)