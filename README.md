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


# Sources
- https://aws.amazon.com/what-is/retrieval-augmented-generation/
- https://www.datacamp.com/datalab/w/851cb143-5b7e-4c15-9377-a983a3e47e24
