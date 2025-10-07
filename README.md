# Student CRUD Python Project

A simple **menu-driven CRUD application** in Python using **MySQL**.  
Allows you to **Create, Read, Update, and Delete student records**.

## Features
- Add a new student record
- View all student records
- Update student details (name, course, marks)
- Delete a student record
- Exit the program

## Technologies Used
- Python 3.x
- MySQL
- mysql-connector-python

## Folder Structure
├── main.py # Menu-driven program
├── stu_crud.py # CRUD functions
├── db_config.py # Database connection setup
├── README.md # Project documentation
└── .gitignore # Ignore unnecessary files


## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/madhura276/student-crud-python.git
cd student-crud-python

2. Install required Python package:
...bash
pip install mysql-connector-python

3. Create the database and table in MySQL:
...sql
CREATE DATABASE IF NOT EXISTS pythondb;
USE pythondb;

CREATE TABLE IF NOT EXISTS student_info (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    course VARCHAR(50),
    marks INT
);

4. Run the program:
...bash
python main.py


## Run in VS Code

You can easily run this project in **Visual Studio Code**:

1. Open VS Code.
2. Go to **File → Open Folder** and select this project folder.
3. Open the terminal in VS Code (**Ctrl + `**).
4. Make sure Python is installed and accessible:
```bash
python --version

5. Install MySQL connector if not installed:
...bash
pip install mysql-connector-python

6. Ensure your MySQL database and table exist (as mentioned above).
7. Run the program:
...bash
python main.py

8. Follow the menu in the terminal to perform CRUD operations on student records.

---

✅ This tells anyone exactly **how to run your project in VS Code**, step by step.  

If you want, I can **combine everything** into a **full final `README.md`** including `.gitignore`, setup, usage, and VS Code instructions — ready to upload to GitHub.  

Do you want me to do that?





