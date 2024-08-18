from langchain.prompts import PromptTemplate
import google.generativeai as genai


class Prompt:
    
    def bangla_to_english(self, text):
        prompt_template_name=PromptTemplate(
            input_variables=['text'],
            template='Translate the following Bangla text to English: {text}'
        )
        return prompt_template_name.format(text=text)

    def audio_to_text(self, file_path ):
        # Upload the file.
        audio_file = genai.upload_file(path=file_path)
        return ["Summarize the speech." , audio_file]
    
    