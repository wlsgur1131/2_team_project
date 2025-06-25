# main.py - Flask 앱의 기본 라우트와 Blueprint를 정의
from flask import Blueprint # type: ignore

# 기본 라우트를 처리할 'main'이라는 Blueprint 생성
bp = Blueprint('main', __name__)

# 루트 URL에 대한 라우트를 정의하며, 간단한 메시지를 반환
@bp.route('/')
def index():
    return 'Hello from Flask!'