from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()
app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"
)

##ollama llama2
llm=Ollama(model="llama2-uncensored")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")

##Adding Routes for Essay
add_routes(
    app,
    prompt1|llm,
    path="/essay"
)

##Adding Routes for Poem
add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
