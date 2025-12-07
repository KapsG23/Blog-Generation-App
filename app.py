## we will be able to call build_topic_graph(from graph_builder) as an API.
## with the help of API we should try to call this graph and use its functionalities and execute the graph.
import uvicorn
from fastapi import FastAPI,Request
from src.graphs.graph_builder import GraphBuilder
from src.llms.groqllm import GroqLLM

import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

## Creating our APIs
## Always keep in mind that we have to keep the API running so as to make the langgraph studio run and make use of it.
@app.post("/blogs")
## we should be able to retrieve the  key-value pairs in request variable.(that is when we are doing the post request)
async def create_blogs(request: Request):
    data = await request.json()
    topic = data.get("topic","")
    language = data.get("language","")


    ## get the llm object.
    groqllm = GroqLLM()
    llm = groqllm.get_llm()

    ## get the graph
    graph_builder = GraphBuilder(llm)
    if topic and language:
        graph = graph_builder.setup_graph(usecase="language")
        ## graph will run the entire language_graph.
        state = graph.invoke({"topic":topic,"current_language":language.lower()})

    elif topic:
        graph = graph_builder.setup_graph(usecase="topic")
        ## graph will run the entire build_topic_graph
        state = graph.invoke({"topic":topic})
        
    ## returning the data with respect to the particular state given above.
    return {"data":state}

if __name__ == "__main__":
    ## reload whenever i make any changes.
    ## 0.0.0.0 is basically referring to the localhost.
    uvicorn.run("app:app",host="0.0.0.0",port=8000,reload=True)