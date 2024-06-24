from config import db

# Creating db model for storing todos
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    desc = db.Column(db.String(100), unique=False, nullable=False)
    
    def to_json(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "desc" : self.desc
        }