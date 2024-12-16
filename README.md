# Memhash Auto Mining
**Memhash Miner** is a lightweight, easy-to-setup Python miner for Linux with minimal dependencies.


# About Memhash
First-ever PoW (Proof of Work) Mining on Telegram, fully supported by Pavel Durov, Telegram CEO.
Every mined block carries real token rewards shared among participants. Tokens, not points, are mined through Memhash.

- Start Mining Now: [Click here](https://t.me/memhash_bot/start?startapp=10cFTW).
- Reminder: You need 300 Telegram Stars to Start Mining.

# Features
- Completely optimized for Linux.
- You can choose between two options to start the bot: 
  - Run continuously.
  - Set a mining duration and recharge duration.
- Quick installation and easy configuration.

# Installation and Setup
#### Step 1. Install python3.10 Ubuntu:
```sh
sudo apt update && sudo apt install -y software-properties-common && sudo add-apt-repository -y ppa:deadsnakes/ppa && sudo apt update && sudo apt install -y python3.10 python3.10-venv python3.10-distutils python3-pip
```
#### Step 2. Install Chrome Ubuntu:
```sh
sudo apt-get install -y libxss1 libappindicator1 libindicator7 && wget https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_131.0.6778.85-1_amd64.deb && sudo apt install ./google-chrome-stable_131.0.6778.85-1_amd64.deb && sudo apt-get install -f
```
#### Step 3. Clone the repository and install dependencies:
```sh
git clone https://github.com/rinkashimee/memhash-auto-mining.git && cd memhash-auto-mining && pip3 install -r requirements.txt
```
#### Step 4. Configure the URL:
- Open the `web.telegram.org` website and navigate to your Memhash bot.
- Press `F12` to open Developer Tools or Right click and then click inspect.
- Navigate to the `Elements` tab.
- Select the `element picker tool` and click on the `Memhash Window`.

  ![image](https://github.com/user-attachments/assets/f26c8d7c-93ea-4d64-9cf3-fb268f96b714)
  ![image](https://github.com/user-attachments/assets/c17ff85b-03b6-44e0-b7c5-771fe728a660)
  
- Copy the iframe src `URL` and paste into `config.py` `URL = ""`

#### Step 5. Configure your Telegram Bot:
- Go to [Bot Father](https://t.me/BotFather)
- Create a bot and and copy the token provided and paste it into `config.py` `TOKEN = ""`

### Step 6. Add screen:
```sh
screen -S memhash-bot
```
### Step 7. Run the bot:
```sh
python3 main.py
```
# Contact
#### For questions or feedback:
- Telegram: [@rinkashi_me](https://t.me/rinkashi_me)
- Discord: [Join 0xSG AirxNode Community](https://discord.gg/BxDj5ZVj8W)


### This project is distributed under the terms of the ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
