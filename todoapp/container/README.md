# To Do App with Django

## Description
### 1. Views/Function
#### a. Add new task (url='/add')
#### b. Mark task as done (url='/complete/task_id')
<<<<<<< HEAD
#### c. Delete task url=('/delete/task_id')
=======
#### c. Delete task (url='/delete/task_id')
>>>>>>> 5babb2393363c43670442631632ec55300f4a7ff

### 2. Model, Entry data for task
#### a. "Title", string (required(frontend))
#### b. "Description", string
#### c. "Start date" & "Due date", date (required(frontend))
#### d. "Category(label)", string
#### e. "Completed", boolean

### 3. Testing
#### a. Model tests 
- ToDoListTests
#### b. Views tests
- StartPageTests
- AddTaskPageTests

## Run the development code - Steps
### 1. Install required frameworks
#### pip install -r requirements.txt

### 2. Database Initializing (sqlite)
#### a. ...path> py manage.py makemigrations toDoApp
#### b. ...path> py manage.py migrate

### 3. Admin Initializing
#### py manage.py createsuperuser

### 4. Run server
#### py manage.py runserver
