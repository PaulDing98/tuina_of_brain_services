from sqlalchemy.orm import Session
from app.core.exceptions import ExpiredCredentialsException
from app.models import User
from app.core.security import verify_token
from app.core.exceptions import UserDidNotExistsExcepytion
from fastapi import Header, Depends
from app.db.session import get_db
def token_to_user_id(authorization: str = Header(...))-> str:
    # 查到非Bearer Token报错
    if not authorization.startswith("Bearer "):
        raise ExpiredCredentialsException()
    return verify_token(token=authorization.split(" ")[1], token_type="access") 



def require_auth(credentials: str = Depends(token_to_user_id), db: Session = Depends(get_db)) -> User:
    # 根据 user_id 查找用户
    db_user = db.query(User).filter(User.id == credentials).first()
    # 如果表里没有这个用户，抛出异常
    if not db_user:
        raise UserDidNotExistsExcepytion()
    return db_user