from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.dojo import Dojo, Ninja


@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('index.html', all_dojos = dojos)

# Adding a new dojo to the list
@app.route('/create/dojo', methods=["POST"])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')


@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {
        "id": dojo_id
    }
    return render_template('dojo.html', dojo=Dojo.get_dojo(data), ninjas=Ninja.get_ninjas(data))