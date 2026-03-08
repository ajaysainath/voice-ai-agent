from agent.agent_controller import understand_request

user_text = "Book an appointment with cardiologist tomorrow"

result = understand_request(user_text)

print("Agent Output:", result)