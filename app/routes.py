from flask import Blueprint, render_template, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/api/animes', methods=['GET'])
def get_animes():
    # Replace with logic to fetch anime data from database or API
    animes = [
        {'title': 'One Piece', 'genre': 'Shounen', 'episodes': 1000},
        {'title': 'Attack on Titan', 'genre': 'Action', 'episodes': 75},
        {'title': 'Naruto', 'genre': 'Shounen', 'episodes': 500},
    ]
    return jsonify(animes)

# Add more routes as needed

