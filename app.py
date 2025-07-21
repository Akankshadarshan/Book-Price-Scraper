# app.py
from flask import Flask, render_template, request
from scraper import scrape_books  # ✅ This must match the function name in scraper.py
from utils import save_to_excel, visualize_prices

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    books = []
    query = ""
    if request.method == "POST":
        query = request.form["query"]
        books = scrape_books(query)
        if books:
            save_to_excel(books)
            visualize_prices(books)
    return render_template("index.html", books=books, query=query)

if __name__ == "__main__":
    app.run(debug=True)

