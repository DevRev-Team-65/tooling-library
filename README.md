# Agent 007 Team 65

Convert queries to tool-code using langchain and openai

## Introduction

This library is an implementation of the problem statement. Here we use gpt-4 as the primary backend and langchain as the framework to achieve our results. The task is divided into retrieval and composition. The retrieval part is done using langchain's retrievers and the composition part is done using langchain's composers. The output of the composer is parsed using the output parser.

## Prerequisites

- Python 3.10
- openai
- langchain
- sentence_transformers (optional)
- huggingface_hub (optional)

## Example

```python

from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI

from src.retrievers import VectorStoreRetriever
from src.composers import ChainOfThoughtComposer
from src.functions import devrev_functions
from src.examples import example_queries

# Initialize the chat object

chat_llm = ChatOpenAI(
    openai_api_key = "<YOUR_API_KEY>",
    temperature=0.7,
)

# Generate Examples

example_str = "".join([f"Query: {query} Answer:\n {functions}" for query, functions in example_queries[:4]])

# Retrievers can be chained together to form a pipeline, with vs_retriever being the most basic

vs_retriever = VectorStoreRetriever(
    embeddings=OpenAIEmbeddings(
        openai_api_key = "<YOUR_API_KEY>"
    ),
    name = "vs_rtr_01",
    init_functions=devrev_functions.copy()
)

cmq_retriever = CustomMultiQueryRetriever(
    chat_llm = ChatOpenAI(
        openai_api_key = "<YOUR_API_KEY>",
        temperature=0.7
    ),
    vector_store=vs_retriever
)

cot_composer = ChainOfThoughtComposer(
    chat_llm=chat_llm,
)

def agent(query):
    # Retrieve functions
    retrieved_functions = cmq_retriever.retrieve(query)

    # Compose answer
    answer = cot_composer(query, retrieved_functions, example_str)

    # Return answer
    return answer['text']

```

## Documentation

### `src`

It is the core library that contains the retrievers, composers, and few functions along with some base examples to begin with

-   ### `src.retrievers`

    It contains the retrievers that are used to retrieve the functions that are similar to the query. They can cascade into each other to form a pipeline.

    -   ##### `src.retrievers.VectorStoreRetriever`

        It is the most basic FAISS based retriever that uses the embedding similarities to retrieve relevant functions.

        **\_\_init\_\_** Initializes the retriever

        -   `embeddings: langchain.embeddings`: The embeddings that are used to generate the embeddings of the functions and the query

        -   `name: str`: The name of the retriever, used for caching

        -   `init_functions: list[dict]`: The functions that are used to initialize the retriever

        **add_functions** Adds the functions to the retriever

        -   `functions: list[dict]`: The functions that are added to the retriever

        **find_functions** Returns the functions that are similar to the query

        -   `query: str`: The query that is used to retrieve the functions

        **get_retriever** Returns the retriever object

    -   ##### `src.retrievers.CustomMultiQueryRetriever`

        It is a retriever that uses the chat model to break the query into multiple queries and then uses the vector store retriever to retrieve the functions.

        **\_\_init\_\_** Initializes the retriever

        -   `chat_llm: langchain.chat_models`: The chat model that is used to generate the query

        -   `vector_store: src.retrievers.VectorStoreRetriever`: The vector store retriever that is used to retrieve the functions

        **find_functions** Returns the functions that are similar to the query

        -   `query: str`: The query that is used to retrieve the functions
    
    -   ##### `src.retrievers.CustomContextualCompressionRetriever`
    
        It is a retriever that uses contextual compression to store documents and infer the query. It uses the vector store retriever to retrieve the functions.

        **\_\_init\_\_** Initializes the retriever

        -   `chat_llm: langchain.chat_models`: The chat model that is used to generate the query

        -   `vector_store: src.retrievers.VectorStoreRetriever`: The vector store retriever that is used to retrieve the functions

        **find_functions** Returns the functions that are similar to the query

        -   `query: str`: The query that is used to retrieve the functions

-   ### `src.composers`

    It contains the composers that are used to generate the answer based on the query and the retrieved functions. These composers are built upon langchain's LLMChain classess and can inherit directly from them.

    -  ##### `src.composers.ChainOfThoughtComposer`

        This uses chain of thought to compose the retrieved function into a meaningful task as specified by the query.

        **\_\_init\_\_**

        -   `chat_llm: langchain.chat_models`: The chat model that is used to generate the answer

        **\_\_call\_\_**

        -   `query: str`: The query that is used to generate the answer

        -   `functions: list[dict] | list[Document()]`: The functions that are retrieved by the retriever

        -   `examples: str`: The examples that are used to generate the answer, from `src.examples`


- #### `src.functions`

    It contains the functions that are used to initialize the retrievers. The functions are taken from the dataset provided by devrev

- #### `src.examples`

    It contains the examples that are passed along with the composer, it is a list of query-result pairs that are used to generate the answer.
    The ideal way to process it is:
    
    ```python
    example_str = "".join([f"Query: {query} Answer:\n {functions}" for query, functions in example_queries[:4]])
    ```
    However the user is free to process it however they want.