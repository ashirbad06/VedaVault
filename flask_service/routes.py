from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock service to return services information
@app.route('/api/services', methods=['GET'])
def get_services():
    services = [
        {'plan': 'Basic', 'description': 'Includes fundamental strategies and access to resources.', 'price': 10},
        {'plan': 'Standard', 'description': 'Includes advanced strategies and personalized services.', 'price': 20},
        {'plan': 'Premium', 'description': 'Complete access to all services with 24/7 support.', 'price': 50}
    ]
    return jsonify(services)

# Mock service for contact form submission
@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    if data:
        return jsonify({'message': f"Thank you {data['name']}, we have received your message."}), 200
    return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Flask server will run on port 5001
