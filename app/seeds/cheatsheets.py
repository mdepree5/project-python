from app.models import db, Cheatsheet


# Adds a demo user, you can add other cheatsheets here if you want
def seed_cheatsheets():
    python_itself = Cheatsheet(
        owner_id=1,
        title='Install Python itself',
        description='We will be installing Python version 3.9.4.',
        dependencies='Have pyenv pre-installed.',
        media_url='https://portswigger.net/cms/images/cc/df/f173-article-211203-python-body-text.png'
        )
    deploy_heroku = Cheatsheet(
        owner_id=2,
        title='Deploying to Heroku',
        description='We will be deploying an app with an Express backend',
        dependencies='Have Heroku CLI installed, and a heroku account',
        media_url='https://www.fullstackpython.com/img/logos/heroku.png'
        )

    db.session.add(python_itself)
    db.session.add(deploy_heroku)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE the cheatsheets table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_cheatsheets():
    db.session.execute('TRUNCATE cheatsheets RESTART IDENTITY CASCADE;')
    db.session.commit()