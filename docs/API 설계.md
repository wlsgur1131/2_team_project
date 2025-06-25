# 📡 API 설계 문서 – 전력 데이터를 활용한 제조업 경기 예측 서비스

## 🧾 개요

이 문서는 전력 기반 제조업 경기 예측 서비스를 위한 RESTful API 명세를 정의합니다. 프론트엔드와 백엔드 간의 통신을 위한 기본 구조를 제공하며, 각 API의 요청/응답 형식을 포함합니다.

---

## 🔐 인증 관련 API

### ▶️ 회원가입

* `POST /api/auth/register`
* 설명: 이메일 기반 회원가입 및 인증 메일 발송
* 요청 Body:

```json
{
  "email": "user@example.com",
  "password": "123456",
  "name": "홍길동"
}
```

* 응답:

```json
{
  "message": "회원가입 완료. 이메일을 확인해주세요.",
  "user_id": 3
}
```

### ▶️ 이메일 인증 확인

* `GET /api/auth/verify?token=...`
* 설명: 메일 내 인증 링크 클릭 시 호출되는 토큰 기반 인증
* 응답:

```json
{
  "message": "이메일 인증이 완료되었습니다."
}
```

### ▶️ 로그인

* `POST /api/auth/login`
* 설명: 로그인 및 토큰 발급
* 요청 Body:

```json
{
  "email": "user@example.com",
  "password": "123456"
}
```

* 응답:

```json
{
  "access_token": "...jwt...",
  "user": {
    "id": 3,
    "name": "홍길동"
  }
}
```

---

## 👤 사용자 설정 API

### ▶️ 관심 설정 저장

* `POST /api/user/preferences`
* 설명: 사용자 관심 지역/업종 저장
* 요청 Body:

```json
{
  "region_code": ["11", "26"],
  "industry_code": ["C10", "C20"]
}
```

### ▶️ 사용자 정보 조회

* `GET /api/user/me`
* 설명: 사용자 정보 및 설정 조회

---

## 📊 데이터 조회 API

### ▶️ 생산지수 추이 조회

* `GET /api/data/production?region=11&industry=C10`
* 설명: 생산지수 시계열 데이터 반환

### ▶️ 전력 사용량 추이

* `GET /api/data/power?region=11`
* 설명: 지역별 전력 사용량 시계열 데이터 반환

### ▶️ 날씨/수출 보조 데이터 조회

* `GET /api/data/weather?region=11`
* `GET /api/data/export?region=11`

---

## 🔮 예측 관련 API

### ▶️ 예측 결과 조회

* `GET /api/predict?region=11&industry=C10`
* 설명: 선택 지역·업종에 대한 다음 달 생산지수 예측
* 응답:

```json
{
  "date": "2025-07-01",
  "predicted_index": 104.3,
  "confidence": 0.87,
  "insight": "전력 사용량 증가에 따라 상승세 유지 예상"
}
```

---

## 🔔 알림 관련 API

### ▶️ 알림 목록 조회

* `GET /api/alerts`

### ▶️ 알림 읽음 처리

* `POST /api/alerts/{alert_id}/read`

---

## ⚙️ 관리자 기능 (선택)

### ▶️ 예측값 수동 등록 (관리자 전용)

* `POST /api/admin/predict`
* 요청 Body:

```json
{
  "date": "2025-07-01",
  "region_code": "11",
  "industry_code": "C10",
  "predicted_index": 104.3,
  "confidence": 0.87,
  "model_version": "v1.0"
}
```

---

## 📎 공통 사항

* 인증: `Authorization: Bearer <JWT>` 헤더 필요 (인증 API 제외)
* 응답은 모두 JSON 형식
* 에러 응답 구조:

```json
{
  "error": "Invalid request",
  "message": "지역코드가 유효하지 않습니다."
}
```
