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

    click.echo("Sample data seeded successfully.")

@cli.command()
def display_results():
    """Display voting results."""
    candidates_query = session.query(Candidate).all()
    click.echo("Candidates and Votes:")
    for candidate in candidates_query:
        click.echo(f"{candidate.name}: {len(candidate.votes)} votes")

    voters_query = session.query(Voter).all()
    click.echo("\nVoters and Votes:")
    for voter in voters_query:
        click.echo(f"{voter.name}: {len(voter.votes)} votes")

if __name__ == "__main__":
    cli()