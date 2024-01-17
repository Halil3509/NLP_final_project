from flask import Flask, request, jsonify
from flask_cors import CORS

from legacy_punct import LegacyPunctuation
from disorder_detection import DisorderDetection

app = Flask(__name__)
cors = CORS(app)

# Define a dictionary to store data (in-memory database for this example)
data = {}


@app.route('/ai/legacy_audio_temp', methods=['POST'])
def get_audio_temp_legacy():

    data = request.json
    text = data.get("text")

    legacy_punct_model = LegacyPunctuation()
    puncted_text = legacy_punct_model.add_punct(text)


    disorder_detection_class = DisorderDetection(puncted_text)
    total_disorder_json = disorder_detection_class.run_disorder_detection()
    # print("Total disorder detection: ", total_disorder_json)

    current_sum = sum(total_disorder_json.values())

    # Normalize the values to ensure the sum is 100
    normalized_dict = {key: round((value / current_sum) * 100, 2) for key, value in total_disorder_json.items()}


    return jsonify({"message": "işlem başarılı",
                    "total_disorder_json": normalized_dict})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)