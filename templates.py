from langchain.prompts import PromptTemplate

class Prompt:
    
    def bangla_to_english(self, text):
        prompt_template_name=PromptTemplate(
            input_variables=['text'],
            template='Translate the following Bangla text to English: {text}'
        )
        return prompt_template_name.format(text=text)
    