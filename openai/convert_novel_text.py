import openai

# Set your OpenAI API key
api_key = 'YOUR_API_KEY'
openai.api_key = api_key

# Text to be converted
input_text = """
[Insert your text here]
"""

# Call the completion endpoint of the GPT-3.5 API
response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=input_text,
  max_tokens=1000,  # Adjust as needed for your text length
  temperature=0.5,  # Controls randomness of generation
  n=1,  # Number of completions to generate
  stop="\n\n"  # Stop generation at a suitable point
)

# Output the generated text
generated_text = response.choices[0].text.strip()
print(generated_text)
