# 2021-Hackathon-Simulator

### 대회 개요
![poster](https://user-images.githubusercontent.com/75441733/140630071-08070e02-4f25-4715-bc98-1a9ce6836db3.jpg)
* 대회명: 제4회 자율주행 아이디어 해커톤
* 일시: 2021. 11. 12. - 2021. 11. 13.
* 장소: 성균관대학교 산학협력센터 캡스톤디자인실 85129호 (거리두기 단계에 따라 변동 가능)
* 주최: 성균관대학교 LINC+ 사업단
* 주관: 성균관대학교 창업동아리, HEVEN


### 팀 구성
- 1팀 : `손희관(팀장)`, `곽동규`, `김태웅`, `송영보`
- 2팀 : `이범수(팀장, 16)`, `김석중`, `양승진`, `허재호`
- 3팀 : `정종현(팀장)`, `박건희`, `박성준`, `홍영진`
- 4팀 : `차민지(팀장)`, `목예본`, `박인지`, `이범수(18)`
- 5팀 : `이주현(팀장)`, `김민주`, `손민규`, `이창준`
- 6팀 : `송은지(팀장)`, `강나윤`, `김승연`, `윤찬혁`
- 7팀 : `박충현(팀장)`, `김태윤`, `박지용`, `이준아`
- 8팀 : `안호진(팀장)`, `배동근`, `전승태`, `함철훈`


### 규칙
- 이번 대회는 트로피 레이스입니다.
- 대회 진행 방식은 다음과 같습니다.


    1 - 1. 토너먼트제로 진행됩니다.   
    1 - 2. 개회식 때 뽑기를 통해 상대 팀이 정해집니다.   
    1 - 3. 저녁 8시부터 익일 아침 8시까지 코드를 작성할 수 있습니다.   
    1 - 4. 지각 제출 시에는 20분 간격으로 1점씩 패널티가 부여되며, 9시 이후에는 미제출로 실격 처리됩니다.   
    1 - 5. 테스트용 컴퓨터는 개회식 장소에 비치할 예정이니, 테스트를 원하는 팀은 해당 장소에 오셔서 사용하시면 됩니다.   


    2 - 1. 각 경기는 먼저 10점을 획득하는 팀이 승리합니다.   
    2 - 2. 만약 10점 득점자가 없을 시, 점수가 높은 팀이 승리합니다.   
    2 - 3. 만약 3분 경과 시 두 팀이 동점일 경우, 먼저 해당 점수를 획득한 팀이 승리합니다.   
    
    
    3 - 1. 여러분이 작성하셔야 할 코드는 Brain.py 입니다.   
    3 - 2. 다른 코드는 건드리실 필요 없이 Brain.py 작성 후 익일 아침 8시 이전까지 joo6058@gmail.com 으로 보내주시면 됩니다.   
    3 - 3. 추가적으로 사용한 모듈이 있는 경우, requirements.txt 로 제출해주세요.   
    3 - 4. 기타 부정행위로 간주되는 코드는 조치가 취해질 수 있습니다.   
    3 - 5. 각 경기가 끝나면 15분간의 코드 수정 시간이 주어집니다.   
    3 - 6. 제자리 조향은 불가능합니다.   
    3 - 7. 현재 Repository에 있는 트로피의 위치와 실제 대회 시의 트로피 위치는 상이할 수 있습니다.   
    

### 안내 사항


1. Requirements   
    - python == 3.8
    - numpy == 1.21.2
    - opencv-python >= 4
    - pygame == 2.0.2


2. Data (LiDAR / GPS / IMU / 속도 / V2X)   
    - `LiDAR` : self.database.lidar.data
    - `GPS` : self.database.car.position
    - `IMU` : self.database.car.direction
    - `속도` : self.database.car.speed
    - `V2X` : self.database.v2x_data (신호등, 트로피 정보)


3. Control   
    - `속도 증가` : self.database.control.up()&nbsp;&nbsp;&nbsp;&nbsp;OR&nbsp;&nbsp;&nbsp;&nbsp;self.up(num)
    - `속도 감소` : self.database.control.down()&nbsp;&nbsp;&nbsp;&nbsp;OR&nbsp;&nbsp;&nbsp;&nbsp;self.down(num)
    - `좌로 조향` : self.database.control.left()&nbsp;&nbsp;&nbsp;&nbsp;OR&nbsp;&nbsp;&nbsp;&nbsp;self.left(num)
    - `우로 조향` : self.database.control.right()&nbsp;&nbsp;&nbsp;&nbsp;OR&nbsp;&nbsp;&nbsp;&nbsp;self.right(num)


### Related Repository
Reference : https://github.com/tdostilio/Race_Game