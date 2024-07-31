from decouple import config
from llama_index.llms.groq import Groq

from fast_zero.components.prompts import PROMPT_HEALTH_CHECK

llm = Groq(
    model=config('MODEL_NAME'),
    api_key=config('GROQ_API_KEY'),
    temperature=config('TEMPERATURE'),
)


def generate_health_check():
    response = llm.complete(PROMPT_HEALTH_CHECK)
    return response.text
