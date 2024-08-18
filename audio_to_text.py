from model import Identifier
from templates import Prompt




file_path = 'simple.mp3'
tmp = Prompt()
prompt = tmp.audio_to_text(file_path)

print(prompt)

identifier = Identifier('gemini-1.5-flash')
model = identifier.get()


response = model.generate_content(prompt)

print(response.text)
