# Mini_RAG
This is a minimal implementation of the RAG model for question answering.

## Requirements

- Python 3.8 or later

#### Install Python using MiniConda

1) Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)

2) Create a new environment using the following command:
```bash
$ conda create -n mini-rag python=3.8
Installation

Install the required packages  
$ pip install -r requirements.txt

Setup the environment variables  
$ cp .env.example .env  
Set your environment variables in the '.env' file like 'OPENA_API_KEY' value
``` bash 
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
