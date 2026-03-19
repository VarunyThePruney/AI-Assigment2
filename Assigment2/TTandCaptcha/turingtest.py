"""
Turing Test Simulation (Hugging Face - Updated Router API)
"""

import os
import requests

MODEL = "HuggingFaceH4/zephyr-7b-beta"
API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL}"

HEADERS = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
    "Content-Type": "application/json"
}


def ai_response(prompt, history):
    full_prompt = ""
    for turn in history:
        full_prompt += f"{turn['role']}: {turn['content']}\n"
    full_prompt += f"user: {prompt}\nassistant:"

    payload = {
        "inputs": full_prompt,
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.9
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    result = response.json()

    # Handle normal response
    if isinstance(result, list):
        return result[0]["generated_text"].split("assistant:")[-1].strip()

    # Handle errors
    elif isinstance(result, dict) and "error" in result:
        return f"[HF API ERROR]: {result['error']}"

    else:
        return "[Unexpected API Response]"


def main():
    print("\n===== TURING TEST (Hugging Face Router API) =====")
    print("You are BOTH the Judge and the Human participant.")
    print("-----------------------------------------------")

    history = []
    rounds = int(input("How many questions would you like to ask? "))

    for i in range(rounds):
        print(f"\nQuestion {i+1}")
        question = input("Judge asks: ")

        human_reply = input("Your HUMAN answer: ")

        ai_reply = ai_response(question, history)

        history.append({"role": "user", "content": question})
        history.append({"role": "assistant", "content": ai_reply})

        print("\n--- Responses (Anonymous) ---")
        print("Entity A:", human_reply)
        print("Entity B:", ai_reply)

    print("\n===== FINAL DECISION =====")
    guess = input("Which entity is the AI? (A/B): ")

    if guess.strip().upper() == "B":
        print("Correct! Entity B was the AI.")
    else:
        print("Incorrect. Entity B was the AI.")


if __name__ == "__main__":
    main()