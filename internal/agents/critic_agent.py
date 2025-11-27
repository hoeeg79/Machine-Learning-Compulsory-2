import autogen
from internal.agents.Tools.api_tool import call_api_tool

def create_critic_agent(LLM_CONFIG):
    critic_agent = autogen.AssistantAgent(
        name="critic",
        system_message=(
            """
            You are an internal critic reviewing the work of another agent.
            Ensure that the research paper meets the requirements specified.
            If the paper is satisfactory, respond with:
        
            APPROVED
            TERMINATE
        
            If the paper does not meet the requirements, provide constructive feedback on what needs to be improved.
        
            
            """
        ),
        max_consecutive_auto_reply=2,
        llm_config=LLM_CONFIG
    )

    return critic_agent
