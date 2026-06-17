from tools.llm import llm
import json

def event_extraction_agent(state):
    filtered_news = state["filtered_news"]
#     prompt = f"""
# You are a financial event extracion system.

# Extract only important businees events.

# For each event provide:

# - event type
# - title
# - impact
# - category

# Categories:
# - AI
# - Partnership
# - Expansion
# - Workforce
# - Earnings
# - Acquisition
# - Product
# - Regulation

# Return VALID JSON ONLY.

# News:
# {news}
# """
#     response = llm.invoke(prompt)
#     return {
#         "events": response.content
#     }
    prompt = f"""
You are a financial event extraction system.

Return ONLY valid JSON.

Do not use markdown.
Do not use ```json.
Do not provide explanations.

Format:

[
  {{
    "event_type": "",
    "title": "",
    "impact": "Positive|Negative|Neutral",
    "category": ""
  }}
]

Text:

{filtered_news}
"""
    response = llm.invoke(prompt)
    print("RAW Response")
    print(response.content)
    if isinstance(response.content, list):
        raw_text = response.content[0]["text"]

    else:
        raw_text = response.content
    events = json.loads(raw_text)

    return {
        "events": events}