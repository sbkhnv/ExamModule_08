from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Boolean
from db.database import Base, ENGINE


class ChairsModel(Base):
    __tablename__ = "chairs"
    id = Column(Integer, primary_key=True)
    image = Column(String(30),nullable=True)
    name = Column(String(30),unique=True)
    description = Column(String(30),nullable=True)
    price = Column(Integer,nullable=False)



    def __repr__(self):
        return f"Chair name => {self.name}"


class CommentsModel(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    text = Column(Text,nullable=True)
    image = Column(String(30),nullable=True)
    first_name = Column(String(30),nullable=False)
    las_name = Column(String(30),nullable=False)
    job = Column(String(30),nullable=True)

    def __repr__(self):
        return f"firs_name => {self.first_name} las_name => {self.las_name} text => {self.text}"



class PostsModel(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    image = Column(String(30),nullable=True)
    description = Column(String(30),nullable=True)
    staff_name = Column(String(30),nullable=True)
    create_date = Column(String(30),nullable=True)

    def __repr__(self):
        return f"staff_name => {self.staff_name} description => {self.description}"



class TeamMembersModel(Base):

    __tablename__ = "team_members"

    id = Column(Integer, primary_key=True)
    image = Column(String(30),nullable=True)
    first_name = Column(String(30),nullable=False)
    last_name = Column(String(30),nullable=False)
    job = Column(String(30),nullable=True)
    description = Column(String(30),nullable=True)

    def __repr__(self):
        return f"first_name => {self.first_name} last_name => {self.last_name} job => {self.job}"


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    username = Column(String(25), unique=True, nullable=False)
    email = Column(String(25), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    def __repr__(self):
        return self.first_name