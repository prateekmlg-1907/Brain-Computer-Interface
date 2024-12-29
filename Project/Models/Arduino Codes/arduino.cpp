#include <Wire.h>
#include <EEPROM.h> // Optional if you want to store small portions of data on the Arduino

// Pin numbers for LEDs to visualize activity
int ledPins[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13};
const int numElectrodes = 14;

// Placeholder for dataset signals (use EEPROM for larger datasets)
float datasetSignals[10][14] = {
  {4.12, 4.15, 4.18, 4.21, 4.25, 4.30, 4.35, 4.40, 4.45, 4.50, 4.55, 4.60, 4.65, 4.70},
  {4.20, 4.22, 4.24, 4.28, 4.30, 4.33, 4.38, 4.42, 4.47, 4.52, 4.57, 4.62, 4.67, 4.72},
  // Add more rows from your dataset here
};

void setup() {
  Serial.begin(9600); // Communication with PC
  for (int i = 0; i < 12; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  static unsigned long lastSwitch = 0;
  static bool useDataset = false; // Toggle between random and dataset

  if (millis() - lastSwitch > 30000) { // Switch every 30 seconds
    useDataset = !useDataset;
    lastSwitch = millis();
  }

  if (useDataset) {
    // Send dataset signals
    for (int row = 0; row < 10; row++) {
      for (int col = 0; col < numElectrodes; col++) {
        Serial.print(datasetSignals[row][col], 6); // Send with 6 decimal places
        Serial.print(",");
        analogWrite(ledPins[col % 12], map(datasetSignals[row][col] * 100, 400, 500, 0, 255)); // Visual feedback
      }
      Serial.println(); // End of one row
      delay(500); // Delay between rows
    }
  } else {
    // Send random signals
    for (int i = 0; i < numElectrodes; i++) {
      float randomValue = 4.0 + static_cast<float>(random(0, 1000)) / 1000.0; // Generate random 4.0–5.0
      Serial.print(randomValue, 6);
      Serial.print(",");
      analogWrite(ledPins[i % 12], map(randomValue * 100, 400, 500, 0, 255)); // Visual feedback
    }
    Serial.println();
    delay(100); // Random signals every 100 ms
  }
}
