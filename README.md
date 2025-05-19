# 🌞 MoonLight Energy Solutions: Solar Radiation Insights Dashboard

## 📋 Project Overview

Welcome to the **MoonLight Energy Solutions Solar Radiation Insights Dashboard**! This interactive tool is built to provide clear, data-driven insights on solar radiation, wind speed, temperature, and other environmental factors across **Benin**, **Sierra Leone**, and **Togo**.

The goal of this project is to:

* Analyze solar radiation data from three West African countries.
* Identify patterns, outliers, and correlations among variables.
* Empower energy investment decisions through visual insights.

## 🏆 Features

### Exploratory Data Analysis (EDA):

* Time-series visualization for **GHI**, **DNI**, **DHI**, and **Temperature (Tamb)**.
* Outlier detection using statistical techniques.
* Correlation analysis between **solar radiation**, **wind speed**, **humidity**, and **temperature**.

### Interactive Streamlit Dashboard:

A clean, interactive interface built with **Streamlit**, enabling users to:

* Explore correlation heatmaps.
* Navigate through time-series analysis.
* Analyze wind and solar interactions.
* Detect anomalies in solar radiation data.

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<sewasewT7>/solar-challenge-week1.git
```

### 2. Navigate into the project folder

```bash
cd solar-challenge-week1
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

* On **Windows**:

```bash
.\venv\Scripts\activate
```

* On **macOS/Linux**:

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit App

```bash
streamlit run src/app/main.py
```

Visit: [http://localhost:8501](http://localhost:8501)

## ✨ How to Use the Dashboard

Use the left sidebar in the dashboard to explore:

* **Time-Series Analysis**: Visual trends over time.
* **Correlation Heatmap Analysis**: Relationships between variables.
* **Wind-Solar Analysis**: Wind impact on GHI.
* **Outliers Detection**: Spot anomalies.

## ✨ Technologies Used

* **Python**: Core programming language
* **Pandas**: Data analysis
* **Seaborn & Matplotlib**: Visualizations
* **Streamlit**: Web-based dashboard
* **Git & GitHub**: Version control & collaboration

## 💼 Acknowledgments

Special thanks to **MoonLight Energy Solutions** for enabling this real-world application of data visualization to drive sustainability.

## 📜 Contributing

Want to contribute? Great!

* Fork the repo
* Create your branch (`git checkout -b feature-xyz`)
* Commit your changes (`git commit -am 'Add feature'`)
* Push to the branch (`git push origin feature-xyz`)
* Create a new Pull Request

## 🛠️ Contact

**Sewasew Tadele**
✉️ [sewasewtadele@gmail.com](mailto:sewasewtadele@gmail.com)

Thank you for exploring this dashboard. Let’s build sustainable energy insights together! 🌞
