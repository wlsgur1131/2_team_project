# 📘 ERD 설계 문서 – 전력 데이터를 활용한 제조업 경기 예측 서비스
본 문서는 제조업 생산지수 예측 웹서비스를 위한 데이터베이스 ERD 설계 문서입니다. 확장성, 정규화, 성능 최적화, 협업 효율성을 고려하여 MySQL 기반으로 작성되었습니다.

---

## 🔧 DB 설계 개요

* **DBMS**: MySQL
* **주요 목적**: 사용자 맞춤형 예측 서비스 제공을 위한 시계열 데이터 저장, 사용자 설정, 예측 결과, 알림 기능 등 전체 서비스 데이터 흐름 구성
* **설계 방식**: 정규화 기반 ERD 설계 + 인덱싱 및 제약조건 명시

---

## 📂 테이블 구성 요약

| 테이블명                 | 설명             |
| -------------------- | -------------- |
| `users`              | 사용자 정보 저장      |
| `user_preferences`   | 관심 지역/업종 설정    |
| `production_index`   | 제조업 생산지수 (실제값) |
| `power_usage`        | 산업용 전력 사용량     |
| `export_data`        | 지역별 수출금액 정보    |
| `weather_data`       | 기온/강수량 등 기후 정보 |
| `prediction_results` | 모델 예측 결과 저장    |
| `user_alerts`        | 사용자 알림 메시지 저장  |

---

## 📌 주요 설계 원칙

* **정규화 (3NF)**: 중복 제거 및 데이터 무결성 확보
* **외래키 사용**: 사용자 참조, 지역/업종 기준 데이터 연결
* **인덱싱**: 시계열 탐색 최적화를 위해 (date, region\_code 등) 복합 인덱스 적용
* **확장성 고려**: 업종/지역별 세분화, 향후 변수 추가 가능성 고려한 설계
* **보안 고려**: 비밀번호 해시 저장 (bcrypt 등 사용 전제)

---

## 🔐 사용자 관련 테이블

### `users`

| 필드명            | 타입           | 설명                 |
| -------------- | ------------ | ------------------ |
| id             | INT          | PK, auto increment |
| email          | VARCHAR(100) | unique, not null   |
| password\_hash | VARCHAR(255) | not null           |
| name           | VARCHAR(50)  | 사용자 이름             |
| login\_type    | VARCHAR(10)  | email / google 구분  |
| created\_at    | TIMESTAMP    | 가입 일시              |

### `user_preferences`

| 필드명            | 타입          | 설명            |
| -------------- | ----------- | ------------- |
| id             | INT         | PK            |
| user\_id       | INT         | FK → users.id |
| region\_code   | VARCHAR(20) | 관심 지역 코드      |
| industry\_code | VARCHAR(20) | 관심 업종 코드      |

---

## 📈 시계열 원본 데이터

### `production_index`

* 제조업 생산지수 원본 (KOSIS)

| 필드명               | 설명                |
| ----------------- | ----------------- |
| date              | 기준 월 (YYYY-MM-DD) |
| region\_code      | 지역 코드             |
| industry\_code    | 업종 코드             |
| production\_index | 생산지수 값            |
| updated\_at       | 갱신 일시             |

**인덱스**: (date, region\_code, industry\_code) UNIQUE

### `power_usage`

* 산업용 전력 사용량 (한국전력)

| 필드명          | 설명                  |
| ------------ | ------------------- |
| date         | 기준 월                |
| region\_code | 지역 코드               |
| power\_usage | 전력 사용량 (kWh 또는 MWh) |
| updated\_at  | 갱신 일시               |

**인덱스**: (date, region\_code) UNIQUE

### `export_data`

* 수출금액 (억 원 기준)

| 필드명            | 설명    |
| -------------- | ----- |
| date           | 기준 월  |
| region\_code   | 지역 코드 |
| export\_amount | 수출 금액 |
| updated\_at    | 갱신 일시 |

**인덱스**: (date, region\_code) UNIQUE

### `weather_data`

* 월별 기온 및 강수량 (기상청)

| 필드명           | 설명       |
| ------------- | -------- |
| date          | 기준 월     |
| region\_code  | 지역 코드    |
| avg\_temp     | 평균기온     |
| max\_temp     | 최고기온     |
| precipitation | 강수량 (mm) |
| updated\_at   | 갱신 일시    |

**인덱스**: (date, region\_code) UNIQUE

---

## 🔮 예측 관련 테이블

### `prediction_results`

* 예측 모델 결과 저장 테이블

| 필드명              | 설명            |
| ---------------- | ------------- |
| date             | 예측 기준 월       |
| region\_code     | 지역 코드         |
| industry\_code   | 업종 코드         |
| predicted\_index | 예측된 생산지수      |
| confidence       | 예측 확신도 (0\~1) |
| model\_version   | 사용한 모델 버전     |
| created\_at      | 생성 일시         |

**인덱스**: (date, region\_code, industry\_code) UNIQUE

### `user_alerts`

* 사용자 알림 메시지

| 필드명          | 설명          |
| ------------ | ----------- |
| user\_id     | 사용자 ID (FK) |
| message      | 알림 메시지      |
| read\_status | 읽음 여부       |
| created\_at  | 생성 일시       |

---

## 🔒 데이터 무결성 및 제약 조건 요약

| 항목                       | 내용                                                                                                       |
| ------------------------ | -------------------------------------------------------------------------------------------------------- |
| **외래키 제약**               | `user_preferences.user_id`, `user_alerts.user_id`는 `users.id`를 참조 (ON DELETE CASCADE 등은 설계 의도에 따라 선택 가능) |
| **고유성 보장 (UNIQUE)**      | 시계열 테이블의 `(date, region_code[, industry_code])` 조합은 모두 UNIQUE 제약 적용하여 중복 방지                              |
| **보조 키 (Alternate Key)** | 각 시계열 테이블의 날짜 + 지역(및 업종) 컬럼은 논리적 보조 키로 사용                                                                |
| **암호화**                  | 사용자 비밀번호는 해시(bcrypt 등)로 저장하여 보안 유지                                                                       |
| **읽음 상태 기본값**            | `user_alerts.read_status`는 기본값 `false`로 설정                                                               |
| **날짜 필드 통일성**            | 날짜 관련 필드는 모두 `DATE` 타입 사용하여 시계열 일관성 유지                                                                   |
| **정규화 준수**               | 테이블 간 관계 및 중복 최소화를 위한 정규화(3NF) 적용                                                                        |

---

✅ ERD 시각화 도구: [dbdiagram.io](https://dbdiagram.io)
