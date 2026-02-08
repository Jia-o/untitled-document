from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
# This line is CRITICAL. It allows your index.html to talk to this script.
CORS(app) 

CATEGORY_MAP = {
    "education": "objects",
    "recreational": "activities",
    "social": "smileys-and-people",
    "diy": "objects",
    "charity": "symbols",
    "cooking": "food-and-drink",
    "relaxation": "smileys-and-people",
    "music": "symbols",
    "busywork": "activities"
}

EXCUSE_MAPPING = {
    "education": "college",
    "recreational": "funny",
    "social": "party",
    "diy": "unbelievable",
    "charity": "family",
    "cooking": "funny",
    "relaxation": "funny",
    "music": "gaming",
    "busywork": "developers"
}

@app.route('/get-magic')
def get_magic():
    try:
        # Fetch activity
        activity_res = requests.get('https://bored-api.appbrewery.com/random', timeout=5).json()
        
        # Determine Category
        raw_type = activity_res.get('type', 'recreational')
        category = CATEGORY_MAP.get(raw_type, "activities")
        
        # Fetch Emoji
        emoji_res = requests.get(f'https://emojihub.yurace.pro/api/random/category/{category}', timeout=5).json()
        
        return jsonify({
            "text": activity_res['activity'],
            "emoji": emoji_res['htmlCode'][0]
        })
    except Exception as e:
        return jsonify({"text": "Thank a friend.", "emoji": "&#10024;"}), 500

@app.route('/get-excuse')
def get_excuse():
    try:
        # Fetch an unbelievable excuse
        response = requests.get('https://excuser-three.vercel.app/v1/excuse/unbelievable', timeout=5)
        data = response.json()
        # The API returns a list, e.g., [{"excuse": "...", ...}]
        return jsonify({"excuse": data[0]['excuse']})
    except Exception as e:
        return jsonify({"excuse": "My pet dragon ate my motivation."}), 200

if __name__ == '__main__':
    # Using port 5000 by default
    app.run(port=5000, debug=True)