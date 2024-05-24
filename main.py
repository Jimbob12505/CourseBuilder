import openai
from dotenv import find_dotenv, load_dotenv
import os
import time
import logging
from datetime import datetime

API_KEY = os.environ.get("SECRET_KEY")

client = openai.OpenAI(api_key=API_KEY)
model = "gpt-4o"

#== ASSISTANT ==#

COURSE_ASSISTANT = "asst_weTVnAaZ7QaTI5vRQr5uscPp"
SLIDE_ASSISTANT = "asst_X1FErHWdEjvsJQ0n4svz4OAC"

def main():
    prompt = input("Enter your prompt: ")
    thread = client.beta.threads.create(
        messages = [
            {
                "role" : "user",
                "content" : """ Create a 5 minute course on "How to build a car" """
            }
        ]
    )

    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=COURSE_ASSISTANT)
    print(f"Run created: {run.id}")
    
    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        print(f"Run Status: {run.status}")
        time.sleep(1)
    else:
        print("Run Completed")
    
    message_response = client.beta.threads.messages.list(thread_id=thread.id)
    messages = message_response.data
    last_message = messages[0]
    print(last_message.content[0].text.value)


if __name__ == "__main__":
    main()