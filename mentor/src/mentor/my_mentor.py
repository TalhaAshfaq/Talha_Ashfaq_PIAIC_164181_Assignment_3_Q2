from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, OpenAIChatCompletionsModel, set_tracing_disabled, set_default_openai_api
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

def mentor_agent():
    external_client = AsyncOpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/",
        api_key=api_key               
    )

    set_default_openai_client(external_client)
    set_tracing_disabled(True)
    set_default_openai_api("chat_completions")

    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=external_client
    )


    mentor = Agent(name="Mentor", instructions="You are a helpful mentor your job is to help user to guide in Study, Education, Job and Technical Skills, Courses", model=model)
    
    result = Runner.run_sync(mentor, "i have done my BS in Information Technology and now i want to learn a Emeerging Technology can you help me? after completing your answer in single chat.")
    md_file = result.final_output
    with open("output.md","w") as file:
        file.write(md_file)
        file.close()

    with open("README.md","w") as file:
        file.write(md_file)
        file.close()
    print(result.final_output)

