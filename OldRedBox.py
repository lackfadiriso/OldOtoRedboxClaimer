import string, asyncio, time, random, pyautogui, webbrowser,pyperclip
from bilgilerim import binance_username, binance_password
from telethon import TelegramClient, events

#Telegram
api_id = 'enter Telegram api_id'
api_hash = 'enter Telegram api_hash'

targets = ['panda_task','Crypto_Box_Code_Binance', 'UnlimitedBinanceBoxes', 'Chat_CryptoBoxSuper',
                'Luckyboxs', 'SHN_Crypto', 'BARISYILDIZ_live', 'BIGBOCSESSS', 'crypto_box_free_binance'] #You can add Telegram Channel. Follow the Telegram channels listed in Targets. Remove the channels from Targets if you are not following them on Telegram.
client = TelegramClient('session_name', api_id, api_hash)

def aç():
    try:
        openImage = pyautogui.locateOnScreen('open.png')
        if openImage is not None:
            open_merkez = pyautogui.center(openImage)
            pyautogui.sleep(1)
            pyautogui.moveTo(open_merkez.x, open_merkez.y)
            pyautogui.click()
        else:
            raise pyautogui.ImageNotFoundException("Resim bulunamadı.")
    except pyautogui.ImageNotFoundException:
        pass


async def process_old_messages():
    url = "https://www.binance.com/en/my/wallet/account/payment/cryptobox"
    webbrowser.open(url)
    time.sleep(5)
    for chat_id in targets:
        async for message in client.iter_messages(chat_id, limit=None):
            if message.text and len(message.text) == 8 and message.text.isalnum() and message.text == message.text.upper():
                with open('Kullanildi.txt', 'r+') as dosya:
                    gereksiz = dosya.read()
                    if message.text not in gereksiz:
                        kopyala = pyperclip.copy(message.text)
                        pyautogui.click(1166, 177)
                        pyautogui.click(1163, 267)

                        pyautogui.moveTo(1127, 525)
                        pyautogui.click()
                        pyautogui.click(1251, 512)
                        pyautogui.sleep(1)
                        pyautogui.click(1159, 639)
                        dosya.write('\n' + message.text)
                        pyautogui.sleep(2)
                        aç()
                        time.sleep(random.randrange(2, 4))
                                                                               
           
async def main():
    await client.start()
    me = await client.get_me()
    print(f"Oturum açıldı: {me.first_name}")
    await process_old_messages()
    # İstemciyi çalışır durumda tutma
    await client.run_until_disconnected()

# Ana işlevi çağırma
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("By By...👋")
except TimeoutError:
    print("İnternet Bağlantısı Yok Yada Zayıf")
