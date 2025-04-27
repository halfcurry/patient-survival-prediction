# Load your trained model
import gradio
import joblib

save_file_name = "xgboost-model.pkl"

xgb_clf = joblib.load(save_file_name)

# Function for prediction

def predict_death_event(age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure,
                        platelets, serum_creatinine, serum_sodium, sex, smoking, time):
    # Prepare the input as a 2D array for prediction
    features = [[
        int(age),
        int(anaemia),
        float(creatinine_phosphokinase),
        int(diabetes),
        float(ejection_fraction),
        int(high_blood_pressure),
        float(platelets),
        float(serum_creatinine),
        float(serum_sodium),
        int(sex),
        int(smoking),
        int(time)
    ]]
    pred = xgb_clf.predict(features)[0]
    return f"{pred}"

"""For categorical user input, user [Radio](https://www.gradio.app/docs/radio) button component.

For numerical user input, user [Slider](https://www.gradio.app/docs/slider) component.
"""

# Inputs from user
age = gradio.Slider(minimum = 30, maximum = 110, value = 60, label = "Age")
anaemia = gradio.Radio(choices = [0, 1], label = "Anaemia", value=0)
creatinine_phosphokinase = gradio.Slider(minimum = 10, maximum = 10000, value = 1000, label = "Creatinine Phosphokinase")
diabetes = gradio.Radio(choices = [0, 1], label = "Diabetes", value=0)
ejection_fraction = gradio.Slider(minimum = 0, maximum = 100, value = 20, label = "Ejection Fraction")
high_blood_pressure = gradio.Radio(choices = [0,1], label = "High Blood Pressure", value=0)
platelets = gradio.Slider(minimum = 10000, maximum = 1000000, value = 300000, label = "Platelets")
serum_creatinine = gradio.Slider(minimum = 0.5, maximum = 10.0, value = 1.0, label = "Serum Creatinine")
serum_sodium = gradio.Slider(minimum = 100, maximum = 200, value = 100, label = "Serum Sodium")
sex = gradio.Radio(choices = [0,1], label = "Sex", value=0)
smoking = gradio.Radio(choices = [0,1], label = "Smoking", value=0)
time = gradio.Slider(minimum = 0, maximum = 500, value = 100, label = "Time")
inputs = [age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time]

# Output response
outputs = gradio.Textbox(label = "Death Event")

# Gradio interface to generate UI link
title = "Patient Survival Prediction"
description = "Predict survival of patient with heart failure, given their clinical record"

iface = gradio.Interface(fn = predict_death_event,
                         inputs = inputs,
                         outputs = outputs,
                         title = title,
                         description = description,
                         allow_flagging='never')

iface.launch(server_name="0.0.0.0", server_port=8001)  # server_name="0.0.0.0", server_port = 8001   # Ref: https://www.gradio.app/docs/interface

