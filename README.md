# Ultimate Subtitle Generator

### 📘✏프로젝트 시작 동기
저는 영상편집을 주로 하며 코딩도 취미로 하던 평범한 사람입니다.<br>
자막 시작길이 정하고, 종료길이 정하고, 텍스트 입력하고... 매일 똑같은 일상이 고통스러웠죠.<br>
그러던 어느 날, Whisper AI라는 Speech-To-Text 서비스를 발견하였고,<br>
샘플을 돌려서 나온 자막은 완벽하지 않지만 충분히 읽을 수 있는 퀄리티의 자막이었습니다.<br>
저는 이 기술이 빨리 상용화되길 기다리며, 더이상 자막으로 고통받지 않았으면 좋겠습니다.<br>
그런 바램에서 누구나 쉽게 다룰 수 있는 자막 자동 생성 프로그램을 만들게 되었습니다.<br>

### 📜프로젝트 설명
영상을 선택한 뒤, 자막을 내보낼 폴더를 지정하고 실행하면 영상에서 음성을 추출해 자막을 생성해줍니다.
#### 모델
AI 모델이란, 학습된 AI를 모델이라고 합니다. 학습한 데이터, 학습된 횟수 등 변수에 따라 달라집니다.<br>
Whisper-AI도 마찬가지입니다. 학습한 데이터와 학습 횟수가 높을수록 모델 이름도, 용량도 커집니다.<br>
현재 사용 가능한 모델은 다음과 같습니다: tiny, base, small, medium, large, large-v2, large-v3<br>
영단어로 해석하면 갈수록 뜻이 커지죠. 그만큼 더 복잡하다는 것입니다.<br>
이 프로젝트에서는 앞서 나열된 모델 모두 사용 가능합니다. 단, 커질수록 컴퓨터 사양이 좋아야죠.
#### 하드웨어 가속 (GPU, CUDA)
이것은 프로그램 사용자의 컴퓨터에서 GPU (그래픽카드)를 사용해 자막을 더 빨리 생성해주는 기능입니다.<br>
이것은 제 경험담입니다. 하드웨어 가속에 사용된 GPU는 NVIDIA GeForce RTX3060 Laptop GPU 입니다.<br>
27분 토크쇼 영상을 하드웨어 가속 없이 자막을 뽑았더니 1시간정도 걸렸습니다.<br>
그러나 하드웨어 가속을 켜고 똑같은 영상에서 자막을 추출했더니, 약 10분 정도 걸렸습니다.<br>
확연한 차이죠. 이 기능이 프로그램에서 가능하도록 구현하였습니다. 컴퓨터가 좋으시다면 꼭 활성화해주세요!<br>

### ❓ 어떻게 사용하나요?
#### 다운받기 & 설정하기
1. 우측에 있는 Release 탭에서 가장 최신 버전을 클릭해주세요.
2. 해당 버전의 포스트 하단에 USG.zip을 다운로드 해주세요.
3. 다운받은 USG.zip를 바탕화면에 풀어주세요.
4. USG Setup.exe 파일을 실행해주세요. 윈도우 디펜더에서 출처를 알 수 없는 프로그램이라고 가로막을거에요.
5. 세부 정보 > 실행을 눌러주세요. 그리고 환영한다는 창이 뜰때까지 너그럽게 기다려주세요.<br>
<b>응답없음이 뜰 수 있어요!</b>
6. 창이 뜨면 설정을 진행해주세요. 이 설정은 최초 실행시 한번만 하시면 됩니다.<br>
   설정 완료 후 바꾸고 싶으시다면 프로그램 > 설정에서 바꾸실 수 있어요.
8. 설정을 완료하면 실행하기 버튼이 표시되요. 자, 이제 프로그램을 시작해 볼까요?
#### 실행하기 & 사용하기
1. 바탕화면에 압축을 푼 폴더에서 Ultimate Subtitle Generator.exe 파일을 실행해주세요.
2. 똑같이 윈도우 디펜더에서 출처를 알 수 없는 프로그램이라고 가로막을거에요. 세부 정보 > 실행을 눌러주세요.
3. 창이 뜬 뒤 응답없음이 뜰거에요, 정상입니다. 창에 UI가 뜰때까지 기다려주세요.
4. UI가 뜨면, 설명대로 진행해주시면 됩니다. 가끔씩 응답없음이 떠요, 프로그램이 열심히 작업중이라 그런거니 양해 부탁드려요.
- 추출하기 버튼 우측에 정사각형 버튼은 설정 버튼입니다. 아이콘이 깨졌어요 ㅠ.ㅠ

### ❗ 버그 신고 및 문의
- 상단에 Issues 탭을 이용해 주세요.
- 기타 문의는 kyky775@gmail.com으로 부탁드려요!
