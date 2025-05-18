# 🎵 Discord Music Bot

A simple Discord bot written in Python that provides slash commands to play music from YouTube directly in your voice channels.

---

## 📌 Features

* ✅ Play YouTube songs directly via slash commands
* ✅ Queue management
* ✅ Volume control
* ✅ Display current song
* ✅ Easy deployment with Docker

---

## 🚀 Getting Started

### 📦 Prerequisites

* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)
* Discord bot token ([Discord Developer Portal](https://discord.com/developers/applications))

---

### ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/discord-music-bot.git
cd discord-music-bot
```

Create a `.env` file in the project root and add your Discord bot token:

```env
DISCORD_TOKEN=your_discord_bot_token_here
```

---

### 🐋 Docker deployment

Build and run the bot using Docker Compose:

```bash
docker compose up -d --build
```

---

## 🎛️ Usage

After deployment, use these slash commands in Discord:

* `/play [song_name]` : Play a song from YouTube.
* `/queue` : Display the current song queue.
* `/volume [0-100]` : Adjust playback volume.
* `/leave` : Disconnect the bot from the voice channel.
* `/h` : Display help message.

---

## 🛠️ Technologies

* **Python 3.12**
* **Pycord (Discord API)**
* **yt-dlp** (YouTube audio extraction)
* **Docker & Docker Compose**

---

## 🔗 Adding bot to your Discord server

* Visit [Discord Developer Portal](https://discord.com/developers/applications).
* Select your bot and navigate to OAuth2 URL Generator.
* Choose permissions: `applications.commands`, `bot`, `voice` (`Connect`, `Speak`).
* Generate and open the URL, then add your bot to your Discord server.

---

## ⚠️ Important Notes

* Keep your Discord token **private** and never share it publicly.
* Ensure you have permission to stream music content.

---

## 📝 License

MIT License © [ekomlenovic](https://github.com/ekomlenovic)
