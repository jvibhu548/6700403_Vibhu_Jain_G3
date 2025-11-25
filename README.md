# 📊 Crypto Analysis Project

This project downloads Bitcoin and Ethereum historical price data using **Python (yfinance)**, stores it in a **data folder**, cleans it later, and then you can use it for **Power BI visualizations**.

---

## 📁 Project Structure

```
Minor Project1/
│
├── crypto_analysis.py      # Python script to download data
├── data/                   # Folder where CSV files will be saved
├── cleaned/                # For cleaned data (future steps)
```

---

## ⚙️ Requirements

Install required Python packages:

```bash
pip install yfinance pandas
```

---

## 🐍 Python Script (crypto_analysis.py)

This script downloads Bitcoin and Ethereum daily price data from **2020-01-01** to today.

```python
import yfinance as yf
import pandas as pd

# Download Bitcoin Data
btc = yf.download("BTC-USD", start="2020-01-01")

# Download Ethereum Data
eath = yf.download("ETH-USD", start="2020-01-01")

# Save inside data folder
btc.to_csv("data/BTC-USD.csv")
eath.to_csv("data/ETH-USD.csv")

print("Dataset downloaded")
```

---

## 📥 Steps to Run the Project

### ✅ Step 1: Create Folder Structure

Make sure these folders exist:

```
Minor Project1/
    data/
    cleaned/
```

If **data** folder does not exist, create it manually.

---

### ✅ Step 2: Run the Script

Open VS Code terminal inside project folder:

```bash
python crypto_analysis.py
```

If successful, you will see:

```
Dataset downloaded
```

And inside **data/** folder, you will get:

```
BTC-USD.csv
ETH-USD.csv
```

---

## 📊 Next Steps (Power BI)

1. Open **Power BI Desktop**
2. Click **Get Data → Text/CSV**
3. Select:

   * `data/BTC-USD.csv`
   * `data/ETH-USD.csv`
4. Load both datasets
5. Create visuals like:

   * Price line charts
   * Volume charts
   * BTC vs ETH comparison

---

## 💡 Notes

* Keep internet on while downloading data
* If you change folder names, update the script paths
* CSV files will update every time you run the script

---

## ❤️ Need Help?

If you get any error, send the screenshot — I’ll fix it immediately!
