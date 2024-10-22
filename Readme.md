# ConfigPilot (Simplify Your Configurations)

<img src="screens/assets/logo.jpg" >

## Description

ConfigPilot automates and simplifies network device configurations for routers, switches, and servers, offering step-by-step guidance for both IT professionals and non-technical users.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Pip (Python package manager)

### Installation

## Clone the repository:

````bash
git clone https://github.com/nomanmazharr/config-pilot.git
cd CONFIG-PILOT

## Set up a virtual environment:

```bash
python -m venv config-pilot
````

## For Windows:

```bash
.\config-pilot\Scripts\activate
```

## For Mac/Linux:

```bash
source config-pilot/bin/activate
```

## Install the required packages:

```bash
pip install -r requirements.txt
```

## Create a .env file in the root directory with the following content:

```bash
GROQ_API_KEY='you api key here'
```

## Run the application:

```bash
streamlit run .\app.py
```
