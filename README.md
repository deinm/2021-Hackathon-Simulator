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
- 2팀 : `이범수(팀장)`, `김석중`, `양승진`, `허재호`
- 3팀 : `정종현(팀장)`, `박건희`, `박성준`, `홍영진`
- 4팀 : `차민지(팀장)`, `목예본`, `박인지`, `이범수(18)`
- 5팀 : `이주현(팀장)`, `김민주`, `손민규`, `이창준`
- 6팀 : `송은지(팀장)`, `강나윤`, `김승연`, `윤찬혁`
- 7팀 : `박충현(팀장)`, `김태윤`, `박지용`, `이준아`
- 8팀 : `안호진(팀장)`, `배동근`, `전승태`, `함철훈`

### 규칙


### 안내 사항
1. Data (LiDAR / GPS / IMU / 속도 / V2X)
    `LiDAR` : data = self.database.lidar.data
    `GPS` : data = self.database.car.position
    `IMU` : data = self.database.car.direction
    `속도` : self.database.car.speed
    `V2X` : self.database.v2x_data

2. Control
    `상` : self.database.control.up()           OR          self.up(num)
    `하` : self.database.control.down()         OR          self.down(num)
    `좌` : self.database.control.left()         OR          self.left(num)
    `우` : self.database.control.right()        OR          self.right(num)

### Prerequisite
```bash
pip install -r requirements.txt
```

### related repository
Reference : https://github.com/tdostilio/Race_Game