# Happy Squad Discord Bot

A small Discord bot that provides a few helpful slash commands, welcome/logging functionality, and server helper utilities for a Hungarian-speaking community.

This repository contains a simple bot built with discord.py (commands extension + app commands). The bot loads a few cogs on startup and synchronizes slash commands to a configured guild.

## Features

- Slash commands (app commands) for quick access to server rules and help.
- Welcome and logging cogs (loadable from `cogs/`) to handle member joins and message logging.
- Configurable via environment variables (uses a `.env` file when present).

## Files of interest

- `main.py` — Bot bootstrap: sets intents, loads cogs, syncs slash commands, and starts the bot.
- `cogs/commands.py` — Example slash commands (`/rules`, `/help`).
- `cogs/welcome.py` — Welcome-related logic (loaded by `main.py`).
- `cogs/logs.py` — Logging-related logic (loaded by `main.py`).
- `requirements.txt` — Python dependencies.

## Prerequisites

- Python 3.11+ (project appears to use features and packaging aligned with modern Python; adjust as needed).
- A Discord application with a bot token. You'll need to invite the bot to your server with the correct scopes and intents.

Make sure the bot application has the following privileged intents enabled in the Discord Developer Portal if you plan to use member/message features:

- Server Members Intent
- Message Content Intent

## Installation

Clone the repository and install dependencies:

```powershell
git clone https://github.com/Robesz0021/happy-squad-discord-bot.git
cd happy-squad-discord-bot
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root (the project already uses `python-dotenv`) and add the required variables. Example:

```
DISCORD_BOT_TOKEN=your_bot_token_here
GUILD_ID=123456789012345678
RULES_CHANNEL_ID=123456789012345678
HAPPY_ID=123456789012345678
```

- `DISCORD_BOT_TOKEN` — The bot token from the Discord Developer Portal.
- `GUILD_ID` — The Discord Guild (server) ID to which slash commands should be synchronized. The bot's `on_ready` attempts to sync commands for this guild.
- `RULES_CHANNEL_ID` — Channel ID used by `/rules` for linking to the rules channel.
- `HAPPY_ID` — A user ID mentioned by `/help` as the contact person.

Note: If `GUILD_ID` is not provided the code will print an error and will not sync guild-specific slash commands. You can modify `main.py` to sync globally if desired.

## Running the bot

Start the bot from the project root. The repository's `main.py` will load the cogs and run the bot.

```powershell
python main.py
```

On startup the bot will:

- Load `cogs.commands`, `cogs.welcome`, and `cogs.logs`.
- Attempt to sync slash commands to the guild defined by `GUILD_ID`.
- Write debug logs to `discord.log` (file created/overwritten on each run).

## How the bot works (brief)

- The bot uses no command prefix for prefix commands (empty string) and relies mainly on app (slash) commands defined in `cogs/commands.py`.
- Slash commands are defined with `@app_commands.command` and the `main.py` syncs them to the configured guild on ready.
- The cogs are standard discord.py Cogs; to add a new cog, create the module in `cogs/` and export an `async def setup(bot)` that adds the cog.

## Development notes

- To add a new slash command, create it as an `@app_commands.command` inside a Cog and load the Cog in `main.py` (or let the bot auto-load the module).
- When changing slash commands, re-run the bot to re-sync the commands to the guild (or add additional sync logic if you want automatic updates).

## Troubleshooting

- Bot doesn't start: ensure `DISCORD_BOT_TOKEN` is set.
- Slash commands not visible: confirm `GUILD_ID` is set and the bot has the application.commands scope in the invite link. Guild sync is faster; global command sync can take up to an hour.
- Permissions errors: ensure the bot has the necessary permissions on the server and that privileged intents are enabled if you use members/message content features.

## Contributing

Contributions are welcome. For small changes:

1. Fork the repository.
2. Create a branch for your feature/fix.
3. Open a pull request describing your changes.

If you plan to add features that change runtime behavior, please include or update tests where applicable.

## License

This project includes a `LICENSE` file in the repository. Please review it for licensing details.

## Contact

If you need help with the project, open an issue or contact the maintainer listed in the repository.

---

Happy coding! :)
