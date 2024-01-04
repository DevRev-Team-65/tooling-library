from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import BooleanOutputParser


class Verifier(LLMChain):
    def __init__(
            self,
            chat_llm: ChatOpenAI
        ):
        prompt_obj = PromptTemplate(
            input_variables=["functions", "answer", "query"],
            template='''You are given some tools - 

            {functions}

            answer only True or False - 

            Will this function Schema - 

            {answer}

            satisfy this request - 

            {query}

            A reminder to answer only True or False. 
            '''
        )
        super().__init__(
            llm=chat_llm,
            prompt=prompt_obj
        )
    
    def __call__(self, answer: str, init_functions: list[dict], query: str):
        return super().__call__(
            {
                "functions": init_functions,
                "answer": answer,
                "query": query
            }
        )

