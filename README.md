# JSON API for checking date overlap

## API Endpoint: /api/isOverlay

### Request: 
A POST request with a JSON payload containing two date ranges. Each date range contains a start and an end property, with the format of YYYY-MM-DD HH:MM:SS.

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


### Response: 
A JSON format, including the two date ranges provided in the request, as well as a boolean overlap property that indicates whether the two date ranges overlap or not.

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

### Result:
If the two date ranges overlap, the value of overlap will be true. If they do not overlap, the value of overlap will be false.

## Installation

* Clone the repository:

	```git clone https://github.com/yunzhaoli/Avalara_homework.git```

* Build and Install the package:

	```make```

## Usage

* Start the server:

	```make run```
	
	The server will now be running on http://localhost:5000.
	To check, send a POST request to the /api/isOverlap endpoint with the following JSON payload:
	
	
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
	    

* Run the tests:

	```make test```

## CI

### Docker

The API could also be run in a Docker container:

* Build the Docker image:

	```docker build -t <image_name> .```
* Run the Docker container:

	```docker run --name <container_name> <image_name>```
	
* Run the tests:

	```docker run --name <container_name> <image_name> python -m unittest discover -v```

### Jenkins

A Jenkins configure file is also provided for building container image and running unit tests through a pipeline.
