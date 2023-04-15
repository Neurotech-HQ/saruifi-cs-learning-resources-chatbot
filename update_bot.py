from sarufi import Sarufi
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.environ.get('SARUFI_CLIENT_ID')
client_secret = os.environ.get('SARUFI_CLEINT_SECRET')

sarufi = Sarufi(client_id=client_id, client_secret=client_secret)

def update_sarufi_bot():
    updated_Nalah_bot = sarufi.update_from_file(
                            id=331,
                            intents="data/intents.yaml",
                            flow="data/dialog.yaml",
                            metadata="data/metadata.json",
                        )
    return updated_Nalah_bot.data


if __name__ == "__main__":
    print(update_sarufi_bot())

