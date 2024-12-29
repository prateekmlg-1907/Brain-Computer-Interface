# 🚀 **Brain-Computer Interface (BCI) Project** 🌐

Welcome to the **BCI Project**! This repository represents cutting-edge research and development in brain-computer interfaces, leveraging advanced machine learning models and the BioAmp EXG Pill for EEG signal processing. 🧠✨

---

## 📂 **Project Structure**
Here's a quick overview of the key components in this repository:

### 📄 **Documentation**
- **Phase 2 Reports:** Conference and journal papers, diagrams, system design, and methodology.
- **References:** Base papers, EEG reports, and additional resources.
- **Reports:** Final project reports for Phase 2.

### 🤖 **Models**
- Multiple machine learning models including:
  - 🌲 **Random Forest**
  - 📈 **XGBoost**
  - 🔄 **Recurrent Neural Networks (RNN)**
  - 🕸️ **Long Short-Term Memory (LSTM)**
  - 🧠 **1D Convolutional Neural Networks (1D CNN)**
  - 🤖 **Transformers**
  - 🔗 **Fusion Model** (Combining top-performing models for improved accuracy)

### 🔌 **BioAmp Folder**
- **Arduino Code**: Single-electrode BioAmp implementation for future integration.
- **SpikeCode**: Code for advanced spike-based signal processing.
- **Data**: Sample EEG signals in CSV format.

---

## 💻 **How to Run the Project**
Follow these steps to reproduce the results:

1. **Train the Models**:
   - 🟢 Start by running **Random Forest** and **XGBoost** models.
   - 📊 Use the metrics generated in the respective folders to validate results.

2. **Run the Fusion Model**:
   - 🔗 Combine the trained models using the **Fusion Model** notebook.
   - 🚨 Note: The Fusion Model requires **4GB of RAM** for computation.

3. **Prediction**:
   - 🧮 Execute the `predict.py` script to test and get real-time predictions.

---

## 🔭 **Future Implementation**
Our roadmap includes:
- 🧠 **BioAmp EXG Pill Integration**:
  - Hardware-based real-time EEG signal acquisition using BioAmp chips.
  - 📂 Code for single-electrode integration can be found in the **BioAmp folder**.
- 🌟 **Multi-Electrode Setup**:
  - Scalable architecture to support multiple electrodes for richer signal processing.

---

## 📊 **Results**
- Visualizations and metrics such as confusion matrices, precision-recall curves, and ROC curves are available for all models.
- 📈 Fusion Model achieves the best overall performance.

---

## 🤝 **Contributions**
Feel free to contribute by:
- Testing the BioAmp single-electrode setup.
- Exploring new EEG signal classification techniques.

---

### 🛠️ **Requirements**
- Python 3.x
- Jupyter Notebook
- Required libraries: `sklearn`, `numpy`, `pandas`, `matplotlib`, `seaborn`, etc.
- Hardware: BioAmp EXG Pill for real-time signal integration (optional).

---

## 📬 **Get in Touch**
For queries, discussions, or collaborations, feel free to contact us!

---

