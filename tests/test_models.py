from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(user_name="Luiz Eduardo", email="luiz@gmail.com", password="batatinha")

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == "luiz@gmail.com"))

    assert result.user_name == "Luiz Eduardo"
