from database import db_session
from sqlalchemy.exc import SQLAlchemyError
from src.model.user import User


class UserRepository:

    def get_all_user(self):
        return db_session.query(User).all()

    def get_user_by_id(self, id: int):
        return db_session.query(User).filter_by(id=id).first()

    def create_user(self, user: User):
        try:
            db_session.add(user)
            db_session.commit()
            return True
        except SQLAlchemyError as e:
            db_session.rollback()
            print(f"Error creating user: {e}")
            return False
