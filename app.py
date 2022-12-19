from flaskext.markdown import Markdown
from unittest import result
from flask import Flask, render_template, url_for, request, render_template
from markdown import markdown
import spacy
from spacy import displacy, load
nlp = spacy.load("C:/Users/vindo/PROJECT/model-best")
colors = {"ORGANISASI": "#FF6666", "NAMA_ORANG": "#FCFF7D", "HARI": "#58E0A7", "TANGGAL": "#9BA3EB", "HARGA_NAIK": "#FFCACA",
          "HARGA_TURUN": "#C3F8FF", "PRODUK_PERTANIAN": "#FFE9C5", "PENYAKIT": "#FB8D62", "LOKASI": "#9E7676", "MUSIM": "#CFD2CF"}
options = {"colors": colors}

app = Flask(__name__)
Markdown(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ekstrak")
def ekstrak():
    return render_template("ekstraksi.html")


@app.route("/tentang")
def tentang():
    return render_template("tentang.html")

# @app.route('/result')
# def resultt():
#    return render_template('result.html')


@app.route('/hasil', methods=["GET", "POST"])
def resultt():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        docx = nlp(rawtext)
        html = displacy.render(docx, style='ent', options=options)
        result = html

    return render_template('hasil.html', rawtext=rawtext, result=result)


if __name__ == "__main__":
    app.run(debug=True)
