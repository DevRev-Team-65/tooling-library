from .vectorstore import VectorStoreRetriever
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class LineList(BaseModel):
    '''
    LineList is a pydantic object that contains a list of strings
    '''
    lines: list[str] = Field(description="Lines of text")


class LineListOutputParser(PydanticOutputParser):
    '''
    LineListOutputParser is a wrapper around PydanticOutputParser that parses the output of the LLM into a list of strings
    '''
    def __init__(self) -> None:
        super().__init__(pydantic_object=LineList)

    def parse(self, text: str) -> LineList:
        lines = text.strip().split("\n")
        return LineList(lines=lines)
    
class CustomMultiQueryRetriever(MultiQueryRetriever):
    '''
    CustomMultiQueryRetriever is a wrapper around MultiQueryRetriever that allows for easy addition of functions and queries
    '''
    def __init__(self, chat_llm, vector_store):
        prompt_obj = PromptTemplate(
            input_variables=["question"],
            template="""Your task is to break down the question into a list different steps.
            The steps should be as specific as possible. Your goal is to have the task broken
            minimum number of simpler atomic steps.
            
            Example question: Prioritize my P0 issues and add them to the current sprint
            Example answer:
            1. Get my id
            2. Find my P0 issues using id
            3. Prioritize my P0 issues from #2
            4. Get the current sprint id
            5. Add issues from #2 to the sprint from #4

            Now solve the following question
            Original question: {question}""",
        )
        output_parser_obj = LineListOutputParser()
        llm_chain = LLMChain(llm=chat_llm, prompt=prompt_obj, output_parser=output_parser_obj)
        super().__init__(
            retriever=vector_store.get_retriever(),
            llm_chain = llm_chain,
            parser_key='lines'
        )
    
    def find_functions(self, query: str):
        docs = super().get_relevant_documents(query)
        return docs