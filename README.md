# Musically Bot

Musically Bot is a Discord bot designed to enhance your server's music experience by allowing users to play audio directly from YouTube. It connects to the voice chat, manages request queues, and supports track skipping.

## Features

- **Play Music from YouTube**: Search and play music from YouTube within your Discord voice channels.
- **Queue Management**: Add music requests to a waiting queue, ensuring a continuous music experience.
- **Control Playback**: Commands to pause, resume, and skip tracks easily.

## Installation

### Prerequisites

- Python 3.8 or higher
- A Discord account and server where you have permission to add bots
- YouTube Data API key (if needed)
- FFMPEG (Ensure it is installed and in your system's PATH)

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/musically-bot.git
   cd musically-bot
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
Make sure the requirements.txt containts the following dependencies:
```bash
   discord.py
   youtube_dl
   PyNacl
   FFMPEG
```
3. **Configure the bot**

Edit the bot.py file to replace the token placeholder with your actual Discord bot token:
  ```bash
client.run("YOUR_DISCORD_BOT_TOKEN")
```
3. **Run the bot**
Launch the bot with the following command:
```bash
   python bot.py
```
## Usage
Once the bot is added to your Discord server, you can use the following commands:

**•?join**: Bot joins the user's current voice channel.
	
**•?disconnect**: Disconnect the bot from the voice channel.
  **•?play <song name or URL>**: Add a song by name or YouTube URL to the queue and play it.
	
**•?skip**: Skip the current track and play the next in the queue.

**•?pause**: Pause the currently playing track.

**•?resume**: Resume the paused track.

## Technical Details

### Data Structures
	
 Uses a queue (wait_list) to manage music requests.
	
### Libraries
	
   **•discord.py** for interacting with the Discord API and managing voice chat.
 
   **•youtube_dl** for retrieving audio streams from YouTube.
 
   **•FFmpeg** for streaming audio to Discord.
   **•PyNacl** for voice encryption and compatibility with discord.py
 
## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

1.Fork the repository

2.Create a feature branch (git checkout -b feature/YourFeature)

3.Commit your changes (git commit -m 'Add YourFeature')

4.Push to the branch (git push origin feature/YourFeature)

5.Open a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Thanks to the creators of discord.py and youtube_dl for their incredible libraries.
