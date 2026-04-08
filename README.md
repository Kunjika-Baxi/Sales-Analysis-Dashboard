# Sales Analysis Dashboard

## Overview
This project is a **Streamlit dashboard** built in Python to analyze a large sales dataset (~5 million rows, ~595 MB).  
It provides interactive visualizations and KPIs for profit trends, product performance, and geographic distribution.

---

## Features
- **Filters**: Select shipment year to dynamically update analysis.  
- **KPIs**: Average profit, maximum profit, top region, top country, and product driving profit.  
- **Visualizations**:
  - Product‑wise profit distribution (bar chart)  
  - Shipment profit trend (line chart)  
  - Profit category distribution (pie chart)  
  - Country‑wise average profit (choropleth map)  
- **Tabs**: Organized into Products, Shipments, Categorical Distribution, and GeoMaps.  

---

## Dataset
- Source: Internal dataset uploaded to Google Drive.  
- Size: ~595 MB, ~5,000,000 rows.  
- Columns include: `Region`, `Country`, `Item Type`, `Order Date`, `Ship Date`, `Total Profit`, etc.  
- For deployment, a **sample dataset** is used to keep the app responsive.  
- Full dataset is available [here](https://drive.google.com/drive/folders/1uRHzyAVkLlKv7hyGr1ln5vCc_MF3GrsH).

---

## Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/yourusername/sales-analysis-dashboard.git
cd sales-analysis-dashboard
pip install -r requirements.txt

streamlit run app.py
