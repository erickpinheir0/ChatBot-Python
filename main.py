from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os

# Configuração da chave da API e endpoint personalizado
os.environ["OPENAI_API_KEY"] = input("Digite sua chave da API Groq: ").strip()
os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"  # Endpoint correto da Groq

# Inicializa o modelo usando LangChain
chat_model = ChatOpenAI(
    model="llama3-70b-8192",  # Substitua pelo modelo correto fornecido pela Groq
    temperature=0.7
)

# Interação simples com o modelo
def chat_with_groq():
    print("Bem-vindo ao Chatbot LangChain + Groq! Digite 'sair' para encerrar.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            print("Chatbot: Até logo!")
            break

        # Enviando mensagem para o modelo
        response = chat_model.invoke([HumanMessage(content=user_input)])
        print(f"Chatbot: {response.content}")

if __name__ == "__main__":
    chat_with_groq()
