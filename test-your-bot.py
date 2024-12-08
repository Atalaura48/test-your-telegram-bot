import asyncio
import sys
import os
import io
from telegram import Bot
from telegram.error import InvalidToken

sys.path.append(os.path.join(os.path.dirname(__file__), 'diger'))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def load_language(language_code):
    if language_code == 'tr':
        import tr
        return tr.get_messages()
    elif language_code == 'fr':
        import fr
        return fr.get_messages()
    elif language_code == 'de':
        import de
        return de.get_messages()
    elif language_code == 'hi':
        import hi
        return hi.get_messages()
    else:
        import en
        return en.get_messages()

async def get_updates():
    while True:
        print("1. English")
        print("2. Türkçe")
        print("3. Français")
        print("4. Deutsch")
        print("5. हिंदी")
        
        language_choice = input("")

        if language_choice == '1':
            language = 'en'
            break
        elif language_choice == '2':
            language = 'tr'
            break
        elif language_choice == '3':
            language = 'fr'
            break
        elif language_choice == '4':
            language = 'de'
            break
        elif language_choice == '5':
            language = 'hi'
            break
        else:
            continue

    lang = load_language(language)
    
    while True:
        TOKEN = input(lang['enter_token'])

        try:
            bot = Bot(token=TOKEN)
            first_message = True

            bot_info = await bot.get_me()
            bot_user_id = bot_info.id

            while True:
                updates = await bot.get_updates()

                if not updates:
                    if first_message:
                        print(f"\033[33m{lang['first_message']}\033[0m")
                        first_message = False

                    print(f"\033[33m{lang['no_updates']}\033[0m")
                    await asyncio.sleep(1)
                    continue

                green_color_code = '\033[32m'
                reset_color_code = '\033[0m'

                for update in updates:
                    print(f"{lang['your_chat_id']} {green_color_code}{update.message.chat.id}{reset_color_code}")
                    print(f"{lang['bots_user_id']} {green_color_code}{bot_user_id}{reset_color_code}")

                    while True:
                        test_message = input(f"{lang['test_message_prompt']} ").strip().lower()

                        if test_message == lang['yes']:
                            try:
                                chat_id = update.message.chat.id
                                await bot.send_message(chat_id, lang['working_message'])
                                
                                print(f"{green_color_code}{lang['test_message_sent']}{reset_color_code}")
                                return

                            except Exception as e:
                                print(f"\033[31m{lang['error_sending_message']}{e}\033[0m")
                            break

                        elif test_message == lang['no']:
                            print(f"\033[33m{lang['exiting']}\033[0m")
                            return
                        else:
                            print(f"\033[31m{lang['invalid_input']}\033[0m")
                            continue

                break

        except InvalidToken:
            print(f"\033[31m{lang['invalid_token']}\033[0m")
        except Exception as e:
            print(f"\033[31m{lang['error_sending_message']}{e}\033[0m")

asyncio.run(get_updates())
