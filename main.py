import openai
from dotenv import find_dotenv, load_dotenv
import os
import time
import logging
from datetime import datetime

API_KEY = os.environ.get("SECRET_KEY")

client = openai.OpenAI(api_key=API_KEY)
model = "gpt-4-turbo"

#== ASSISTANT ==#

COURSE_ASSISTANT = "asst_weTVnAaZ7QaTI5vRQr5uscPp"
SLIDE_ASSISTANT = "asst_X1FErHWdEjvsJQ0n4svz4OAC"

def main():

    instructions = input("Enter the instructions for the course: ")
    audience = input("Enter the audience/style guide: ")
    length = input("Enter the length of the lesson in minutes (5, 10, 15, 20, 25): ")

    prompt = f"""
        Instructions: {instructions}
        Audience/Style Guide: {audience}
        Length of Lesson: {length} minutes
    """

    thread = client.beta.threads.create(
        messages = [
            {
                "role" : "user",
                "content" : prompt
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
    return last_message.content[0].text.value


if __name__ == "__main__":
    main()