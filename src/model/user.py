from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    email = Column(String(120), unique=True, nullable=True)

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __repr__(self):
        """
        Define a string representation for the User model.
        """
        return f"<User(id={self.id}, name={self.name}, email={self.email}>"
