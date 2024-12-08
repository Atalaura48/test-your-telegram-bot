This Python script enables you to interact with the Telegram Bot API to test bot functionality, choose a preferred language, and fetch updates in real time.

## Features

- Multi-language support (English, Turkish, French, German, Hindi).
- Prompts user to enter the Telegram Bot Token.
- Verifies the token and retrieves bot information.
- Fetches and displays Telegram updates in real time.
- Allows users to send a test message to the bot.

## Prerequisites

- Python 3.7 or higher
- `python-telegram-bot` library

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/Atalaura48/test-your-telegram-bot.git
    cd test-your-telegram-bot
    ```

2. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Ensure the following language modules are present in the `diger` folder:

    - `tr.py`
    - `fr.py`
    - `de.py`
    - `hi.py`
    - `en.py`

    Each module should define a function `get_messages()` that returns a dictionary of language strings.

## Usage

1. Run the script:

    ```bash
    python bot_fetcher.py
    ```

2. Select a language from the menu.

3. Enter the Telegram Bot Token when prompted.

4. Follow the prompts to test the bot.

## Sample Language Module

Here’s an example of the English (`en.py`) language module:

```python
def get_messages():
    return {
        'enter_token': "Please enter your Telegram Bot Token: ",
        'first_message': "Fetching updates for the first time...",
        'no_updates': "No new updates found.",
        'your_chat_id': "Your chat ID is:",
        'bots_user_id': "Bot's user ID is:",
        'test_message_prompt': "Do you want to send a test message? (yes/no): ",
        'working_message': "The bot is working correctly!",
        'test_message_sent': "Test message sent successfully.",
        'error_sending_message': "Error sending message: ",
        'invalid_input': "Invalid input, please try again.",
        'exiting': "Exiting the application.",
        'invalid_token': "The provided token is invalid."
    }
```

## Notes

- Ensure your bot token is valid and has permissions to fetch updates and send messages.
- The script uses ANSI color codes for console output.

## Open Source

This project is open source and is hosted on GitHub. Contributions are welcome!

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. All contributions are welcome!

## License

This project is licensed under the MIT License.

## Repository

You can find the repository here: [GitHub - Atalaura48/test-your-telegram-bot](https://github.com/Atalaura48/test-your-telegram-bot)
