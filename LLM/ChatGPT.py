'''
pip install openai
'''
import os
import openai

class ChatGPT():
    def __init__(self, model_path = 'gpt-3.5-turbo', api_key = None, proxy_url = None):
        if proxy_url:
            os.environ['https_proxy'] = proxy_url if proxy_url else None
            os.environ['http_proxy'] = proxy_url if proxy_url else None
        openai.api_key = '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'
        self.model_path = model_path
        self.prompt = "所有回答最多使用1000字"

    def generate(self, message):
        try:
            response = openai.ChatCompletion.create(
                model=self.model_path,
                messages=[
                    {"role": "user", "content": message}
                ]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            print(e)
            return "对不起，你的请求出错了，请再次尝试。\nSorry, your request has encountered an error. Please try again.\n"
    def message_to_prompt(self, message, system_prompt=""):
        system_prompt = self.prompt + system_prompt
        for interaction in self.history:
            user_prompt, bot_prompt = str(interaction[0]).strip(' '), str(interaction[1]).strip(' ')
            system_prompt = f"{system_prompt} User: {user_prompt} Bot: {bot_prompt}"
        prompt = f"{system_prompt} ### Instruction:{message.strip()}  ### Response:"
        return prompt        
        
    def chat(self, system_prompt, message, history):
        self.history = history
        prompt = self.message_to_prompt(message, system_prompt)
        response = self.generate(prompt)
        self.history.append([message, response])
        return response, self.history
    
    def clear_history(self):
        # 清空历史记录
        self.history = []