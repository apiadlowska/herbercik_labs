from flask import Flask, render_template_string, request

app = Flask(__name__)

# dane: lekcje i quizy
lessons = {
    "budowa-atomu": {
        "title": "Budowa atomu",
        "content": """Każdy atom składa się z jądra (protony i neutrony) oraz elektronów krążących wokół niego.
        
Ważne liczby:
- Z — liczba atomowa (liczba protonów).
- A — liczba masowa (protony + neutrony).
- N — liczba neutronów = A - Z.

Przykład: 23Na → Z=11, A=23, N=12"""
    },
    "izotopy": {
        "title": "Izotopy",
        "content": """Izotopy to odmiany tego samego pierwiastka o tej samej liczbie protonów (Z),
ale różnej liczbie neutronów (N).

Przykład: 12C, 13C, 14C."""
    }
}

quiz = [
    {"q": "Która liczba atomowa odpowiada tlenowi?", "a": ["6", "7", "8", "16"], "correct": 2},
    {"q": "Izotopy różnią się liczbą...", "a": ["Protonów", "Neutronów", "Elektronów", "Powłok"], "correct": 1},
]

# szablon HTML
template = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>📘 Nauka chemii</title>
</head>
<body style="font-family: Arial; background: #f4f4f4; padding: 20px;">
  <h1>🔬 Nauka chemii</h1>
  <nav>
    <a href="/">Strona główna</a> |
    <a href="/lekcje">Lekcje</a> |
    <a href="/quiz">Quiz</a>
  </nav>
  <hr>
  {{ content|safe }}
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(template, content="<h2>Witaj!</h2><p>Wybierz lekcję lub quiz.</p>")

@app.route("/lekcje")
def show_lessons():
    links = "".join([f"<li><a href='/lekcja/{lid}'>{l['title']}</a></li>" for lid, l in lessons.items()])
    return render_template_string(template, content=f"<h2>Lekcje</h2><ul>{links}</ul>")

@app.route("/lekcja/<lid>")
def lesson(lid):
    lesson = lessons.get(lid, {"title": "Nie znaleziono", "content": ""})
    return render_template_string(template, content=f"<h2>{lesson['title']}</h2><p>{lesson['content']}</p>")

@app.route("/quiz", methods=["GET", "POST"])
def run_quiz():
    if request.method == "POST":
        score = 0
        for i, q in enumerate(quiz):
            if str(q["correct"]) == request.form.get(f"q{i}"):
                score += 1
        return render_template_string(template, content=f"<h2>Wynik quizu</h2><p>Twój wynik: {score}/{len(quiz)}</p><a href='/quiz'>Spróbuj ponownie</a>")
    
    form = "<form method='post'>"
    for i, q in enumerate(quiz):
        form += f"<p><b>{q['q']}</b><br>"
        for j, ans in enumerate(q["a"]):
            form += f"<label><input type='radio' name='q{i}' value='{j}'> {ans}</label><br>"
        form += "</p>"
    form += "<button type='submit'>Sprawdź</button></form>"
    return render_template_string(template, content=form)

if __name__ == "__main__":
    app.run(debug=True)
