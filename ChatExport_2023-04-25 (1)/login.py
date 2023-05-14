from telethon.sync import TelegramClient, events

# Your API ID and API hash obtained from https://my.telegram.org
api_id = 12345
api_hash = "0123456789abcdef0123456789abcdef"

# Your phone number with the country code, without '+' or '00'
phone_number = "1234567890"

# The name or username of the group or channel to export
entity_name = "mygroup"

# The path to the file to save the exported chat to
export_file = "exported_chat.txt"

# Create a new Telegram client
client = TelegramClient("session_name", api_id, api_hash)

# Define an event handler to handle incoming messages


@client.on(events.NewMessage(chats=entity_name))
async def handler(event):
    with open(export_file, "a", encoding="utf-8") as f:
        f.write(f"{event.raw_text}\n")


# Start the client and log in
client.start(phone_number)

# Prompt the user to enter the verification code
code = input("Please enter the verification code: ")

# Sign in to the account  with the verification code
client.sign_in(code=code)

# Get the entity (group or channel) to export
entity = client.get_entity(entity_name)

# Export the chat
for message in client.iter_messages(entity):
    pass  # The handler will write the messages to the file

# Stop the client
client.disconnect()
