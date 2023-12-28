from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

from langchain.schema import HumanMessage

llm = OpenAI(openai_api_key="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")
chat_model = ChatOpenAI(openai_api_key="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")


text = "What would be a good company names for a company that makes colorful shoes?"
messages = [HumanMessage(content=text)]

llm.invoke(text)
# >> Feetful of Fun

chat_model.invoke(messages)
# >> AIMessage(content="Socks O'Color")




