from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# 1. Asegurar el TOKEN de cualquien lado
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# 2. Configuracion del Bot
intents = Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents)

# 3. Funcionalidad de los mensajes
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(El mensaje estaba vacio porque no estaban activados los intents)')
        return
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    
    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# 4. Lanzamiento del Bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


# 5. Manejo de mensajes entrantes
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# 6. Uso del TOKEN
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()

