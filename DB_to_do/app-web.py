from flask import Flask
import dao

app = Flask(__name__)


@app.route('/')
def listTasks():
    tasks = dao.readTasks()
    output = "<table class='right'>"

    for row in tasks:
        output += f'<tr><th>{row[0]:6d}</th> <th>{row[1]:<30s}</th> <th>{row[2]:5}</th>  <th>{row[3]}</th>   <th>{row[4]}</th>   <th>{row[5]}</th></tr>'

    output += "</table>"
    return output


@app.route('/delete/<int:id>')
def delete(id):
    dao.removeTask(id)
    return f"""
            <meta http-equiv="refresh" content=2;URL='/'" /> 
            Task {id} deleted!!!"""


@app.route('/setdone/<int:id>')
def setDone(id):
    dao.updateTask(id, title=None, done=True)
    return f"""
            <meta http-equiv="refresh" content=2;URL='/'" /> 
            Task {id} set DONE"""
