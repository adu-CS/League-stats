from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Home Page route
@app.route("/")
def home():
    return render_template("home.html")

# Route to form used to add a new player to the database
@app.route("/enternew")
def enternew():
    return render_template("player.html")

# Route to add a new record (INSERT) player data to the database
@app.route("/addrec", methods=['POST'])
def addrec():
    if request.method == 'POST':
        try:
            name = request.form['name']
            runs = request.form['runs']
            avg = request.form['avg']
            sr = request.form['sr']

            with sqlite3.connect('database.sqlite') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Players (name, runs, avg, sr) VALUES (?, ?, ?, ?)", (name, runs, avg, sr))
                con.commit()
                msg = "Record successfully added to database"
        except:
            con.rollback()
            msg = "Error in the INSERT"

        finally:
            con.close()
            return render_template('result.html', msg=msg)

# Route to SELECT all data from the Players table and display in a table
@app.route('/list')
def list():
    con = sqlite3.connect("database.sqlite")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT rowid, * FROM Players")

    rows = cur.fetchall()
    con.close()
    return render_template("list.html", rows=rows)

# Route that will SELECT a specific row in the database then load an Edit form 
@app.route("/edit", methods=['POST','GET'])
def edit():
    if request.method == 'POST':
        try:
            id = request.form['id']
            with sqlite3.connect("database.sqlite") as con:
                con.row_factory = sqlite3.Row
                cur = con.cursor()
                cur.execute("SELECT rowid, * FROM Players WHERE rowid = ?", (id,))
                rows = cur.fetchall()
        except:
            rows = None
        return render_template("edit.html", rows=rows)

# Route used to execute the UPDATE statement on a specific record in the database
@app.route("/editrec", methods=['POST'])
def editrec():
    if request.method == 'POST':
        try:
            rowid = request.form['rowid']
            name = request.form['name']
            runs = request.form['runs']
            avg = request.form['avg']
            sr = request.form['sr']

            with sqlite3.connect('database.sqlite') as con:
                cur = con.cursor()
                cur.execute("UPDATE Players SET name=?, runs=?, avg=?, sr=? WHERE rowid=?", (name, runs, avg, sr, rowid))
                con.commit()
                msg = "Record successfully edited in the database"
        except:
            con.rollback()
            msg = "Error in the Edit"

        finally:
            con.close()
            return render_template('result.html', msg=msg)

# Route used to DELETE a specific record in the database    
@app.route("/delete", methods=['POST'])
def delete():
    if request.method == 'POST':
        try:
            rowid = request.form['id']
            with sqlite3.connect('database.sqlite') as con:
                cur = con.cursor()
                cur.execute("DELETE FROM Players WHERE rowid=?", (rowid,))
                con.commit()
                msg = "Record successfully deleted from the database"
        except:
            con.rollback()
            msg = "Error in the DELETE"

        finally:
            con.close()
            return render_template('result.html', msg=msg)

# Route to form used to add a new team to the database
@app.route("/enternewteam")
def enternewteam():
    return render_template("team.html")

# Route to add a new record (INSERT) team data to the database
@app.route("/addteamrec", methods=['POST'])
def addteamrec():
    if request.method == 'POST':
        try:
            name = request.form['name']
            team = request.form['team']

            with sqlite3.connect('database.sqlite') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Teams (name, team) VALUES (?, ?)", (name, team))
                con.commit()
                msg = "Record successfully added to database"
        except:
            con.rollback()
            msg = "Error in the INSERT"

        finally:
            con.close()
            return render_template('result.html', msg=msg)

# Route to SELECT all data from the Teams table and display in a table
@app.route('/listteams')
def listteams():
    con = sqlite3.connect("database.sqlite")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT rowid, * FROM Teams")

    rows = cur.fetchall()
    con.close()
    return render_template("listteams.html", rows=rows)

# Route that will SELECT a specific row in the Teams table then load an Edit form 
@app.route("/editteam", methods=['POST','GET'])
def editteam():
    if request.method == 'POST':
        try:
            id = request.form['id']
            with sqlite3.connect("database.sqlite") as con:
                con.row_factory = sqlite3.Row
                cur = con.cursor()
                cur.execute("SELECT rowid, * FROM Teams WHERE rowid = ?", (id,))
                rows = cur.fetchall()
        except:
            rows = None
        return render_template("editteam.html", rows=rows)

# Route used to execute the UPDATE statement on a specific record in the Teams table
@app.route("/editteamrec", methods=['POST'])
def editteamrec():
    if request.method == 'POST':
        try:
            rowid = request.form['rowid']
            name = request.form['name']
            team = request.form['team']

            with sqlite3.connect('database.sqlite') as con:
                cur = con.cursor()
                cur.execute("UPDATE Teams SET name=?, team=? WHERE rowid=?", (name, team, rowid))
                con.commit()
                msg = "Record successfully edited in the database"
        except:
            con.rollback()
            msg = "Error in the Edit"

        finally:
            con.close()
            return render_template('result.html', msg=msg)

# Route used to DELETE a specific record in the Teams table    
@app.route("/deleteteam", methods=['POST'])
def deleteteam():
    if request.method == 'POST':
        try:
            rowid = request.form['id']
            with sqlite3.connect('database.sqlite') as con:
                cur = con.cursor()
                cur.execute("DELETE FROM Teams WHERE rowid=?", (rowid,))
                con.commit()
                msg = "Record successfully deleted from the database"
        except:
            con.rollback()
            msg = "Error in the DELETE"

        finally:
            con.close()
            return render_template('result.html', msg=msg)


if __name__ == '__main__':
    app.run(debug=True)
