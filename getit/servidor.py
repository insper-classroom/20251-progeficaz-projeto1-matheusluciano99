from flask import Flask, render_template_string, request, redirect, url_for
import sqlite3 as sql
import views


app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = "static"


@app.route("/")
def index():
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from notes")
    data = cur.fetchall()

    return render_template_string(views.index(data), data=data)


@app.route("/submit", methods=["POST"])
def submit_form():
    title = request.form.get("Title")
    description = request.form.get("Description")
    con = sql.connect("db_web.db")
    cur = con.cursor()
    cur.execute(
        "insert into notes(Title, Description) values (?,?)", (title, description)
    )
    con.commit()
    return redirect(url_for("index"))


@app.route("/delete/<string:id>", methods=["GET"])
def delete_note(id):
    con = sql.connect("db_web.db")
    cur = con.cursor()
    cur.execute("delete from notes where id = ?", (id,))
    con.commit()
    return redirect("/")


@app.route("/update/<string:id>", methods=["POST", "GET"])
def edit_note(id):
    if request.method == "POST":
        title = request.form.get("Title")
        description = request.form.get("Description")
        con = sql.connect("db_web.db")
        cur = con.cursor()
        cur.execute(
            "update notes set Title=?,Description=? where Id=?",
            (title, description, id),
        )
        con.commit()
        return redirect(url_for("index"))

    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from notes where Id=?", (id,))
    note = cur.fetchone()

    return render_template_string(views.edit_template(note))


if __name__ == "__main__":
    app.run(debug=True)
