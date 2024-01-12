from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from model import Candidate, Voter, Vote


fake = Faker()


DATABASE_URL = "sqlite:///vote_database.db"
engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# Add candidates (using Faker)
candidates = []
for _ in range(2):
    candidate = Candidate(name=fake.name())
    candidates.append(candidate)
    session.add(candidate)
session.commit()

# Add voters (using Faker)
voters = []
for _ in range(4):
    voter = Voter(name=fake.name(), candidate=candidates[fake.random_int(min=0, max=1)])
    voters.append(voter)
    session.add(voter)
session.commit()

# Add votes (using Faker)
for _ in range(4):
    vote = Vote(voter=voters[fake.random_int(min=0, max=3)], candidate=candidates[fake.random_int(min=0, max=1)])
    session.add(vote)
session.commit()

print("Sample data seeded successfully.")

# Close the session
session.close()


