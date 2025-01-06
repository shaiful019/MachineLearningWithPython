from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load(r'Sessions\Day12\insurance_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        # Get values from the form
        age = float(request.form['age'])
        sex = 1 if request.form['sex'] == 'male' else 0
        bmi = float(request.form['bmi'])
        children = float(request.form['children'])
        smoker = 1 if request.form['smoker'] == 'yes' else 0
        
        # Get region values
        region = request.form['region']
        region_northeast = 1 if region == 'northeast' else 0
        region_northwest = 1 if region == 'northwest' else 0
        region_southeast = 1 if region == 'southeast' else 0
        region_southwest = 1 if region == 'southwest' else 0

        # Create feature array
        features = np.array([[age, sex, bmi, children, smoker, 
                            region_northeast, region_northwest, 
                            region_southeast, region_southwest]])

        # Make prediction
        prediction = model.predict(features)[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True) 