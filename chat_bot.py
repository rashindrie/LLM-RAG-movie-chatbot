from dataset_handler import read_data
from pinecone_handler import PineconeHandler
from openai_handler import OpenAI


class ChatBot:
    def __init__(self, context_path, index_name = "imdb-movies"):
        # set up pinecone and openai handlers
        self.pinecone_h = PineconeHandler()
        self.openai_h = OpenAI()

        # setup pinecone index
        self._setup_pinecone(context_path, index_name)

        # setup RAG based prompt
        self.qa_with_sources = self.openai_h._setup_openai_response(self.pinecone_h.docsearch)

    def _setup_pinecone(self, context_path, index_name):
        dataset = read_data(context_path)

        # step 1: create documents for storing on pinecone
        self.pinecone_h.create_documents_from_data(dataset)

        # step 2: check cost of sending tokens to OpenAI using tiktoken using documents created in step 1
        self.openai_h.check_cost_with_tiktoken(self.pinecone_h.docs)

        # step 3: create index on pinecone
        self.pinecone_h.create_index_on_pinecone(index_name)

        # step 4: upsert documents created in step 1 to index created in Step 3
        self.pinecone_h.upsert_to_pinecone(self.openai_h.embeddings)

    def generate_response(self, question):
        return self.openai_h.qa_with_sources(question)
