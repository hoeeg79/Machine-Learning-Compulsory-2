# Assignment Description:
The goal of this assignment is to apply the concepts you've learned to implement and evaulate an AI agent.

# 01. Implement an AI agent
Using the Autogen framework, implement an AI agent that can solve the following type of task:

Find a research paper on [topic] that was published [in/before/after] [year] and has [number of citations] citations.

Square brackets:
```
The square brackets are placeholders for the actual topic, year, number of citations, etc.
```

# 02. Implement the required tools
In order to solve the task, the agent will need to search for research papers based on publishing year, number of citations, etc.

To do this, the agent could use the following tools:
- A web search tool
- A research paper database
- A research paper search API

Your task is to implement one of these, or a similar tool that provides your agent with the ability to search for research papers based on publishing year, number of citations, etc.

# 03. Evaluate the agent
Once you've implemented the agent, you need to evaluate how it performs on the task. As described in the lecture on agent evaluation you can rely on the underlying LLM to evaluate how your agent performs.

# Cloud-based LLM
This assignment will be difficult to run locally due to its complexity. To make it possible for you to complete the assignment, you can make use of a cloud-based LLM and a fork of the Autogen framework.

## Mistral AI
The Mistral AI cloud API has a generous free tier that you can use. You need to create an account and then create an API key through their platform.