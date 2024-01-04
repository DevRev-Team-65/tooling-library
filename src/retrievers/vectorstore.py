import json
from langchain.schema import Document
from langchain.vectorstores import FAISS

class VectorStoreRetriever:
    '''
    VectorStore is a wrapper around FAISS that allows for easy addition of functions and queries
    '''
    def __init__(self, embeddings, name: str, init_functions: list[dict]):
        self.embeddings = embeddings
        self.init_functions = init_functions
        self.documents = 0
        for i,f in enumerate(init_functions):
            self.init_functions[i] = Document(page_content=json.dumps(f), metadata={"index": self.documents})
            self.documents += 1

        #create a vector store
        try:
            self.vector_store = FAISS.load_local(name, self.embeddings)
        except:
            #no local store
            self.vector_store = FAISS.from_documents(
                self.init_functions,
                self.embeddings
            )
            self.vector_store.save_local(name)
        self.vs_name = name
        self.vs_retriever = self.vector_store.as_retriever()
        self.documents = len(init_functions)
    
    def add_functions(self, function_list: list[dict]):
        for i,f in enumerate(function_list):
            function_list[i] = Document(page_content=json.dumps(f), metadata={"index": self.documents})
            self.documents += 1
        self.vector_store.add_documents(function_list)
        self.vector_store.save_local(self.vs_name)
    
    def find_functions(self, query: str):
        return self.vs_retriever.get_relevant_documents(query)
    
    def get_retriever(self):
        return self.vs_retriever