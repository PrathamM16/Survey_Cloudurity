PROBLEM STATEMENT
![image](https://github.com/PrathamM16/Survey_Cloudurity/assets/121935421/eebb3422-178c-42b7-a237-8625f550cbd6)



# Survey Cloudurity

Survey Cloudurity is a web application built with Flask for creating and conducting surveys.

## Features

- Create surveys with multiple-choice questions.
- Collect responses from participants.
- Analyze survey results with visualizations.


use this to install packages pip install Flask Flask-Migrate Flask-Script Flask-Login Flask-WTF SQLAlchemy


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/PrathamM16/Survey_Cloudurity.git
Install the required dependencies:


Usage
Navigate to the project directory:

cd Survey_Cloudurity
Set up the Flask environment variables:

export FLASK_APP=app.py
export FLASK_ENV=development
Initialize the database:

flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Run the application:

flask run
Access the application in your web browser at http://localhost:5000.



YOUR ALLOWED TO CREATE A VIRTUAL ENVIRONMENT AND PERFORM THE CODING TASK
commands for creating virtual environment :

install Virtualenv (if not already installed):
pip install virtualenv

Navigate to Your Project Directory:
Open a terminal or command prompt and navigate to the directory where you want to create the virtual environment. For example:
cd /path/to/your/project/directory

Create a Virtual Environment:
Run the following command to create a virtual environment named venv:
virtualenv venv

If you're using Python 3 and want to specify the Python version:
virtualenv -p python3 venv


Activate the Virtual Environment:
On Windows:
venv\Scripts\activate

On macOS and Linux:
source venv/bin/activate

Verify Activation:
Once activated, the command prompt or terminal should show the name of the virtual environment at the beginning of each line.

Install Dependencies:
Now, you can install the necessary packages for your project using pip, and they will be isolated within the virtual environment.

Deactivate the Virtual Environment:
To deactivate the virtual environment and return to the global Python environment, simply run:
deactivate

Remember to activate the virtual environment every time you work on your project use: venv\Scripts\activate
