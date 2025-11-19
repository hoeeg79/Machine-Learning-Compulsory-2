import autogen

def create_search_agent(LLM_CONFIG):
    assistant = autogen.AssistantAgent(
        name="Search Query Agent",
        system_message="""
                Your task is to create search prompts based on user requests for academic papers.
                When the user provides a topic, year constraint (in, before, after), year. 
                First come up with 4 synonyms or related terms for the topic.
                The search query should be contructed the following way:
                "q=yearPublished>2018 AND (fullText:"TOPIC" OR fullText:"FIRST SYNONYM" OR fullText:"SECOND SYNONYM" OR fullText:"THIRD SYNONYM" OR fullText:"FOURTH SYNONYM")"
            """,
        llm_config=LLM_CONFIG,
    )
    return assistant