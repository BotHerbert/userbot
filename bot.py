from telethon import TelegramClient, events, functions

from telethon.tl.types import User

# Replace the values below with your own API credentials

api_id = 988074

api_hash = 'a5ec8b7b6dbeedc2514ca7e4ba200c13'

session_name = 'neww'

client = TelegramClient(session_name, api_id, api_hash)

mystat = 1

@client.on(events.NewMessage)

async def handle_new_message(event):

    global mystat

    if event.is_private:

        if '/мета' in event.raw_text.lower():

            user = await event.get_chat()

            user_link = "Пожалуйста, не используйте мета вопросы. Они тратят время! И ваше, и других людей, которые пытаются вам помочь! Вы стараетесь быть вежливым, не переходя сразу к своей проблеме, как люди делают при личной встрече. Но чат — это совсем другое. Люди печатают намного медленнее, чем говорят. Вместо проявления вежливости, вы заставляете другого человека ждать, пока сформулируете вопрос, что приводит к потере производительности."

            await event.reply(user_link)

            if '/мета' in event.raw_text.lower():

                # Delete bot's message

                await event.delete()

        if '/словарь' in event.raw_text.lower():

            # Block user

            user = await event.get_chat()

            user_link = "Вот, держи, воспользуйся словарём: http://www.gramota.ru/slovari/info/lop/"

            await event.reply(user_link)

            if '/словарь' in event.raw_text.lower():

                # Delete bot's message

                await event.delete()

        if '/бан' in event.raw_text.lower():

            # Block user

            user = await event.get_chat()

            user_link = f"[{user.first_name}](tg://user?id={user.id})"

            await event.reply(f'{user_link} заблокирован')

            await client(functions.contacts.BlockRequest(user))

            if '/бан' in event.raw_text.lower():

                # Delete bot's message

                await event.delete()

        if '/сплю' in event.raw_text.lower():

            mystat = 2

            await event.reply('Статус сплю поставлен. Спокойной ночи, Господин')

		if '/онлайн' in event.raw_text.lower():            mystat = 1

            await event.reply('Статус онлайн поставлен.')

        if '/занят' in event.raw_text.lower():

            mystat = 0

            await event.reply('Статус занят поставлен.')

        if mystat == 0:

            await event.reply('Я занят. Скоро вернусь и отвечу.')

            return

		if mystat == 2:

            await event.reply('Я сплю. Скоро проснусь и отвечу.')

            return

            

client.start()

client.run_until_disconnected()
