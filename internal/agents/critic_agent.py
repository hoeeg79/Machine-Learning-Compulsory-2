import autogen

def create_critic_agent():
    critic_agent = autogen.AssistantAgent(
        name="critic",
        system_message=(
            "You are an internal critic reviewing the work of another agent.\n"
            "Ensure that the research paper meets the requirements specified.\n"
            "If the paper is satisfactory, respond with 'APPROVED'.\n"
            "If the paper does not meet the requirements, provide constructive feedback on what needs to be improved."
        )
    )
    return critic_agent