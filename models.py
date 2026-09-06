from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Task(Base):
   __tablename__ = "tasks"
   id : Mapped[int] = mapped_column(primary_key = True)
   title : Mapped[str] = mapped_column()
   description : Mapped[str] = mapped_column()
   completed : Mapped[bool] = mapped_column()
   created_at : Mapped[datetime] = mapped_column(default = datetime.utcnow)
   updated_at : Mapped[datetime] = mapped_column(
       default= datetime.utcnow,
       onupdate = datetime.utcnow
   )