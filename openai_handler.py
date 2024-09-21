import os
import tiktoken

from langchain.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain

from PROMPTS import *

class OpenAI:
    def __init__(self, tiktoker_enc="cl100k_base", cost_per_1000_tokens=0.0001, embedding_model="text-embedding-ada-002"):
        self.openai_api_key = os.environ["OPENAI_API_KEY"]
        self.cost_per_1000_tokens = cost_per_1000_tokens
        self.tiktoken_enc = tiktoker_enc
        self.currency = "AUD"

        self.embeddings = OpenAIEmbeddings(
            model=embedding_model
        )

        self.document_prompt = PromptTemplate.from_template(DOCUMENT_PROMPT)
        self.question_prompt = PromptTemplate.from_template(QUESTION_PROMPT)

        # define the OpenAI model to use for the Chatbot
        self.llm_model = ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0)

    def check_cost_with_tiktoken(self, docs):
        # Create the encoder
        encoder = tiktoken.get_encoding(self.tiktoken_enc)

        # Create a list containing the number of tokens for each document
        tokens_per_doc = [len(encoder.encode(doc.page_content)) for doc in docs]

        print(tokens_per_doc[:5])

        # Show the estimated cost, which is the sum of the amount of tokens divided by 1000, times $0.0001
        total_tokens = sum(tokens_per_doc)
        cost = (total_tokens / 1000) * self.cost_per_1000_tokens
        print(f"Cost estimation using Tiktoken: {cost} {self.currency}")


    def _setup_openai_response(self, docsearch):
        self.qa_with_sources = RetrievalQAWithSourcesChain.from_chain_type(
            chain_type="stuff",  # there are other chain types but this is cheaper
            llm=self.llm_model,
            chain_type_kwargs={
                "prompt": self.question_prompt,
                "document_prompt": self.document_prompt
            },
            retriever=docsearch.as_retriever(),
        )
        return self.qa_with_sources
