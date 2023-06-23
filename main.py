import os

import anthropic
from dotenv import load_dotenv

load_dotenv()

anthropic_client = anthropic.Client(api_key=os.getenv("ANTHROPIC_API_KEY"))

# you can put some context here, to specialize the Model
context = ""

# Anthropic Claude pricing: https://cdn2.assets-servd.host/anthropic-website/production/images/model_pricing_may2023.pdf
PRICE_PROMPT = 1.102E-5
PRICE_COMPLETION = 3.268E-5

def count_used_tokens(prompt, completion):
    prompt_token_count = anthropic.count_tokens(prompt)
    completion_token_count = anthropic.count_tokens(completion)

    prompt_cost = prompt_token_count * PRICE_PROMPT
    completion_cost = completion_token_count * PRICE_COMPLETION

    total_cost = prompt_cost + completion_cost

    return (
        "🟡 Used tokens this round: "
        + f"Prompt: {prompt_token_count} tokens, "
        + f"Completion: {completion_token_count} tokens - "
        + f"{format(total_cost, '.5f')} USD)"
    )

# run a chat loop, retrieve text from the user, collect context and generate a response.
while True:
    user_inp = input("You: ")

    current_inp = anthropic.HUMAN_PROMPT + user_inp + anthropic.AI_PROMPT
    context += current_inp

    prompt = context

    completion = anthropic_client.completion(
        prompt=prompt, model="claude-v1.3-100k", max_tokens_to_sample=1000
    )["completion"]

    context += completion

    print("Anthropic: " + completion)
    print(count_used_tokens(prompt, completion))