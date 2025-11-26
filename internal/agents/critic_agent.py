import autogen

def create_critic_agent(LLM_CONFIG):
    critic_agent = autogen.AssistantAgent(
        name="critic",
        system_message=(
            """
            You are an internal critic reviewing the work of another agent.
            Ensure that the research paper meets the requirements specified.
            If the paper is satisfactory, respond with:
        
            APPROVED
        
            If the paper does not meet the requirements, provide constructive feedback on what needs to be improved.
        
            If it fulfills the requirements completely, respond **exactly** with the word TERMINATE
            on a line by itself, with nothing else, no quotes, no symbols.
            Example:
            TERMINATE
            """
        ),
        llm_config=LLM_CONFIG
    )
    return critic_agent