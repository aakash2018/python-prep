from langchain_openai import ChatOpenAI

# Apni OpenAI API key yahan paste karo
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0    
)

response = llm.invoke("Hello, chatbot!")
print(response.content)
