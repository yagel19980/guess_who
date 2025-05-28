from flask import Flask, jsonify, request, abort
from models import db, Player, init_db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/players", methods=["GET"])
def get_players():
    players = Player.query.all()
    return jsonify([{
        "name": p.name,
        "id": p.id,
        "image": p.image
    } for p in players])

@app.route("/choose/<int:player_id>", methods=["PUT"])
def choose_player(player_id):
    player = Player.query.get(player_id)
    if not player:
        abort(404, "Player not found")
    player.chosen = True
    db.session.commit()
    return jsonify({"message": "Player chosen"}), 200

@app.route("/chosen", methods=["GET"])
def get_chosen():
    player = Player.query.filter_by(chosen=True).first()
    if not player:
        return jsonify({"message": "No player has been chosen yet"}), 404
    return jsonify({
        "id": player.id,
        "name": player.name,
        "image": player.image
    })

if __name__ == "__main__":
    with app.app_context():
        init_db()
    app.run(debug=True, use_reloader=False)
    #use this if you want to reload automatically
    #app.run(debug=True)
