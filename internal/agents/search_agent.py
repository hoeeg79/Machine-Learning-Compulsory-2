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
        max_consecutive_auto_reply=2,
        llm_config=LLM_CONFIG,
    )
    assistant.register_for_llm(name="api_tool", description="call api")(call_api_tool)

    return assistant

# "q=yearPublished>2018 AND (fullText:"TOPIC" OR fullText:"FIRST SYNONYM" OR fullText:"SECOND SYNONYM" OR fullText:"THIRD SYNONYM" OR fullText:"FOURTH SYNONYM")"

# You are not a reviewer or critic. If you receive research paper data from the api_tool, you should format an output structured like this:
# ### Paper 1: "Low Interest Rates and Housing Bubbles: Still No Smoking Gun"
# - **Authors:** Kenneth Kuttner
# - **Year Published:** 2012
# - **Description:** This paper revisits the relationship between interest rates and house prices, arguing that the impact of interest rates on house prices is quite modest based on recent studies and new evidence.
# - **Deposited Date:** Not available
# - **Full Text:** The full text discusses the modest impact of interest rates on house prices, contrary to conventional user cost theory.

# Send this to chat where a critic will review your findings.