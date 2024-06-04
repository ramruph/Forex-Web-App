# Forex-Web-App
![alt images](https://github.com/ramruph/Forex-Web-App/blob/main/images/demo.gif)

# Project Name: Forex Trading Application

This Forex Trading Application is designed to provide real-time forex data and perform various data analyses. The application is built using Flask for the web interface and integrates Prometheus for monitoring.

## Features
I chose this system design and approach to accomplish the following goals for the project's end:
- Real-time forex data retrieval
- Data analysis and pattern detection
- Web interface for displaying data
- Prometheus integration for monitoring
- Continuous Integration and Continuous Delivery (CI/CD) setup using GitHub Actions
- Kafka integration for event-driven messaging

## Project Folder Structure
The system is designed as a Flask app with Javascript frontend and Python backend for analytics and API connections and data gathering.

The folder structure is as follows:ß
- configs: Contains config files for Kafka, Prometheus and Github Actions
- src: Source Python code for:
    - Flask Application
    - Data Collection
    - Data Analytics
    - Collecting scheduled data
    - API connectivity script
-static: contains web front end code and style designs
-test: Contains unittests and pytest scripts for data capture, data integration, and application
-Procfile: configuration for Heroku
-requirements.txt: system requirements for running application locally

![alt images](https://github.com/ramruph/Forex-Web-App/blob/main/images/screenshot1.png)

![alt images](https://github.com/ramruph/Forex-Web-App/blob/main/images/screenshot2.png)

## Setup Instructions
### Prerequisites
- Python 3.9
- Pip
- Virtualenv
- Heroku CLI (for deployment)
- Docker (for running Prometheus and Kafka)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/forex_app.git
cd forex_app
```

### Step 2: Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  
```
### Step 3: Install Dependencies
```bash
pip install -r requirements.txtß
```
### Step 4: Run Application Locally
```bash
python src/app.py
```

