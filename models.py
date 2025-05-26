from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    chosen = db.Column(db.Boolean, default=False)

def init_db():
    db.create_all()
    if not Player.query.first():
        players = [
            Player(name="Alice", image="https://example.com/alice.jpg"),
            Player(name="Bob", image="https://example.com/bob.jpg"),
        ]
        db.session.bulk_save_objects(players)
        db.session.commit()
