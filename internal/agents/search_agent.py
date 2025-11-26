import autogen
from internal.agents.Tools.api_tool import call_api_tool

def create_search_agent(LLM_CONFIG):
    assistant = autogen.AssistantAgent(
        name="Search Query Agent",
        system_message="""
                Your task is to create search prompts based on user requests for academic papers.
                When the user provides a topic, year constraint (in, before, after), year. 
                You should take the topic and tell which tool you suggest.
                example of search: "TOPIC".
                The tool to use for the search is "api_tool".
            """,
        llm_config=LLM_CONFIG,
    )
    assistant.register_for_llm(name="api_tool", description="Call api")(call_api_tool)

    return assistant

# "q=yearPublished>2018 AND (fullText:"TOPIC" OR fullText:"FIRST SYNONYM" OR fullText:"SECOND SYNONYM" OR fullText:"THIRD SYNONYM" OR fullText:"FOURTH SYNONYM")"