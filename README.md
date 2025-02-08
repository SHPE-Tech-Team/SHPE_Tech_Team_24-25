# AI Lotería 2024-2025
![google loteria gif](https://www.google.com/logos/doodles/2019/celebrating-loteria-6753651837108226.3-2xa.gif)

This project brings a new approach to the popular Latin American game Lotería. With using Python libraries that utilize convolutional neural networks and deep learning, Lotería can become fully automized. 


# Project Setup Instructions

This guide will walk you through setting up the backend and frontend of the project. For the backend, we'll skip the Docker setup for Mac users due to limitations, and instead focus on Docker for the frontend.

## Backend Setup
**Step 1:** Create a Python Virtual Environment

Open a terminal and create a Python virtual environment. Replace `<myenvpath>` with your desired environment name (e.g., myenv):
```
python3 -m venv <myenvpath>
```

**Step 2:** Activate Python Enviroment

**On Mac/Linux:**

Activate the virtual environment with the following command:
```
source `<myenvpath>`/bin/activate
```
**On Windows:**

Activate the virtual environment with this command:
```
`<myenvpath>`\Scripts\activate
```
Once activated, your terminal should show the virtual environment's name in the prompt.

**Step 3:** Install Backend Dependencies

Once the virtual environment is set up, activate it (see below for activation commands depending on your OS) and install the required dependencies:
```
pip install -r requirements.txt
```

**Step 4:** Run the Backend Server

You have two options to run the backend server:

**Option 1:** Use the command line to navigate to the flask_server directory and run the server:
```
cd back/flask_server
```
```
python3 server.py
```
**Option 2:** Alternatively, you can open server.py in an IDE like VSCode and simply click the play button on the top right corner to run the server.

## Frontend Setup

**Step 1:** Install [Docker](https://docs.docker.com/get-started/get-docker/)

Make sure Docker is installed on your machine.

**Step 2:** Build the Frontend Docker Image

Once Docker is installed, open another terminal window and navigate to your project directory. Then build the Docker image for the frontend:
```
docker build -t loteria_frontend:l_front .
```
**Step 3:** Run the Frontend Docker Container

Start the frontend container by running the following command:
```
docker compose up 
```
**Step 4:** Access the Frontend in Your Browser

Open your web browser and go to the following URL to view the frontend:
```
http://localhost:3000/
```