PROBLEM STATEMENT
![image](https://github.com/PrathamM16/Survey_Cloudurity/assets/121935421/eebb3422-178c-42b7-a237-8625f550cbd6)

Note :I have run this code inside virtual environment 

Main screen-![Screenshot 2024-06-07 170744](https://github.com/PrathamM16/Survey_Cloudurity/assets/121935421/2f0a406a-6000-427a-8b0a-344906caf72d)
When clicked on survey person can respond to the survey ![Screenshot 2024-06-07 170927](https://github.com/PrathamM16/Survey_Cloudurity/assets/121935421/111ce9a2-388f-4180-88dd-dbd000c83e01)
If Survey date has ended ![Screenshot 2024-06-07 170944](https://github.com/PrathamM16/Survey_Cloudurity/assets/121935421/1620b605-cc36-43b4-ac31-30dceb53278d)
If tried to login without registering ![Screenshot 2024-06-07 171044](https://github.com/PrathamM16/Survey_Cloudurity/assets/121935421/10c720e0-616a-43e5-bb5e-9a47e422e9ad)
After registering ![image](https://github.com/PrathamM16/Survey_Cloudurity/assets/121935421/8b4d2ba1-2e6b-4ad1-be42-a7ac446c468f)
Login now ![image](https://github.com/PrathamM16/Survey_Cloudurity/assets/121935421/b91fce5d-215f-4899-a698-d53ba3e501cb)
The interface gets changed to user profile where Create survey logout and responses can be seen ![Screenshot 2024-06-07 171322](https://github.com/PrathamM16/Survey_Cloudurity/assets/121935421/1564542f-ecc1-4983-9b85-6c52e566890c)
Form for creating a survey ![Screenshot 2024-06-07 171435](https://github.com/PrathamM16/Survey_Cloudurity/assets/121935421/42b2cfc2-f9b2-4025-9a91-3217e8dbb938)
Validation that minimum 5 question to 20 is done ![Screenshot 2024-06-07 171720](https://github.com/PrathamM16/Survey_Cloudurity/assets/121935421/1cb0ef4d-52e4-4750-aae2-c6c8f4f7f5c0)
After creating Techinal questions its visible on available survey ![Screenshot 2024-06-07 172036](https://github.com/PrathamM16/Survey_Cloudurity/assets/121935421/b30ab604-5a92-4678-83ee-d28a25e63f59)


For indeteail working of this  access it from command prompt and work 

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
**cd Survey_Cloudurity**

Set up the Flask environment variables:
**export FLASK_APP=app.py
export FLASK_ENV=development**

Initialize the database:
**flask db init
flask db migrate -m "Initial migration"
flask db upgrade**

Run the application:
**flask run**
**Access the application in your web browser at http://localhost:5000.**

YOUR ALLOWED TO CREATE A VIRTUAL ENVIRONMENT AND PERFORM THE CODING TASK
commands for creating virtual environment :

install Virtualenv (if not already installed):
**pip install virtualenv**

Navigate to Your Project Directory:
Open a terminal or command prompt and navigate to the directory where you want to create the virtual environment. For example:
**cd /path/to/your/project/directory**

Create a Virtual Environment:
Run the following command to create a virtual environment named venv:
virtualenv venv

If you're using Python 3 and want to specify the Python version:
**virtualenv -p python3 venv**


Activate the Virtual Environment:
On Windows:
**venv\Scripts\activate**

On macOS and Linux:
**source venv/bin/activate**

Verify Activation:
Once activated, the command prompt or terminal should show the name of the virtual environment at the beginning of each line.

Install Dependencies:
Now, you can install the necessary packages for your project using pip, and they will be isolated within the virtual environment.

Deactivate the Virtual Environment:
To deactivate the virtual environment and return to the global Python environment, simply run:
**deactivate**

Remember to activate the virtual environment every time you work on your project **use: venv\Scripts\activate**
