from sqlalchemy import create_engine, Column, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from bot.config import Config

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True, nullable=False)
    thumbnail = Column(String, nullable=True) # ꜰɪʟᴇ_ɪᴅ ᴏꜰ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ
    caption = Column(String, nullable=True)

class Database:
    def __init__(self):
        self.engine = create_engine(Config.DB_URI)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def get_user(self, user_id):
        session = self.get_session()
        user = session.query(User).filter_by(user_id=user_id).first()
        if not user:
            user = User(user_id=user_id)
            session.add(user)
            session.commit()
        return user

    def set_thumbnail(self, user_id, file_id):
        session = self.get_session()
        user = session.query(User).filter_by(user_id=user_id).first()
        if user:
            user.thumbnail = file_id
            session.commit()
        else:
            new_user = User(user_id=user_id, thumbnail=file_id)
            session.add(new_user)
            session.commit()

    def get_thumbnail(self, user_id):
        session = self.get_session()
        user = session.query(User).filter_by(user_id=user_id).first()
        return user.thumbnail if user else None

db = Database()
