import joblib
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Load the scaler and model files
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/Predict', methods=['GET', 'POST'])
def prediction():
    return render_template('Index.html')

@app.route('/form', methods=['GET', 'POST'])
def brain():
    if request.method == 'POST':
        try:
            # Collecting the form data
            PatientNo = float(request.form['PatientNo'])
            Glucose = float(request.form['Glucose'])
            BP = float(request.form['BP'])
            SkinThickness = float(request.form['SkinThickness'])
            Insulin = float(request.form['Insulin'])
            BMI = float(request.form['BMI'])
            DPedigreeFun = float(request.form['DPedigreeFun'])
            Age = float(request.form['Age'])

            # Validating the inputs (you can modify the conditions as per your dataset requirements)
            if Glucose > 0 and BP > 0 and SkinThickness >= 0 and Insulin >= 0 and BMI > 0:
                values = [PatientNo, Glucose, BP, SkinThickness, Insulin, BMI, DPedigreeFun, Age]

                # Standardize the input data
                arr = scaler.transform([values])
                arr = model.predict(arr)

            

                return render_template('prediction.html', prediction=str(prediction[0]))
            else:
                return "Sorry.... Error in the entered values in the form. Please check the values and fill it."

        except FileNotFoundError:
            return "Model file not found", 500
    return render_template('prediction.html')

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
