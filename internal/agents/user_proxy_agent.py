# todo sej agent

def create_user_proxy():
    user_proxy = UserProxyAgent(
        name="user_proxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=5,
        is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"]
    )
    user_proxy.register_for_execution(name="calculator")(calculator)
    return user_proxy
