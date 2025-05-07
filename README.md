# Telegram Bot Template 🚀

![build](https://img.shields.io/badge/build-passing-orange)
![demo](https://img.shields.io/badge/demo-ready-green)
![version](https://img.shields.io/badge/version-1.0.3-blue)


A robust and scalable Telegram bot template built with **Python**, **Aiogram**, **SQLAlchemy**, and **Poetry**. This template is designed to help you kickstart your Telegram bot development with best practices, including logging, testing, and database integration.

---

## Features ✨

- **Aiogram**: A modern and fully asynchronous framework for Telegram Bot API.
- **SQLAlchemy**: Powerful ORM for database management, supporting PostgreSQL, MySQL, SQLite, and more.
- **Poetry**: Dependency management and packaging made easy.
- **Logging**: Built-in logging for better debugging and monitoring.
- **Testing**: Ready-to-use pytest setup for unit and integration testing. **_(not done yet)_**
- **Modular Structure**: Clean and organized codebase for easy scalability.
- **Environment Variables**: Secure configuration using `.env` files.

---

## Getting Started 🛠️

### Prerequisites

- Python 3.9+
- Poetry (for dependency management)
- Telegram Bot Token (get it from [BotFather](https://core.telegram.org/bots#botfather))

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Yastrah/Telegram-bot-template.git
   cd Telegram-bot-template
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Set up your environment variables:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Update `.env` with your Telegram bot token and database credentials:
     ```env
     BOT_TOKEN=your-telegram-bot-token
     DATABASE_URL=sqlite:///./database.db
     ```

4. Run the bot:
   ```bash
   poetry run python -m bot
   ```

---

## Project Structure 📂

```
telegram-bot-template/
├── bot/                   # Main bot application
│   ├── keyboards/         # Custom keyboards
│   ├── middlewares/       # Custom middlewares
│   ├── models/            # Database models (SQLAlchemy)
│   ├── routers/           # Events routers
│   ├── services/          # Business logic and services
│   ├── utils/             # Utility functions and helpers
│   ├── __init__.py        # Bot initialization
│   ├── config.ini         # Bot config with main info
│   ├── config_reader.py   # Parser for config file
│   ├── states.py          # Custom states
│   └── template_engine.py # Parser for HTML files
├── templates/             # HTML files for bot dialogues
├── .env.example           # Environment variables template
├── app.py                 # Entry point for the bot
├── poetry.lock            # Poetry lock file
├── pyproject.toml         # Poetry project configuration
└── README.md              # Project documentation
```

---

## Logging 📝

The bot uses Python's built-in `logging` module for structured and configurable logging. Logs are output to the console and saved to `logs/bot.log`.

Example log output:
```
2025-04-23 10:08:34 [INFO] __main__: Bot started successfully!
2025-04-23 10:09:12 [DEBUG] router: Received message: Hello, bot.
```

---

## Testing 🧪 **_(not done yet)_**

The project includes a `pytest` setup for unit and integration testing. To run tests:

```bash
poetry run pytest
```

---

## Database Integration 🗄️ **_(not done yet)_**

The bot uses **SQLAlchemy** for database operations. By default, it uses SQLite, but you can easily switch to PostgreSQL, MySQL, or any other supported database by updating the `DATABASE_URL` in `.env`.

Example model:
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
```

---

## Contributing 🤝

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

---

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Versioning 🏷️

**Current Version:** `v1.0.0`

We use [Semantic Versioning](https://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your-username/telegram-bot-template/tags).

---

## Acknowledgments 🙏

- [Aiogram](https://docs.aiogram.dev/) for the Telegram Bot API framework.
- [SQLAlchemy](https://www.sqlalchemy.org/) for database management.
- [Poetry](https://python-poetry.org/) for dependency management.

---

## Support 💬

If you have any questions or need help, feel free to open an issue or contact me directly.

---

Enjoy building your Telegram bot! 🤖✨

---