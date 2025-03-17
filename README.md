# **V H GitHub Unziper Bot**

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

MIT License

Copyright (c) 2025 DEVELOPER V H#5111

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

