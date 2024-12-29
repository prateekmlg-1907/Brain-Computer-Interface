import pandas as pd
import joblib
import numpy as np
import pyttsx3

model = joblib.load('7. Fusion Model/fusion_model.pkl')
electrode_names = [
    'F3', 'FC5', 'AF3', 'F7', 'T7',
    'P7', 'O1', 'O2', 'P8', 'T8',
    'F8', 'AF4', 'FC6', 'F4'
]
phoneme_map = {
    0: 'f', 1: 'ee', 2: 'k', 3: 'm', 4: 'n', 5: 'ng', 6: 'oo', 7: 'ow',
    8: 'p', 9: 's', 10: 'sh', 11: 't', 12: 'ra', 13: 'v', 14: 'z', 15: 'zh'
}

user_input = input("Enter 14 electrode values separated by spaces: ")
electrode_values = np.array([float(x) for x in user_input.split()])
input_df = pd.DataFrame([electrode_values], columns=electrode_names)
predicted_phoneme = model.predict(input_df)

predicted_phoneme_name = phoneme_map[predicted_phoneme[0]]
print(f"Predicted Phoneme: {predicted_phoneme_name}")
engine = pyttsx3.init()
engine.say(predicted_phoneme_name)
engine.runAndWait()