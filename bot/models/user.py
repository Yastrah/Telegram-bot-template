from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from bot.services.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String(length=5), primary_key=True)
    login = Column(String(length=30), nullable=False)
    password = Column(String(length=30), nullable=True)

    # connection with room Project
    projects = relationship(
        "Project", back_populates="user", cascade="all, delete-orphan", lazy="selectin"  # lazy="join"
    )

    @property
    def members_count(self) -> int:
        return len(self.members)

    def __repr__(self):
        return f"{self.__class__.__name__} <id={self.id}, login={self.login}, password={self.password}, projects={self.projects}>"


class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(String(length=5), ForeignKey('user.id'), nullable=False)
    project_name = Column(String(length=30), nullable=False)

    user = relationship("User", back_populates="projects")  # connection with User

    def __repr__(self):
        return f"<project_name={self.project_name}, owner_id={self.owner_id}>"
