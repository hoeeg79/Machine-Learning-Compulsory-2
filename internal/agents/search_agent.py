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

                If asked again, to improve the search, you should think of a synonym for the topic, 
                and use it to create a new search query, and execute the tool again.
            """,
        max_consecutive_auto_reply=2,
        llm_config=LLM_CONFIG,
    )
    assistant.register_for_llm(name="api_tool", description="call api")(call_api_tool)

    return assistant
