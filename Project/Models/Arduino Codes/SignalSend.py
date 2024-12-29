import serial
import pandas as pd
import pyttsx3

# Connect to Arduino
ser = serial.Serial('COM3', 9600)  # Update with your COM port
electrode_names = ['F3', 'FC5', 'AF3', 'F7', 'T7', 'P7', 'O1', 'O2', 'P8', 'T8', 'F8', 'AF4', 'FC6', 'F4']

# Load your pre-trained model
model = joblib.load('fusion_model.pkl')
phoneme_map = {0: 'f', 1: 'ee', 2: 'k', 3: 'm', 4: 'n', 5: 'ng', 6: 'oo', 7: 'ow', 8: 'p', 9: 's', 10: 'sh', 11: 't',
               12: 'ra', 13: 'v', 14: 'z', 15: 'zh'}

engine = pyttsx3.init()

while True:
    if ser.in_waiting > 0:
        # Read one line of data from the serial port
        line = ser.readline().decode('utf-8').strip()
        values = list(map(float, line.split(',')))

        if len(values) == len(electrode_names):
            # Create DataFrame for prediction
            input_df = pd.DataFrame([values], columns=electrode_names)
            predicted_phoneme = model.predict(input_df)
            predicted_phoneme_name = phoneme_map[predicted_phoneme[0]]

            print(f"Predicted Phoneme: {predicted_phoneme_name}")
            engine.say(predicted_phoneme_name)
            engine.runAndWait()
