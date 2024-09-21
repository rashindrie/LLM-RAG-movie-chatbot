# Movie-ChatBot with Pinecone and OpenAI-ChatGPT

Retrieval-augmented generation, or RAG, is a technique used with large language models (LLMs) to provide additional context without fine-tuning or retraining. 
It enhances the ability of language models to provide factual responses without hallucinating, which is a limitation of classical setups.

The goal of this project is to build a question-answering bot for movie-related questions. 


# Tools

We will be using the following tools and models:

- [OpenAI](https://openai.com)'s gpt-3.5-turbo model for prompt completions
- [OpenAI](https://openai.com)'s text-embedding-ada-002 model to create vector embeddings
- [Pinecone](https://www.pinecone.io) as the vector database to store the embeddings
- [langchain](https://www.langchain.com) as the tool to interact with OpenAI and Pinecone

# Pre-requisites

1. Create a developer account in [OpenAI](https://platform.openai.com/signup) and obtain a secret key.
2. Create a [Pinecone](https://app.pinecone.io/?sessionType=signup) account and obtain an API key for it. 
3. Download the [IMDb Movies/Shows with Descriptions](https://www.kaggle.com/datasets/ishikajohari/imdb-data-with-descriptions) data set from Kaggle.

# Install Dependencies

```pip install openai==1.27
pip install pinecone-client==4.0.0
pip install langchain==0.1.19
pip install langchain-openai==0.1.6
pip install langchain-pinecone==0.1.0
pip install tiktoken==0.7.0
pip install typing_extensions==4.11.0
```

# Running the code

## Setup the Chatbot
```python
from chat_bot import ChatBot
chatbot = ChatBot(context_path=<<insert_dataset_path>>)
```

## Query the Chatbot

#### Input 1:
```
question = "What's a good movie about a dogs to watch with my kid"
response = chatbot.generate_response(question)
print(response)
```
#### Response 1:
```
{'question': "What's a good movie about a dogs to watch with my kid",
 'answer': "'A Dog's Purpose' is a heartwarming movie about a dog's journey through multiple lives and the bond it forms with humans. It would be a good movie to watch with a kid.\n",
 'sources': 'https://www.imdb.com/title/tt1753383'}

```

#### Input 2:
```
question = "What's a good movie about a nature?"
response = chatbot.generate_response(question)
print(response)
```
#### Response 2:
```
{'question': "What's a good movie about a nature?", 
'answer': "'Big Miracle' is a movie about environmental activism and saving whales. It showcases the beauty of nature and the importance of conservation efforts.\n", 
'sources': 'https://www.imdb.com/title/tt1430615'}
```


# Sources
- https://aws.amazon.com/what-is/retrieval-augmented-generation/
- https://www.datacamp.com/datalab/w/851cb143-5b7e-4c15-9377-a983a3e47e24
