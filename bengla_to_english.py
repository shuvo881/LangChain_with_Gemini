from model import Identifier
from templates import Prompt



text = 'আমি বাংলায় গান গাই।'
tmp = Prompt()
prompt = tmp.bangla_to_english(text=text)

identifier = Identifier('gemini-1.5-flash')
model = identifier.get()


response = model.generate_content(prompt)

print(response.text)
