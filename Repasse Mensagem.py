from telethon import TelegramClient, sync, events
from time import sleep
import requests
from senhas_particular import api_hash,api_id

sessao = 'Repassagem Mensagem'

def main():
        print ('Monitoriamento iniciado...')
        client = TelegramClient (sessao, api_id, api_hash)
        @client.on(events.NewMessage(chats = [1001820640022]))
        async def enviar_mensagem(event):
            await client.send_message(1002202546001,event.raw_text)
        @client.on(events.NewMessage(chats = [1001913744023]))
        async def enviar_mensagem(event):
            await client.send_message(1002155000646,event.raw_text)
        client.start()
        client.run_until_disconnected()
main()
