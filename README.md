# AI Lotería 2024-2025
![google loteria gif](https://www.google.com/logos/doodles/2019/celebrating-loteria-6753651837108226.3-2xa.gif)

This project brings a new approach to the popular Latin American game Lotería. With using Python libraries that utilize convolutional neural networks and deep learning, Lotería can become fully automized. 


# Project Setup Instructions

This guide will walk you through setting up the backend and frontend of the project. For the backend, we'll skip the Docker setup for Mac users due to limitations, and instead focus on Docker for the frontend.

## Repository Setup
**Step 1:** Install [Git](https://git-scm.com/downloads) and install [VSCode](https://code.visualstudio.com/download)

Git needs to be installed on your system to be able to clone the repository and commit/push your changes.

VSCode is our recommended IDE, as our team has more familiarity with it. It has excellent functionality with Git Bash.

**Step 2:** Login to GitHub via terminal

Open a terminal (in VSCode via *Ctrl+Shift+`* or *Terminal->New Terminal* or on your system with Git Bash/Terminal) and run the following:
```
git config --global user.name "your_github_username"
git config --global user.email "your_email@domain.com"
```
This will allow you to commit changes and push them to the repository.


## Backend Setup
**Step 1:** Create a Python Virtual Environment

Open a terminal and create a Python virtual environment. We recommend using venv for the directory name for consistency with .gitignore:
```
python3 -m venv venv
```

**Step 2:** Activate Python Enviroment

**On Mac/Linux:**

Activate the virtual environment with the following command:
```
source venv/bin/activate
```
**On Windows:**

Activate the virtual environment with this command:
```
venv\Scripts\activate
```
Once activated, your terminal should show the virtual environment's name in the prompt.

**Step 3:** Install Backend Dependencies

Once the virtual environment is set up, activate it (see below for activation commands depending on your OS) and install the required dependencies:
```
pip install -r flask_backend/requirements.txt
```

**Step 4:** Run the Backend Server

You have two options to run the backend server:

**Option 1:** Use the command line to navigate to the flask_server directory and run the server:
```
cd flask_backend/flask_server
```
```
python3 server.py
```
**Option 2:** Alternatively, you can open server.py in an IDE like VSCode and click the play button on the top right corner.

## Frontend Setup

**Step 1:** Install [Docker](https://docs.docker.com/get-started/get-docker/)

Make sure Docker is installed on your machine.

**On Windows:**

Install WSL on your system. Installing Docker should prompt this by itself, but WSL is necessary to run Docker containers.

**Step 2:** Change Directory
```
cd react_frontend
```

**Step 3:** Build the Frontend Docker Image

Once Docker is installed, open another terminal window and navigate to your project directory. Then build the Docker image for the frontend:
```
docker build -t loteria_frontend:l_front .
```
**Step 4:** Run the Frontend Docker Container

Start the frontend container by running the following command:
```
docker compose up 
```
**Step 5:** Access the Frontend in Your Browser

Open your web browser and go to the following URL to view the frontend:
```
http://localhost:3000/
```
