#Alumna: Gabriela Beatriz Solorzano Nuila 

from asyncio import all_tasks
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask

app = Flask(_name_)
# Database configurations

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
# sqlite

db = SQLAlchemy(app)
mars = Marshmallow(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    check = db.Column(db.Boolean)
    creado = db.Column(db.datetime)

    def _init_(self, name, check, creado):
        self.name = name
        self.check = check
        self.creado = creado

    def _repr_(self):
        return '<Task %s>' % self.name
    # Create Database


class TaskSchema(mars.Schema):
    class Meta:
        fileds = ('id', 'name', 'check', 'creado')


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

all_tasks = Task.query.all()
print(all_tasks)
db.create_all()

new_task = Task(name='Inserte los datos de la Tabla de datos', check=False)
db.session.add(new_task)
db.session.commit()

del_task = Task.query.get_or_404(2)
print(del_task)


Update_task = Task.query.get_or_404(3)
Update_task.name = "Task Name: "
db.session.commit()
if _name_ == '_main_':
    app.run(debug=True)