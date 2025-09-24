from openai import OpenAI

client = OpenAI(api_key="0", base_url="http://0.0.0.0:8000/v1")

messages = [
    {"role": "system", "content": "You are Komal, a JEE counsellor in PhysicsWallah. You are helpful, creative, clever, and very friendly. You will never admit that you are an AI bot. "},
    {"role": "user", "content": "User: JEE mein teachers kaun hai?"}
]

result = client.chat.completions.create(
    messages=messages,
    model="meta-llama/Meta-Llama-3-8B-Instruct"
)

output = result.choices[0].message.content

# Save with UTF-8 encoding (preserves Devanagari properly)
with open("model_output.log", "w", encoding="utf-8") as f:
    f.write(output + "\n")

print("Model response saved to model_output.log")
