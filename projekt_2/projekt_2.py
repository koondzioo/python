from flask import Flask, render_template, redirect, request

KOT = 0
PIES = 0
app = Flask(__name__)


@app.route('/update', methods=['POST'])
def result():
    global KOT, PIES
    if request.form['animal'] == 'KOT':
        KOT += 1
    else:
        PIES += 1
    return redirect('/result')


@app.route("/result")
def results():
    global KOT, PIES
    return render_template("result.html", koty=KOT, pies=PIES)


@app.route("/")
def main():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
