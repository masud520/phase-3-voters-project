
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class Candidate(Base):
    __tablename__ = 'candidates'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    votes_relation = relationship('Vote', back_populates='candidate')

class Voter(Base):
    __tablename__ = 'voters'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    candidate_id = Column(Integer, ForeignKey('candidates.id'))
    votes = relationship('Vote', back_populates='voter', cascade="all, delete-orphan", passive_deletes=True)
    candidate = relationship('Candidate', back_populates='votes_relation')

class Vote(Base):
    __tablename__ = 'votes'

    id = Column(Integer, primary_key=True)
    voter_id = Column(Integer, ForeignKey('voters.id', ondelete="CASCADE"))
    candidate_id = Column(Integer, ForeignKey('candidates.id'))
    candidate = relationship('Candidate', back_populates='votes_relation', uselist=False)
    voter = relationship('Voter', back_populates='votes')
    votes_relation = relationship('Candidate', back_populates='votes_relation')  # Add this line

# Rest of the code remains the same

# Create the database engine
DATABASE_URL = "sqlite:///vote_database.db"
engine = create_engine(DATABASE_URL, echo=True)

# Create the tables
Base.metadata.create_all(bind=engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add some sample data
candidate1 = Candidate(name='John Doe')
candidate2 = Candidate(name='Jane Smith')
session.add_all([candidate1, candidate2])
session.commit()

voter1 = Voter(name='Alice Johnson', candidate=candidate1)
voter2 = Voter(name='Bob Anderson', candidate=candidate1)
voter3 = Voter(name='Charlie Brown', candidate=candidate2)
voter4 = Voter(name='Diana Taylor', candidate=candidate2)
session.add_all([voter1, voter2, voter3, voter4])
session.commit()

vote1 = Vote(voter=voter1, candidate=candidate1)
vote2 = Vote(voter=voter2, candidate=candidate1)
vote3 = Vote(voter=voter3, candidate=candidate2)
vote4 = Vote(voter=voter4, candidate=candidate2)
session.add_all([vote1, vote2, vote3, vote4])
session.commit()

# Query and display results for candidates
candidates = session.query(Candidate).all()
print("Candidates:")
for candidate in candidates:
    print(f"{candidate.name}: {len(candidate.votes_relation)} votes")

# Query and display results for voters
voters = session.query(Voter).all()
print("\nVoters:")
for voter in voters:
    print(f"{voter.name}: {len(voter.votes)} votes")

# Close the session
session.close()
