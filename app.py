from flask import Flask, render_template_string
import csv
import os

app = Flask(__name__)

CSV_PATH = os.path.join(os.path.dirname(__file__), "data", "seu_dataset.csv")

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Dados - Emprego x IA</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { margin-bottom: 10px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ccc; padding: 6px 8px; text-align: left; }
        th { background-color: #eee; }
    </style>
</head>
<body>
    <h1>Emprego / Desemprego relacionado à IA</h1>
    <p>Fonte: {{ csv_name }}</p>
    <table>
        <thead>
            <tr>
            {% for h in header %}
                <th>{{ h }}</th>
            {% endfor %}
            </tr>
        </thead>
        <tbody>
        {% for row in rows %}
            <tr>
            {% for cell in row %}
                <td>{{ cell }}</td>
            {% endfor %}
            </tr>
        {% endfor %}
        </tbody>
    </table>
</body>
</html>
"""

@app.route("/")
def index():
    rows = []
    header = []

    # Ajuste o delimiter se seu CSV usar ';' em vez de ','
    with open(CSV_PATH, newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')  # troque para ',' se for o caso
        for i, row in enumerate(reader):
            if i == 0:
                header = row
            else:
                rows.append(row)

    return render_template_string(
        HTML_TEMPLATE,
        header=header,
        rows=rows,
        csv_name=os.path.basename(CSV_PATH)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
