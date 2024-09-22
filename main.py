import langchain

from chat_bot import ChatBot
from configs import set_access_keys

# Set to True to Enable debug logging
langchain.debug = False
set_access_keys()

chatbot = ChatBot(context_path='data/IMDB.csv')

question_1 = "What's a good movie about a dogs to watch with my kid"
response_1 = chatbot.generate_response(question_1)
print(response_1)

question_2 = "What's a good movie about a nature to watch with my kid"
response_2 = chatbot.generate_response(question_2)
print(response_2)
