from flask import Flask  # type: ignore  # Flask 프레임워크에서 Flask 클래스 임포트
from dotenv import load_dotenv           # .env 파일에서 환경변수를 로드하기 위한 모듈 임포트
import os                                # 운영체제 환경변수 접근을 위한 os 모듈

def create_app():
    # .env 파일에 정의된 환경 변수들을 시스템 환경변수로 로드
    load_dotenv()

    # Flask 앱 인스턴스 생성
    app = Flask(__name__)

    # 환경변수로부터 DB 관련 설정값들을 Flask 앱 설정에 저장
    app.config['DB_HOST'] = os.getenv('DB_HOST')          # DB 호스트 주소
    app.config['DB_USER'] = os.getenv('DB_USER')          # DB 사용자명
    app.config['DB_PASSWORD'] = os.getenv('DB_PASSWORD')  # DB 비밀번호
    app.config['DB_NAME'] = os.getenv('DB_NAME')          # DB 이름

    # 라우트 정의된 Blueprint를 등록하여 엔드포인트 활성화
    from .routes.main import bp as main_bp
    app.register_blueprint(main_bp)

    # 앱 인스턴스 반환
    return app