# V H GitHub Unzipper Bot

A Discord bot that downloads and extracts GitHub repositories, then sends the files to users via DM.

---

## Features

✅ Password-protected access  
✅ Validates GitHub repository links  
✅ Downloads and extracts repositories  
✅ Sends all extracted files to the user’s DM  
✅ Automatically deletes temporary files  
✅ Professional message responses  

---

## Setup & Installation

### 1️⃣ Install Dependencies
Run the following command to install the required libraries:
```sh
pip install discord requests aiohttp
```

### 2️⃣ Configure the Bot
- Open `bot.py` and replace `"YOUR_BOT_TOKEN"` with your actual Discord bot token.  
- The default password is **`vhop5111lol`**, but you can change it inside `bot.py`.  

### 3️⃣ Run the Bot
Start the bot with:
```sh
python bot.py
```

---

## Commands

| Command | Description |
|---------|-------------|
| `$gitunzip` | Starts the unzip process |

---

## How It Works

1️⃣ **User enters** `$gitunzip`.  
2️⃣ **Bot asks for password** → Enter the correct password.  
3️⃣ **Bot asks for a GitHub repository link** → Provide a valid link (e.g., `https://github.com/user/repo`).  
4️⃣ **Bot downloads, unzips, and sends files** to the user’s DM.  
5️⃣ **Bot cleans up temporary files** and closes the connection.  

---

## Example Usage

```sh
User: $gitunzip  
Bot: Welcome To V H GITUNZIPER BOT! Please enter the correct password to continue.  
User: Type the password 
Bot: ✅ Password correct! Now send a valid GitHub repository link.  
User: https://github.com/user/repo  
Bot: ⏳ Downloading & Unzipping... Please wait.  
Bot: ✅ Repository Unzipped! Sending files...  
Bot: ✅ Thank you for using V H GITUNZIPER!  
Bot: 🔒 Connection Closed.  
```

---

## Troubleshooting

- **Bot not sending files?** → Check if your DMs are open.  
- **Wrong password?** → Try again with the correct password.  
- **Invalid GitHub link?** → Ensure it’s a valid repository link.  
- **Bot not responding?** → Restart the bot and try again.  

---

## Contributing

Feel free to improve the bot by submitting pull requests!  

---

## License

Mit License .  
