from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole
from data.configs import GIGACHAT_SECRET_B64, GIGACHAT_SCOPE


payload = Chat(
    messages=[
        Messages(
            role=MessagesRole.SYSTEM,
            content="Ты саркастичный и дерзкий бот, который иногда издевается над пользователем, но помогает ему."
        )
    ],
    temperature=0.7,
    max_tokens=200,
),100

def get_gigachat_response(promt):
    with GigaChat(credentials=GIGACHAT_SECRET_B64, scope=GIGACHAT_SCOPE, verify_ssl_certs=False) as giga:
        response = giga.chat(promt)
        return response.choices[0].message.content
