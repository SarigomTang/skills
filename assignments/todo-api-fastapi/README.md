# 📘 Assignment: To-Do API with FastAPI

## 🎯 Objective

Learn how to build a simple REST API with FastAPI by creating a task manager that stores to-do items and returns JSON data.

## 📝 Tasks

### 🛠️ Create the Task API

#### Description
Build a basic API that stores a list of tasks and exposes routes to read and add tasks.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Define a `GET /tasks` route that returns all stored tasks in JSON
- Define a `POST /tasks` route that accepts a new task from the request body
- Store tasks in memory while the server is running
- Return a clear JSON response after creating a task

### 🛠️ Add Task Details

#### Description
Expand the API so each task includes a title and whether it is complete.

#### Requirements
Completed program should:

- Accept task data such as `title` and `completed`
- Return a task dictionary with those fields in the response
- Prevent empty or invalid task titles from being added
- Display all tasks in a readable JSON format

### 🛠️ Improve the API with Updates and Deletion

#### Description
Make the task manager more useful by allowing tasks to be updated or removed.

#### Requirements
Completed program should:

- Add a `PUT /tasks/{task_id}` route to update a task
- Add a `DELETE /tasks/{task_id}` route to remove a task
- Return a `404` response when a task is not found
- Keep the response messages clear and easy to understand
