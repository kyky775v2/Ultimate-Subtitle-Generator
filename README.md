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
현재 사용 가능한 모델은 다음과 같습니다: large-v3<br>
영단어로 해석하면 갈수록 뜻이 커지죠. 그만큼 더 복잡하다는 것입니다.<br>
이 프로젝트에서는 앞서 나열된 모델 모두 사용 가능합니다. 단, 커질수록 컴퓨터 사양이 좋아야죠.
#### 하드웨어 가속 (GPU, CUDA)
이것은 프로그램 사용자의 컴퓨터에서 GPU (그래픽카드)를 사용해 자막을 더 빨리 생성해주는 기능입니다.<br>
이것은 제 경험담입니다. 하드웨어 가속에 사용된 GPU는 NVIDIA GeForce RTX3060 Laptop GPU 입니다.<br>
27분 토크쇼 영상을 하드웨어 가속 없이 자막을 뽑았더니 1시간정도 걸렸습니다.<br>
그러나 하드웨어 가속을 켜고 똑같은 영상에서 자막을 추출했더니, 약 10분 정도 걸렸습니다.<br>
확연한 차이죠. 이 기능이 프로그램에서 가능하도록 구현하였습니다. 컴퓨터가 좋으시다면 꼭 활성화해주세요!<br>

### ❓ 어떻게 사용하나요?
#### 다운받기 & 실행하기
1. 우측에 있는 Release 탭에서 가장 최신 버전을 다운로드 해주세요.
2. 다운받은 usg.zip를 바탕화면에 풀어주세요.
3. 바탕화면에 압축을 푼 폴더에서 usg.exe 파일을 실행해주세요.
4. 윈도우 디펜더에서 출처를 알 수 없는 프로그램이라고 가로막을거에요. 세부 정보 > 실행을 눌러주세요.
5. 검은 창이 뜬 뒤 흰 창이 뜨고 응답없음이 표시될거에요, 정상입니다. 흰 창에 UI가 뜰때까지 기다려주세요.
#### 설정하기
1. 최초 실행 시 영어로 표시될거에요. Start 버튼 우측에 톱니바퀴 아이콘을 눌러주세요.
2. 상단에서 순서대로 언어, 하드웨어 (GPU) 가속, AI모델 선택입니다.<br>
하드웨어 가속 섹션이 안보이신다면 안타깝게도 기기가 하드웨어 가속을 지원하지 않는 경우에요... :(
#### 사용하기
1. 영상/오디오 선택은 음성이 담긴 파일을 우측의 폴더 아이콘을 눌러 선택해주세요.
2. 자막 출력 폴더는 자막을 내보낼 폴더를 우측의 폴더 아이콘을 눌러 선택해주세요.
3. 시작을 눌러 작업을 시작합니다.<br>
<b>시작 버튼을 누른 후 완료될때까지 창이 응답없음으로 변할꺼에요! 정상이에요. 조금만 기다려주세요.</b>
4. 처리가 완료되면 일괄 작업이 성공적으로 끝났다고 하단에 표시될거에요. 끝입니다! 이제 커피 한 잔의 여유를 즐기러 가보자구요!<br>
([2]에서 선택한 폴더에 result.srt 파일이 생겼을거에요. 처리된 자막 파일입니다.)
### ❗ 버그 신고 및 문의
- 상단에 Issues 탭을 이용해 주세요.
- 기타 문의는 kyky775@gmail.com으로 부탁드려요!
