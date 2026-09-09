import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

app = FastAPI()

load_dotenv()

DATABASE_URL = os.getenv("MYSQL_DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100))


Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()

    rows = "".join(
        f"<tr><td>{user.id}</td><td>{user.name}</td><td>{user.email}</td></tr>"
        for user in users
    )
    return HTMLResponse(
        f"""
        <html>
            <head><title>Users</title></head>
            <body>
                <h1>Stored Users</h1>
                <table border="1" cellpadding="8">
                    <tr><th>ID</th><th>Name</th><th>Email</th></tr>
                    {rows}
                </table>
            </body>
        </html>
        """
    )


@app.post("/users")
def create_user(name: str, email: str):
    db = SessionLocal()
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.close()
    return {"message": "User created"}


@app.get("/users")
def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users
