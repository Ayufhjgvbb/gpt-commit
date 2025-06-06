import subprocess
import os
from openai import OpenAI
from dotenv import load_dotenv
import requests
import json
import re

# Load environment variables
load_dotenv()


def clean_commit_message(message):
    """
    Extract the commit message from between double quotes.
    The LLM response will always contain the message in double quotes.
    """
    # Find text between double quotes
    match = re.search(r'"([^"]*)"', message)
    if match:
        return match.group(1)
    return message.strip()  # Fallback to stripping if no quotes found


def get_git_diff():
    staged_files = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        capture_output=True,
        text=True
    ).stdout.strip().split('\n')

    if not staged_files or staged_files[0] == '':
        return None
    
    diffs = []
    for file in staged_files:
        if file:
            diff = subprocess.run(
                ["git", "diff", "--cached", "--", file],
                capture_output=True,
                text=True
            ).stdout.strip()
            if diff:
                diffs.append(f"Changes in {file}:\n{diff}")

    return "\n\n".join(diffs) if diffs else None


def check_ollama_available():
    try:
        response = requests.get("http://localhost:11434/api/tags")
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False


def generate_message_openai(diff, model="gpt-4"):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    if not client.api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable is not set. "
            "Please set it or use --backend ollama"
        )

    prompt = f"Write a concise Git commit message with no more than 50 characters. \
            The message should be inside of quotes for the following diff:\n\n{diff}"
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
        raw_message = response.choices[0].message.content.strip()
        return clean_commit_message(raw_message)
    except Exception as e:
        raise RuntimeError(f"Error calling OpenAI API: {str(e)}")


def generate_message_ollama(diff, model="codellama:latest"):
    if not check_ollama_available():
        raise RuntimeError("Ollama is not running. Please start Ollama first.")

    prompt = f"Write a concise Git commit message and the \
            message should be inside of quotes for the following diff:\n\n{diff}"
    
    try:
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(
            "http://localhost:11434/api/generate",
            headers=headers,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.3
                }
            }
        )
        response_data = response.json()

        if "response" in response_data:
            raw_message = response_data["response"].strip()
        elif "message" in response_data and "content" in response_data["message"]:
            raw_message = response_data["message"]["content"].strip()
        else:
            raise RuntimeError(f"Unexpected response format: {response_data}")
        
        return clean_commit_message(raw_message)
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error calling Ollama API: {str(e)}")
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Invalid JSON response from Ollama API: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error: {str(e)}")


def direct_commit(backend="openai", model=None):
    """
    Directly commit changes with an AI-generated commit message.
    """
    diff = get_git_diff()
    if not diff:
        print("No changes staged for commit.")
        return

    print("Generating commit message...")
    try:
        if backend == "ollama":
            message = generate_message_ollama(diff, model or "codellama:latest")
        else:
            message = generate_message_openai(diff, model or "gpt-4")
        
        subprocess.run(
            ["git", "commit", "-m", message],
            check=True
        )
        
        print(f"Changes committed successfully")
    except Exception as e:
        print(f"Error: {e}")
        return
