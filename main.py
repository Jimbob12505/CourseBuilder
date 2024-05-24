import openai
from dotenv import find_dotenv, load_dotenv
import os
import time
import logging
from datetime import datetime

API_KEY = os.environ.get("SECRET_KEY")
COURSE_BUILDER_ID = os.environ.get("COURSE_BUILDER")
SLIDE_CREATOR_ID = os.environ.get("SLIDE_CREATOR")

client = openai.OpenAI(api_key=API_KEY)
model = "gpt-4o"

#== ASSISTANT ==#

COURSE_ASSISTANT = "asst_weTVnAaZ7QaTI5vRQr5uscPp"
SLIDE_ASSISTANT = "asst_X1FErHWdEjvsJQ0n4svz4OAC"

# THREAD

thread_id = "thread_rKRip6iwuS6Cm9mfJxWdQ2ig"

message = "Create a 5 minute course on Introduction to Geology"
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content=message
)

run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=COURSE_ASSISTANT,
    instructions="Please address the user as Vatsal Labh"
)

def wait_for_completion(client, thread_id, run_id, sleep_interval=5):
    
    while True:
        try:
            run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id = run_id)
            if run.completed_at:
                elapsed_time = run.completed_at - run.created_at
                formatted_elapsed_time = time.strftime(
                    "%H:%M:%S", time.gmtime(elapsed_time)
                )
                print(f"Run completed in {formatted_elapsed_time}")
                logging.info(f"Run completed in {formatted_elapsed_time}")

                messages = client.beta.threads.messages.list(thread_id=thread_id)
                last_message = messages.data[0]
                response = last_message.content[0].text.value
                print(f"Assistant Response: {response}")
                break
        except Exception as e:
            logging.error(f"Error occured {e}")
            break
        logging.info("Waiting for run to complete...")
        time.sleep(sleep_interval)


wait_for_completion(client=client, thread_id=thread_id, run_id=run.id)


run_step = client.beta.threads.runs.steps.list(
    thread_id=thread_id,
    run_id=run.id
)

print(f"Steps ---> {run_step.data[0]}")