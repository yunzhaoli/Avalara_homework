from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)
HTTP_BAD_REQUEST = 400
HTTP_OK = 200
SERVICE_PORT = 5000

@app.route('/api/isOverlap', methods=['POST'])
def checkOverlap():
    app.logger.info("trigger isOverlap api")
    # if the request is not json, return error automatically by flask
    data = request.get_json()

    # Check if the request is valid
    if 'range1' not in data or 'range2' not in data:
        app.logger.error("Invalid request for missing range")
        return jsonify({"error": "Invalid request for missing range"}), HTTP_BAD_REQUEST 

    if 'start' not in data['range1'] or 'end' not in data['range1']:
        app.logger.error("Invalid request for range1")
        return jsonify({"error": "Invalid request for range1"}), HTTP_BAD_REQUEST 
    
    if 'start' not in data['range2'] or 'end' not in data['range2']:
        app.logger.error("Invalid request for range2")
        return jsonify({"error": "Invalid request for range2"}), HTTP_BAD_REQUEST
    
    try:
        range1_start = datetime.strptime(data['range1']['start'], '%Y-%m-%d %H:%M:%S')
        range1_end = datetime.strptime(data['range1']['end'], '%Y-%m-%d %H:%M:%S')
        range2_start = datetime.strptime(data['range2']['start'], '%Y-%m-%d %H:%M:%S')
        range2_end = datetime.strptime(data['range2']['end'], '%Y-%m-%d %H:%M:%S')
    except ValueError:
        app.logger.error("Invalid request for time format")
        return jsonify({"error": "Invalid request for time format"}), HTTP_BAD_REQUEST 


    # Check if the range is valid
    if range1_start >= range1_end:
        app.logger.error("Invalid request for range1")
        return jsonify({"error": "Invalid request for range1"}), HTTP_BAD_REQUEST 
    if range2_start >= range2_end:
        app.logger.error("Invalid request for range2")
        return jsonify({"error": "Invalid request for range2"}), HTTP_BAD_REQUEST 

    # Check if the range is overlap 
    # by comparing one range's start time and the other range's end time
    overlap = True
    if range1_end <= range2_start:
        overlap = False

    if range2_end <= range1_start:
        overlap = False
    
    # return the result
    response = {
        "range1": {
            "start": range1_start,
            "end": range1_end
        },
        "range2": {
            "start": range2_start,
            "end": range2_end
        },
        "overlap": overlap
    }

    app.logger.info(f"valid request {overlap}, send 200 OK back to client")
    return jsonify(response, HTTP_OK)

if __name__ == '__main__':
    app.logger.info("start isOverlap app")
    app.run(host='0.0.0.0', port=SERVICE_PORT, debug=True)


