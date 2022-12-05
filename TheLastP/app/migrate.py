from app.models import db


def create_db():
    db.drop_all()
    db.create_all()


def init_db():
    create_db()
    admin = Users(
        name="Billie"

    )

    db.session.add(admin)
    db.session.commit()