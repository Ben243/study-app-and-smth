import psycopg2
from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

# DATABASE_URL = os.environ["DATABASE_URL"]
DATABASE_URL = 'postgresql+psycopg2://postgres:postgres@pgdb:5432/study_app'


# conn = psycopg2.connect(DATABASE_URL)
# cur = conn.cursor()
# cur.close()
# conn.close()

engine = create_engine(DATABASE_URL)

def send_query(query):
    with engine.connect() as connection:
        result = connection.execute(query)
        connection.close()
        return result.fetchall()

def update_query(query):
    with engine.connect() as connection:
        connection.execute(query)
        connection.commit()
        connection.close()
        return True
    return False


class Base(DeclarativeBase):
    pass

class Problem(Base):
    __tablename__ = "Problem"

    problemid: Mapped[int] = mapped_column(primary_key=True)
    textbookid: Mapped[str] = mapped_column()
    topicid: Mapped[str] = mapped_column()
    problemno: Mapped[int] = mapped_column()
    problemquestion: Mapped[str] = mapped_column()
    problemsolution: Mapped[str] = mapped_column()
    problemstate: Mapped[str] = mapped_column()

class Textbook(Base):
    __tablename__ = "Textbook"

    textbookid: Mapped[int] = mapped_column(primary_key=True)
    textbookname: Mapped[str] = mapped_column()
    textbookfilepath: Mapped[str] = mapped_column()
    textbookstate: Mapped[str] = mapped_column()

class Topic(Base):
    __tablename__ = "Topic"

    topicid: Mapped[int] = mapped_column(primary_key=True)
    textbookid: Mapped[str] = mapped_column()
    topicdescription: Mapped[str] = mapped_column()
    topicstate: Mapped[str] = mapped_column()

def create_problem(textbook, topic, problem_number, problem_question, problem_solution, problem_state):
    # create a new problem in the database
    # query = "INSERT INTO problems (problem_text) VALUES ('This is a test problem')"
    # update_query(query)
    with Session(engine) as session:
        new_problem = Problem(
            textbookid=textbook,
            topicid=topic,
            problemno=problem_number,
            problemquestion=problem_question,
            problemsolution=problem_solution,
            problemstate=problem_state
        )
        session.add(new_problem)
        session.commit()