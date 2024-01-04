from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

class ChainOfThoughtComposer(LLMChain):
    def __init__(
            self,
            chat_llm: ChatOpenAI
        ):
        prompt_obj = PromptTemplate(
            input_variables=["query", "functions", "examples"],
            template="""
            You are a helpful chatbot and you need to answer the given query by giving an output in JSON format of the tools,
            argument names, argument values which are needed to solve the query.If the query cannot be solved by the list of tools I provide then outout an empty list.
            The following is the list of tools,argument names,descriptions,examples etc. Understand the functionality of each tool and argument:
            {functions}
            To reference the value of the ith tool in the chain, use $$PREV[i] as argument value. i =
            0, 1, .. j-1; j = current tool’s index in the array
            If the query could not be answered with the given set of tools, output an empty list instead.
            
            Sample Queries and their outputs:
            {examples}

            When given a query you should first think what you should do.
            
            E.g if the query is "Retrieve work items associated with the Rev organisation 'REV-123' and owned by the user 'DEVU-789'" then the thought process should be:
            Based on the given query, my thought process for solving it would be as follows:
            - We need to retrieve work items associated with a specific Rev organisation  and owned by a specific user
            - Since we need to filter for work items, the 'works_list' tool would be useful.
            - Looking at the available arguments for `worklist`, we can see that the `ticket.rev_org` and `owned_by` arguments are relevant to the query.
            - Therefore, we can use the `ticket.rev_org` argument with the value of "REV-123" and the `owned_by` argument with the value of "DEVU-789".
            - The desired output format is in json, so we can create a list of objects (tools) and their respective arguments and values in json format.
            - The first object would be the `works_list` tool with the arguments for `ticket.rev_org` and `owned_by` and their corresponding values.
            - The second object would be the `summarize_objects` tool with the argument for `objects` and the value of "REV-123" from the `works_list` tool.
            {{
                "tool_name": "works_list",
                "arguments": [
                    {{
                    "argument_name": "ticket.rev_org",
                    "argument_value": "REV-123"
                    }},
                    {{
                    "argument_name": "owned_by",
                    "argument_value": "DEVU-789"
                    }}
                ]
            }},
            {{
                "tool_name": "summarize_objects",
                "arguments": [
                    {{
                    "argument_name": "objects",
                    "argument_value": "$$PREV[0]"
                    }}
                ]
            }}]

            if the query is "Summarize issues similar to
            don:core:dvrv-us-1:devo/0:issue/1" then the thought process should be:
            I have to summarize issues similar to "don:core:dvrv-us-1:devo/0:issue/1.
            So I should use the tool "get_similar_work_items" and argument"work_id" and the argument value can be don:core:dvrv-us-1:devo/0:issue/1.
            I also have to summarize so I should use the tool  "summarize_objects" and argument name  "objects".
            

            Understand well the functionalities of the tools and arguments and output in JSON format the tool name, argument name, argument value etc which are needed to solve the following query:
            {query}
            """
        )
        super().__init__(
            llm=chat_llm,
            prompt=prompt_obj
        )
    
    def __call__(self, query: str, functions: list[dict], examples):
        return super().__call__(
            {
                "query": query,
                "functions": functions,
                "examples": examples
            }
        )
