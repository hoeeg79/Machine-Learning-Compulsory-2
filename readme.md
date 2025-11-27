# Research Paper Lookup Helper

This project is the second compulsory of Machine Learning at EASV. It evovles around making use of LLMs as AI agents, tools and autogen, to look for research papers via an API.

## Initial Setup

You will need to get an API key for the CORE API. This can be found here: https://core.ac.uk/services/api

You will also need an API key for either MistralAI or Cerebras. Given which you chose, minor changes are needed in main, to align. At the moment it is setup for Cerebras.

Now that you have your keys, make a ".env" file in root of the directory, and add two lines like this:

```
API_KEY=[YOUR_API_KEY_HERE]
AI_API_KEY=[YOUR_AI_KEY_HERE]
```

## How to Run

You have two options to run it. When you have turned it on you can use swagger on localhost:8000/docs to access the endpoint.

### Option 1: Docker

This is the easiest option. All you need to do is start the docker compose:

```
docker compose up
```

### Option 2: Run locally

We strongly recommend you setup a virtual environment if you run locally. To run it, first you have to install requirements. 

In a terminal, find your way to the root folder and run:

```
pip install -r req.txt
```

Now you can start the project by running:
```
uvicorn main:app
```

## Changes to use Mistral AI

If you want to use Mistral AI instead. you will need to change which config is used in the agents. In main.py, simply change the LLM_CONFIG used as parameter to instantiate the agents, to the mistral AI config, instead of Cerebras config.