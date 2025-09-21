# 🚴 Paris Bike App

An interactive Streamlit application to explore and analyze bike traffic data in Paris.  
This project is based on a dataset of bike counters across the city, enabling users to visualize trends, filter by stations/arrondissements, and analyze traffic patterns.

---

## 📖 Description

The Paris Bike App allows users to:
- Visualize bike counts over time (daily, monthly, yearly).
- Filter traffic data by specific bike stations or arrondissements.
- Explore patterns using a **heatmap** (day of week × hour of day).
- Gain insights into urban mobility and cycling adoption in Paris.

This project demonstrates how to combine **data science**, **Streamlit** for visualization, and **Docker** for reproducibility.

---

## 🛠️ Features

- 📊 **Time-series plots** of bike usage.
- 🗺️ **Geographic filtering** by station/arrondissement.
- 🔥 **Heatmap visualization** for traffic intensity.
- ✅ **Unit tests** for data loading and filtering functions.
- 🔄 **CI pipeline** with GitHub Actions to ensure code quality.

---

## 🖼️ Visuals

Example heatmap of bike traffic by day of week and hour of day:

*<img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/bf28e1d9-add9-421c-82f2-d8251a10c9f7" />


---

## ⚡ Installation

Clone the repository:

```bash
git clone https://github.com/mamounjamai/paris-bike-app.git
cd paris-bike-app
Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py
```

🐳 Run with Docker

Build the image:

docker build -t paris-bike-app .


Run the container:

docker run -p 8501:8501 paris-bike-app


Then open http://localhost:8501
 in your browser.

🧪 Running Tests

This project uses pytest for testing.

Run all tests with:

pytest -v


Tests cover:

Data loading from Parquet files.

Filtering functions.

CI is set up with GitHub Actions to run tests automatically on each push.

📌 Roadmap

Add predictive models for bike usage.

Deploy the app online (Streamlit Cloud or Heroku).

Extend visualizations with weather and traffic correlations.

🙌 Contributing

Contributions are welcome!

Fork the repository.

Create a new branch.

Commit your changes and open a pull request.

👤 Authors and Acknowledgments

Developed by Mamoun Jamai

📄 License

This project is licensed under the MIT License – feel free to use and modify it.

