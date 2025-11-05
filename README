
# Finance Management API

A **Python-based FastAPI backend** for managing personal finances - featuring user authentication, transaction tracking, and category management.  

Built with **Python**, **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **Alembic** - structured for scalability and maintainability.

## Tech Stack


- **Language**: Python  
- **Framework**: FastAPI  
- **Database**: PostgreSQL  
- **ORM**: SQLAlchemy  
- **Migrations**: Alembic    
- **Server**: Uvicorn  
## Features

- 🔐 User Authentication & Authorization with JWT and OAuth2

- 💸 Transaction Management (add, update, delete, view)

- 🧂 Argon2 Password Hashing — state-of-the-art cryptographic security

- 🗄️ Database Migrations using Alembic

- ⚙️ Environment-based Configuration

- 🧩 Modular, Scalable Architecture

## Installation & Setup

#### 1️⃣ Clone the repository

```bash
git clone https://github.com/jainmanan2409/finance-management-webapp-python.git
cd finance-management-webapp-python/backend
```

#### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows 
```

#### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

#### 4️⃣ Create a ``.env`` File
In your ``backend/`` directory, create a ``.env`` file with the following contents:
```bash
DATABASE_URL=postgresql+psycopg2://<username>:<password>@localhost/<dbname>
SECRET_KEY=<your_secret_key>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Make sure to add ``.env`` to ``.gitignore`` so your secrets are never pushed to GitHub.

## Database Setup

#### Initialize Migrations
```bash
alembic revision --autogenerate -m "initial migration"
```

#### Apply Migrations
```bash
alembic upgrade head
```

#### If your tables already exist:
```bash
alembic stamp head
```
## Run the Application

#### Start your FastAPI server:
```bsh
uvicorn app.main:app --reload
```
FastAPI auto-generates Swagger UI:

- **Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)


## Transactions & Categories

Transactions are divided into **predefined categories** — you cannot add or modify them manually.

The two available categories are:

- `INCOME`
- `EXPENSE`

Each transaction must specify its `type` (`INCOME` or `EXPENSE`), `amount`, and optional `note`.

Example payload:

```json
{
  "amount": 2500.00,
  "type": "INCOME",
  "note": "Salary credited"
}
```


## 🔐 Authentication

- Register a user at `/create`
- Login at `/login` to get a JWT access token
- Use the token in the **Authorize** button in Swagger or as a Bearer token in requests


## 🧰 Troubleshooting

- If migrations fail due to existing data, clear your database or use Alembic revision commands.
- Ensure your database URL in `config.py` matches your PostgreSQL instance.
- If auth fails, regenerate your `SECRET_KEY`.


## 🧩 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repo 🍴
2. Create a new branch for your feature/fix
3. Commit and push changes
4. Submit a Pull Request with clear details


## 🪄 Future Enhancements

- Add frontend (React/Next.js or similar)
- Introduce user-defined categories
- Add analytics dashboard for visualizing income/expenses


## 🤝 Credits

Developed with ❤️ by **Manan Jain**.

If you find this project useful:

- ⭐ Star the repo on GitHub
- 🪶 Fork and customize it
- 🗨️ Share feedback and ideas for improvements



> “Track your finances. Control your future.”
