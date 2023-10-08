import translators as ts
from telethon import TelegramClient, functions, events, sync, types
import asyncio
import requests

channels_file_url = 'https://raw.githubusercontent.com/Cyzoo/TelGram_Bot_Israel/main/Telgram%20Groups'
channels_urls = requests.get(channels_file_url).text.splitlines()
channels_usernames = [url.split('/')[-1] for url in channels_urls]

report_message = """
Subject: Urgent: Reporting Violation of Community Standards and Terms of Service

Dear Telegram Support,

I hope this message finds you well. I am writing to urgently report a Telegram channel (@channelusername) that is blatantly violating the community standards and terms of service by disseminating extremely violent content and promoting terrorism.

The channel is a propagator of the terror organization Hamas and is actively involved in sharing horrifying visuals of attacks, kidnappings, and killings of both soldiers and innocent civilians, including women and children, in Israel. Such content is not only deeply distressing but also incites violence, hatred, and terrorism, posing a significant threat to public safety and security.

Additionally, there are other associated accounts that, while not directly sharing graphic content, are openly supporting and endorsing these heinous acts of violence and terrorism. This is a clear infringement of Telegram’s policies, and it is imperative to address this issue promptly to ensure the safety and well-being of all users and to maintain the integrity of the Telegram platform.

I kindly request your immediate attention to investigate, suspend, or permanently block these accounts to prevent the further spread of such harmful content. It is essential to take stringent measures against channels that promote terrorism and violence to ensure that Telegram remains a safe and secure platform for all users.

I am confident that Telegram will take this report seriously and act swiftly to address this grave concern. I am available to provide any additional information or clarification required in this regard.

Thank you for your prompt attention and action.
"""

session_name = 'session_name'
api_id = 'api_id'
api_hash = 'api_hash'


async def main():
    # Create a TelegramClient
    client = TelegramClient(session_name, api_id, api_hash)

    # Start the client
    await client.start()

    for channel in channels_usernames:
        try:
            # Get the entity (channel) by username
            entity = await client.get_entity(channel_username)

            # Get the last 20 messages from the channel
            messages = await client.get_messages(entity, limit=20)
            message_ids = [message.id for message in messages]
            result = client(functions.messages.ReportRequest(
                peer=channel_username,
                id=message_ids,
                reason=types.InputReportReasonViolence(),
                message=report_message.replace('channelusername', channel_username)
            ))

        except Exception as e:
            print(f"Error: {e}")

    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
