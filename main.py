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