from groq import Groq
import os
import time
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.1-8b-instant"

def ask_ai(prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )
    time.sleep(1)
    return response.choices[0].message.content.strip()

def detect_severity(technical_text):
    prompt = f"""
    Read this technical outage description and reply with only one word:
    low, medium, or high based on severity.
    Text: {technical_text}
    """
    return ask_ai(prompt).lower()

def generate_message(technical_text, tone, severity, stage):
    prompt = f"""
    You are a customer communication expert.
    Technical issue: {technical_text}
    Severity: {severity}
    Tone: {tone} (calm = professional and reassuring,
                   empathetic = understanding and caring,
                   concise = short and direct)
    Stage: {stage}
    Write a customer-facing status update for the {stage} stage.
    - Do NOT use technical terms
    - Keep it under 3 sentences
    - Match the tone exactly
    - Be human and clear
    Reply with only the message, nothing else.
    """
    return ask_ai(prompt)

def check_quality(message, tone):
    prompt = f"""
    Does this message match a {tone} tone?
    Message: {message}
    Reply with only YES or NO.
    """
    result = ask_ai(prompt)
    return "YES" if "YES" in result.upper() else "NO"

def agent_loop(technical_text, tone, severity=None):
    if not severity:
        severity = detect_severity(technical_text)

    results = {}
    stages = ["initial", "in-progress", "resolved"]

    for stage in stages:
        max_tries = 3
        attempt = 0
        while attempt < max_tries:
            message = generate_message(technical_text, tone, severity, stage)
            quality = check_quality(message, tone)
            if quality == "YES":
                results[stage] = message
                break
            else:
                attempt += 1
                if attempt == max_tries:
                    results[stage] = message

    return results, severity

if __name__ == "__main__":
    test_text = "Database primary node failed, replication lag 200ms, failover initiated"
    results, severity = agent_loop(test_text, "empathetic")
    print(f"\nDetected Severity: {severity}")
    for stage, msg in results.items():
        print(f"\n{stage.upper()}:\n{msg}")
