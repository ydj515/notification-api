from app.database.conn import db
from app.database.schema import Users


def test_registration(client, session):
    """
    레버 로그인
    :param client:
    :param session:
    :return:
    """
    user = dict(email="ydj515@naver.com", pw="123456", name="유동진", phone="01012345678")
    res = client.post("api/auth/register/email", json=user)
    res_body = res.json()
    print(res.json())
    
    assert res.status_code == 201
    assert "Authorization" in res_body


def test_registration_exist_email(client, session):
    """
    레버 로그인
    :param client:
    :param session:
    :return:
    """
    user = dict(email="ydj515@naver.com", pw="123456", name="유동진", phone="01012345678")
    db_user = Users.create(session=session, **user)
    session.commit()
    res = client.post("api/auth/register/email", json=user)
    res_body = res.json()

    assert res.status_code == 400
    assert 'EMAIL_EXISTS' == res_body["msg"]