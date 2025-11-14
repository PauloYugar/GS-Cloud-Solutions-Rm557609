from flask import Flask, render_template_string
import pandas as pd
import os

app = Flask(__name__)

CSV_PATH = os.path.join(os.path.dirname(__file__), "data", "gs_dataset.csv")

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Emprego x IA - CSV</title>
</head>
<body>
    <h1>Dados de Emprego / IA</h1>
    {{ table|safe }}
</body>
</html>
"""

@app.route("/")
def index():
    df = pd.read_csv(CSV_PATH)
    return render_template_string(HTML_TEMPLATE, table=df.to_html(index=False))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
