# JSON API for checking date overlap

## API Endpoint: /api/isOverlay

Request: A POST request with a JSON payload containing two date ranges. Each date range is represented by an object with a start and an end property, both in the format of YYYY-MM-DD HH:MM:SS.

Response: a JSON format, including the two date ranges provided in the request, as well as a boolean overlap property that indicates whether the two date ranges overlap or not.

If the two date ranges overlap, the value of overlap will be true. If they do not overlap, the value of overlap will be false.

### Request Method: POST

#### Request Payload:

```
{
  "range1": {
    "start": "2023-01-01 00:00:00",
    "end": "2023-01-01 11:59:59"
  },
  "range2": {
    "start": "2023-01-01 08:00:00",
    "end": "2023-01-01 23:59:59"
  }
}
```


#### Response Payload:

```
{
  "range1": {
    "start": "2023-01-01 00:00:00",
    "end": "2023-01-01 11:59:59"
  },
  "range2": {
    "start": "2023-01-01 08:00:00",
    "end": "2023-01-01 23:59:59"
  },
  "overlap": true
}
```

## Installation

* Clone the repository to your local machine:

	```git clone https://github.com/yunzhaoli/Avalara_homework.git```
* Install the required dependencies:

	```pip install -r requirements.txt```

## Usage

* Start the server by running:

	```python api.py```
* The server will now be running on http://localhost:5000.
* To check if two date ranges overlap, send a POST request to the /api/isOverlap endpoint with the following JSON payload:
	
	``` 
	{
	      "range1": {
	          "start": "2023-01-01 00:00:00",
	          "end": "2023-01-01 11:59:59"
	      },
	      "range2": {
	          "start": "2023-01-01 08:00:00",
	          "end": "2023-01-01 23:59:59"
	      }
	 }
	
	```
	    
The response will be in JSON format and will contain an "overlap" field with a boolean value indicating whether the date ranges overlap.
* To run the tests, simply run:

	```python -m unittest discover -v```

## Docker

You can also run the API in a Docker container. To do so:

* Build the Docker image:

	```docker build -t <image_name> .```
* Run the Docker container:

	```docker run --name <container_name> <image_name>```
	
	This will start the container and run the API inside it.
* Or to run the tests in the Docker container:

	```docker run --name <container_name> <image_name> python -m unittest discover -v```

## CI
A Jenkins configure file is also provided for building container image and running unit tests.
