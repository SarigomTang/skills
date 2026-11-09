# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to create a simple REST API using the FastAPI framework in Python. Students will define routes, accept request data, and return JSON responses.

## 📝 Tasks

### 🛠️ Create Your First API

#### Description
Build a basic FastAPI application that serves a simple greeting and exposes a route that returns data for a specific item.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Define a `GET /` route that returns a welcome message in JSON
- Define a `GET /items/{item_id}` route that returns the item ID and a message
- Run the app with Uvicorn so it can be served locally

### 🛠️ Add Data and POST Requests

#### Description
Expand the application so it can accept incoming JSON data and save it in memory for later retrieval.

#### Requirements
Completed program should:

- Define a `POST /items` route that accepts JSON input
- Validate that required fields are present before storing the data
- Return the created item as JSON with a successful response status
- Add a `GET /items` route that lists all current items

### 🛠️ Improve the API with Validation and Error Handling

#### Description
Make the API more robust by handling invalid input and missing resources gracefully.

#### Requirements
Completed program should:

- Add a query parameter route such as `GET /items/search?q=...`
- Filter or search items based on user input
- Return a `404` response when an item is not found
- Use clear JSON messages for successful and failed requests

