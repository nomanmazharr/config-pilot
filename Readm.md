# ConfigPilot (Simplify Your Configurations)

<img src="/public/Config Pilot Logo.png" >

## Description

ConfigPilot automates and simplifies network device configurations for routers, switches, and servers, offering step-by-step guidance for both IT professionals and non-technical users.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Pip (Python package manager)

### Installation

## Clone the repository:

````bash
git clone https://github.com/umairazmat/Ai-Codify
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
OPENAI_API_KEY=your_actual_api_key
OPENAI_API_BASE=your_actual_api_key
```

## Run the application:

```bash
streamlit run .\app.py
```

## if script not run :

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
