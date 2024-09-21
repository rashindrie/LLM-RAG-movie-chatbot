import os

from pinecone import Pinecone, ServerlessSpec
from langchain.document_loaders import DataFrameLoader
from langchain_pinecone import PineconeVectorStore


class PineconeHandler:
    def __init__(self):
        # initialize pinecone
        self.pc = Pinecone(
            api_key=os.environ.get("PINECONE_API_KEY"),
            environment="gcp-starter"
        )
        self.docsearch = None

    def create_documents_from_data(self, movies_df, debug=False):
        """
        Convert to documents that are reuqired by Pinecone

        Create page_content column which will include Title, Genre and Description.
        This will be the content in the Document.
        Any other information in the movies_df will be considered as meta-data
        """
        movies_df["page_content"] = "Title: " + movies_df["movie_title"] + "\n" + \
                                    "Genre: " + movies_df["genres"] + "\n" + \
                                    "Description: " + movies_df["movie_description"]
        movies_df["page_content"] = movies_df["page_content"].str.replace('\\n', '\n')

        # Select page_content and source columns
        movies_df = movies_df[["page_content", "source"]]

        # Load the documents from the dataframe into docs
        docs = DataFrameLoader(
            movies_df,
            page_content_column="page_content"
        ).load()

        # Print the first 3 documents and the number of documents
        if debug:
            print(f"First 3 documents: {docs[:3]}")
        print(f"Number of documents: {len(docs)}")

        self.docs = docs

    def create_index_on_pinecone(self, index_name):
        # List the names of available indexes. Assign to existing_index_names.
        self.index_name = index_name
        print("Existing Indexes: ", self.pc.list_indexes())

        # First check that the given index does not exist yet
        # create an index if it doesn't exist
        if index_name not in self.pc.list_indexes().names():
            self.pc.create_index(
                name=index_name,
                dimension=1536,
                metric='cosine',
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1"
                ),
            )

            print("Updated Indexes: ", self.pc.list_indexes())


    def upsert_to_pinecone(self, embeddings):
        # Create an index from its name
        index = self.pc.Index(self.index_name)

        # Count the number of vectors in the index
        n_vectors = index.describe_index_stats().get('total_vector_count', 0)
        print(f"There are {n_vectors} vectors in the index already.")

        # Check if there is already some data in the index on Pinecone
        if n_vectors > 0:
            # If there is, get the documents to search from the index. Assign to docsearch.
            docsearch = PineconeVectorStore.from_existing_index(
                self.index_name,
                embeddings
            )
        else:
            # If not, fill the index from the documents and return those docs to assign to docsearch
            docsearch = PineconeVectorStore.from_documents(
                self.docs,
                embeddings,
                index_name=self.index_name
            )

        self.docsearch = docsearch


    def get_relevant_documents_as_retriever(self, question):
        if self.docsearch is None:
            print("Error. Upsert records to pinecone before retrieving")
            return None
        return self.docsearch.as_retriever().get_relevant_documents(question)

