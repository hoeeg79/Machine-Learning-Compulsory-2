import autogen
from internal.agents.Tools.api_tool import call_api_tool

def create_summarize_agent(LLM_CONFIG):
    summarize_agent = autogen.AssistantAgent(
        name="summarize",
        system_message=(
            """
            You are an internal summarizer agent.
            Your task is to summarize the findings of another agent.
            Provide a concise summary of the key points and insights.
            The next agent after you should be critic.

            You should format an output structured like this:
            ### Paper 1: "Low Interest Rates and Housing Bubbles: Still No Smoking Gun"
            - **Authors:** Kenneth Kuttner
            - **Year Published:** 2012
            - **Description:** This paper revisits the relationship between interest rates and house prices, arguing that the impact of interest rates on house prices is quite modest based on recent studies and new evidence.
            - **Deposited Date:** Not available
            - **Full Text:** The full text discusses the modest impact of interest rates on house prices, contrary to conventional user cost theory.
            """
        ),
        llm_config=LLM_CONFIG
    )

    # summarize_agent.register_for_llm(name="api_tool", description="Call api")(call_api_tool)
    return summarize_agent