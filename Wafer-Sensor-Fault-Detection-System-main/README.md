Here is your complete, **final `README.md` file** content. You can **copy and paste this directly into VS Code** or any markdown editor for your research-based ML project:

---

```markdown
# 🧠 Sensor-Driven Fault Detection in Semiconductor Wafers using Automated ML Pipelines

> ✅ Research-based Project | 🎓 SRM Institute of Science and Technology, Kattankulathur, Chennai  
> 👨‍🎓 Student: Mohit Saxena | Reg. No.: RA2211003011412  
> 🧑‍🏫 Guide: Mr. Gokul Krishnan  
> 📁 Domain: Machine Learning, Smart Manufacturing, Data Science

---

## 📌 Project Overview

This research-based project proposes an **end-to-end automated machine learning pipeline** for detecting **faulty semiconductor wafers** using **raw sensor data** instead of traditional image-based techniques. The pipeline integrates data preprocessing, handling class imbalance, model training, and real-time deployment.

---

## 🌟 Novelty of the Research

Unlike previous studies that relied on high-cost image data and deep learning (CNNs), this project introduces a **lightweight, interpretable, and sensor-driven ML pipeline**. Key novelties include:

- Use of **sensor signal data** instead of wafer images for faster, real-time deployment.
- Robust **feature selection** for model interpretability.
- **SMOTETomek** hybrid resampling to solve class imbalance issues.
- Fully automated ML pipeline with support for **online prediction via CSV input**.
- **Low computational cost** – no need for GPUs or large datasets.

---

## 🎯 Objectives

1. **Real-time Fault Detection**: Build a pipeline to classify wafers as "Good" or "Bad" based on sensor readings.
2. **Sensor-Driven Modeling**: Focus on inline process data rather than image data.
3. **Address Class Imbalance**: Apply SMOTETomek to handle skewed datasets.
4. **Model Interpretability**: Use feature selection and ensemble models for transparency.
5. **Deployment Readiness**: Enable file upload interface for factory integration.

---

## 📉 Limitations (Research Gaps) of Previous Research

1. **High Computational Cost**  
   - Previous methods used CNNs and deep models on image data.  
   - These needed powerful GPUs, limiting real-time factory deployment.

2. **Bias Due to Class Imbalance**  
   - Faulty wafers were underrepresented (~10%), causing misclassification.  
   - Many models had poor recall for defective wafers.

3. **Focus on Image Data Rather Than Sensor Data**  
   - Most prior studies used wafer map/optical images.  
   - Ignored real-time, inline sensor signals readily available on the production floor.

4. **Lack of Real-Time Deployable Systems**  
   - Most studies stopped at offline training.  
   - No automated pipelines for real-world inference.

5. **No Proper Feature Selection**  
   - Many used all sensor/image features, increasing noise and reducing explainability.

6. **Lack of Explainability**  
   - CNN-based models were black-boxes.  
   - Industrial users require reasoning behind predictions.

7. **Overfitting to Small Datasets**  
   - Accuracy inflated on small test samples.  
   - Poor generalization to other wafer lines or shifts.

---

## 🧰 Techniques & Technologies Used

| Stage            | Technique / Tool           | Description |
|------------------|----------------------------|-------------|
| Data Cleaning    | KNN Imputation              | Fill missing sensor values. |
| Scaling          | Robust Scaler               | Normalize features while minimizing outlier effect. |
| Feature Selection| Variance Threshold, RF      | Drop low-importance sensors. |
| Class Balancing  | SMOTETomek                  | Hybrid method to balance classes. |
| Model Training   | Random Forest, SVC, LR      | Trained with cross-validation. |
| Evaluation       | Accuracy, ROC-AUC, F1, etc. | Multi-metric validation. |
| Deployment       | Flask + Pickle Models       | Real-time prediction app. |

---

## 📂 Folder Structure

```

wafer-fault-detection-ml/
│
├── application.py              # Flask app entry point
├── prediction\_pipeline.py      # Code for model inference
├── training\_pipeline.py        # Training and saving ML pipeline
├── utils.py                    # Data transformation utils
├── logger.py                   # Logging utility
├── exception.py                # Error handler
├── train.csv / test.csv        # Training and test sensor data
├── input\_\_.csv                 # Input file format for predictions
├── predicted\_file.csv          # Output file with predictions
├── README.md                   # Project overview (this file)
└── models/                     # Pickled model files

````

---

## 🚀 How to Run the Project

### ✅ Step 1: Clone the Repo

```bash
git clone https://github.com/yourusername/wafer-fault-detection-ml.git
cd wafer-fault-detection-ml
````

### ✅ Step 2: Install Required Libraries

```bash
pip install -r requirements.txt
```

### ✅ Step 3: Train the Model

```bash
python training_pipeline.py
```

### ✅ Step 4: Run Flask Web Interface

```bash
python application.py
```

### ✅ Step 5: Upload CSV for Prediction

* Navigate to `http://127.0.0.1:5000/`
* Upload a CSV file with sensor data.
* Get an output CSV showing wafer status: **Good** / **Bad**.

---

## 🧪 Sample CSV Format

| Sensor1 | Sensor2 | Sensor3 | ... | SensorN |
| ------- | ------- | ------- | --- | ------- |
| 52.1    | 120.5   | 0.032   | ... | 84.2    |

---

## 📊 Model Evaluation Summary

| Metric    | Value  |
| --------- | ------ |
| Accuracy  | 97.37% |
| ROC-AUC   | 0.97   |
| Precision | High   |
| Recall    | High   |
| F1 Score  | High   |

---

## 🖼️ Output Section

You can paste your output screenshots below:

### 1. 📤 Input CSV Upload

![Input Example](screenshots/input_csv.png)

### 2. 🧠 Prediction Interface

![Prediction UI](screenshots/interface.png)

### 3. 📄 Output CSV with Status

![Output](screenshots/output_csv.png)

### 4. 📈 Model Evaluation Metrics

![Metrics](screenshots/metrics.png)

---

## 🏫 Institution

**SRM Institute of Science and Technology**
Kattankulathur, Chennai – 603203, India

---

## 📧 Contact

**👨‍💻 Author:** Mohit Saxena
**🎓 Register Number:** RA2211003011412
**📫 Email:** [mohitsaxena@email.com](mailto:mohitsaxena@email.com)
**🔬 Type:** Research-based Final Year Project (2025)

---

```

Let me know if you'd like this saved as a `.md` file and downloaded!
```
