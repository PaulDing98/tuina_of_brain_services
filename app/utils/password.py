from passlib.context import CryptContext
from typing import Optional

# 创建密码上下文（配置bcrypt算法）
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
    bcrypt__rounds=12  # 哈希轮数，越高越安全但越慢，12是合理值
)

class PasswordHandler:
    """密码处理工具类"""
    
    @staticmethod
    def hash(password: str) -> str:
        """
        对密码进行哈希处理
        返回: bcrypt哈希字符串，格式如 $2b$12$... 
        """
        return pwd_context.hash(password)
    
    @staticmethod
    def verify(plain_password: str, hashed_password: str) -> bool:
        """
        验证密码是否匹配
        """
        return pwd_context.verify(plain_password, hashed_password)
    
    @staticmethod
    def is_strong_password(password: str) -> bool:
        """
        检查密码强度（业务规则）
        """
        if len(password) < 8:
            return False
        if not any(c.isupper() for c in password):
            return False
        if not any(c.islower() for c in password):
            return False
        if not any(c.isdigit() for c in password):
            return False
        if not any(c in "!@#$%^&*" for c in password):
            return False
        return True