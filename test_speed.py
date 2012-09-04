import cProfile
import flask
from flaskext.mongoobject import MongoObject

db = MongoObject()
app = flask.Flask(__name__)
TESTING = True


class TestModel(db.Model):
    __collection__ = "tests"


db.set_mapper(TestModel)

app.config['MONGODB_HOST'] = "mongodb://localhost:27017"
app.config['MONGODB_DATABASE'] = "testdb"
app.config['MONGODB_AUTOREF'] = True
app.config['TESTING'] = True
db.init_app(app)

def create_model(interval):
    for i in interval:
        model = TestModel({"test": {"name": "testing_{}".format(i)}})
        model.save()

def find_model(interval):
    for i in interval:
        TestModel.query.find({"test.name": "testing_{}".format(i)})


if __name__ == '__main__':
    interval = range(1000)
    cProfile.run('create_model(interval)')
    #old_version, for interval = 1000: 116059 function calls (114058 primitive calls) in 0.192-0.211 seconds

    cProfile.run('find_model(interval)')
    #old_version, for interval = 1000: 51003 function calls in 0.078-0.086 seconds




    db.clear()