# utils.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def save_to_excel(data, filename="data/books.xlsx"):
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

def visualize_prices(data):
    if not data:
        return

    df = pd.DataFrame(data)
    plt.figure(figsize=(10, 5))
    sns.histplot(df['price'], bins=10, kde=True)
    plt.title("Price Distribution of Search Results")
    plt.xlabel("Price")
    plt.ylabel("Count")
    os.makedirs("static", exist_ok=True)
    plt.savefig("static/price_plot.png")
    plt.close()


