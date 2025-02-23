# Training Log App
러닝 기반 운동/훈련 일지 작성용 mac앱
download : https://github.com/JIN-ARTLW/Training-Log-App/releases/tag/1.0


사용자가 개인의 트레이닝(운동, 학습 등) 기록을 손쉽게 관리할 수 있도록 돕는 macOS 앱

## 주요 기능

- **트레이닝 기록 관리**
  ![image](https://github.com/user-attachments/assets/0a64d12e-8a65-40b1-8b6b-9f7b4affe470)
  - 일별 훈련일지 작성 가능
  - 러닝 트레이닝 : 다양한 트레이닝 종류
    [조깅, 지속주, 윈드 스프린트, LSD, 가속주, 언덕훈련, 인터벌, TT, 크로스 컨트리]  
    인터벌, 언덕훈련은 m*횟수 포맷 지원
  - 보강 트레이닝 (텍스트 형식)
  - 아침 심박수 (bpm)
  - 공복 몸무게 (kg)
  - 작일 취침 시각, 기상시각 입력 시 수면 시간 자동 계산
  - 배변 여부 (o,x)
  - 식사 기록
    [아침, 점심, 저녁, 간식]
  - 코멘트 (훈련 후기 및 몸상태 등 텍스트 형식 기록 가능)
 
- **주간 뷰어**
  ![image](https://github.com/user-attachments/assets/1e39bfb7-193c-439c-a78a-0a4cb3f61454)
  - 훈련 일지 작성 시 1주일 단위 보기 지원 (월요일 시작)

- **월간 뷰어**
  ![image](https://github.com/user-attachments/assets/ecd15901-db0d-496a-83fa-3f88acd72e82)
  - 훈련 일지 작성 시 1개월 단위 보기 지원 (달린 거리, 몸무게와 몸무게 변화, 수면시간)

- **데이터 내보내기**
  ![image](https://github.com/user-attachments/assets/45d1c202-b59c-4744-98bb-05ab6c5225d8)
  - 주간, 월간 일지를 이미지(png) 파일로 기록 내보내기 지원  

- **데이터 백업 및 불러오기**  
  - 정기적인 자동 백업 기능  
  - 이전 기록 복구를 위한 기능 제공

- **인터페이스**  
  - PyQt5 기반 UI  
  - 다크/라이트 모드 지원 및 반응형 디자인

- **효율적인 데이터 처리**  
  - SQLite 데이터베이스 기반 저장 기능

## 설치 및 실행
![image](https://github.com/user-attachments/assets/bcf2eb39-72cf-4d7b-91ef-f48ee51c37bb)
1. **DMG 파일 다운로드 및 설치**  
   - DMG 파일을 다운로드합니다.  
   - DMG를 열고, **Training Log** 아이콘을 `/Applications` 폴더로 드래그하여 복사합니다.

2. **앱 실행**  
   - `/Applications` 폴더에서 **Training Log**를 실행하면 앱이 시작됩니다.


## 기여

- 프로젝트 개선이나 버그 수정에 기여하고 싶으신 분은 이 저장소를 포크한 후 Pull Request를 보내주세요.
- 문제나 제안 사항은 이슈 트래커에 등록해 주시면 감사하겠습니다.
