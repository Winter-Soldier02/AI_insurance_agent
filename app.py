from flask import Flask, render_template, request, jsonify
import sqlite3
import openai
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def fetch_policies():
    conn = sqlite3.connect('policies.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM policies")
    data = cur.fetchall()
    conn.close()
    return data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    mode = request.json.get('mode', 'recommendation')  # default mode

    if mode == 'recommendation':
        policies = fetch_policies()
        policy_text = "\n".join(
            f"- {p[1]} (Type: {p[2]}, Age: {p[3]}, Income: {p[4]}, Coverage: {p[5]}) - {p[6]}"
            for p in policies
        )

        prompt = f"""
You are an intelligent insurance assistant. A user said: "{user_input}".

Here are the available policies:
{policy_text}

depending on the user's question reply him/her

if the user request is based on request for policy compare policies and give him most appropriate policies
 Format your response with real line breaks (press Enter after each line). Do not use \\n or HTML.

Example:
1. **Policy Name**
• Type: ...
• Age Group: ...
• Income Group: ...
• Coverage: ...
• Why it's recommended: ...
"""

    elif mode == 'document':
        prompt = f"""
You are an expert insurance document generator bot.

Based on the user's input: "{user_input}", generate a formal insurance policy document.

The document should include:
- Full Name
- Age
- Policy Type
- Coverage Amount
- Duration
- Optional Add-ons (if mentioned)
- Formal Legal Language (realistic)

 Output should look like a real policy document, formatted cleanly with line breaks.
"""

    else:
        return jsonify({'reply': "❌ Invalid mode selected."})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    answer = response.choices[0].message.content
    return jsonify({'reply': answer})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
