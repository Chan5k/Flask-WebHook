from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

received_data = []

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    received_data.append(data)
    print(data)
    return jsonify({'status': 'success'}), 200

@app.route('/display', methods=['GET'])
def display():
    global received_data
    data_to_display = jsonify(received_data)
    received_data = []  # Clear the list
    return data_to_display

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
