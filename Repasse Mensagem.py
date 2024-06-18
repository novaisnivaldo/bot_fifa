from telethon import TelegramClient, sync, events
from time import sleep
import requests
from senhas_particular import api_hash,api_id

sessao = 'Repassagem Mensagem'

def main():
        print ('Monitoriamento iniciado...')
        client = TelegramClient (sessao, api_id, api_hash)
        Size_8m = 100
        ID_BOT_8m = []
        Size_12m = 100
        ID_BOT_12m = []

        @client.on(events.NewMessage(chats = [1001820640022]))
        async def enviar_mensagem(event):
            id_mensagem_8m = await client.send_message(-1002202546001,event.raw_text)
            id_grupo_boot_8m = event.message.id
            id_grupo_reenvio_8m = id_mensagem_8m.id
            if len(ID_BOT_8m) >= Size_8m:
                ID_BOT_8m.pop(0)
            ID_BOT_8m.append([id_grupo_boot_8m,id_grupo_reenvio_8m])

        @client.on(events.MessageEdited(chats = [1001820640022]))
        async def enviar_mensagem(event):
            msg_alt_8m = event.message.id        
            for i in range(len(ID_BOT_8m)):
                if msg_alt_8m == ID_BOT_8m[i][0]:
                    msg_edit_8m = ID_BOT_8m[i][1]
                    break
            await client.edit_message(-1002202546001,msg_edit_8m,event.raw_text)


        @client.on(events.NewMessage(chats = [1001913744023]))
        async def enviar_mensagem(event):
            id_mensagem_12m = await client.send_message(-1002155000646,event.raw_text)
            id_grupo_boot_12m = event.message.id
            id_grupo_reenvio_12m = id_mensagem_12m.id
            if len(ID_BOT_12m) >= Size_12m:
                ID_BOT_12m.pop(0)
            ID_BOT_12m.append([id_grupo_boot_12m,id_grupo_reenvio_12m])

        @client.on(events.MessageEdited(chats = [1001913744023]))
        async def enviar_mensagem(event):
            msg_alt_12m = event.message.id        
            for i in range(len(ID_BOT_12m)):
                if msg_alt_12m == ID_BOT_12m[i][0]:
                    msg_edit_12m = ID_BOT_12m[i][1]
                    break
            await client.edit_message(-1002155000646,msg_edit_12m,event.raw_text)

        client.start()
        client.run_until_disconnected()
main()
