# READ ME

## 개발 환경

- Python
  - python
  - django
  - sqlite3
- javascript
  - Vue.js
- 사용 라이브러리
  - bootstrap
  - bootstrap-vue
  - font-awesome

## 1. 프로젝트 개요

- #### 목표 컨셉 - 커뮤니티적 요소를 포함한 영화 추천 사이트  

- #### 주요 목표 기능

  - **컨텐츠 기반 필터링**에 기반한 영화 추천

  - **포인트 제도**를 도입하여 커뮤니티적 요소 강화

  - **쉽고, 간단**하게 커뮤니티 게시글을 이용

  - 정확한 검색어를 입력하지 않아도 사용자요구 정보와 유사한 정보 제공

    

- #### 명세서 요구 주요기능

  - 로그인된 유저의 영화에 대한 평점을 등록 / 수정 / 삭제
  - 필요 정보를 클라이언트 화면에서 확인
  - 영화 데이터베이스를 기반으로한 영화 추천



## 2. 팀 역할 및 업무 분장

#### 2-1) 팀 정보

팀장 : 부울경 1반 곽동현

팀원 : 부울경 1반 이혜진



#### 2-2) 업무 분장

- 곽동현 (BACK-END)
  - Django API Server, 영화 추천 Algorithm 개발
  - 데이터베이스 구축
- 이혜진 (FRONT-END)
  - Vue를 이용한 서버(Django, API)와 클라이언트간 통신, 데이터 관리
  - 핵심 UI 개발



## 3. 프로젝트 결과



#### 프로젝트 ERD

![ERD](READ ME.assets/ERD.png)

### 구현 

- #### 주요 목표 기능

  - 컨텐츠 기반 필터링에 기반한 영화 추천 ✔

  - 포인트 제도를 도입하여 커뮤니티적 요소 강화 ✔

  - **쉽고, 간단**하게 커뮤니티 게시글을 이용 ✔

  - 정확한 검색어를 입력하지 않아도 사용자요구 정보와 유사한 정보 제공 ✔

    

- #### 명세서 요구 주요기능

  - 로그인된 유저의 영화에 대한 평점을 등록 / 수정 / 삭제 ✔
  - 필요 정보를 클라이언트 화면에서 확인 ✔
  - 영화 데이터베이스를 기반으로한 영화 추천 ✔



### 미구현

- ####  보유 포인트를 소모하여 중복 평점 부여가 가능한 시스템

  - 기획 후 단계에서 브레인스토밍한 아이디어로 구현하기에 시간 부족

- #### 팔로우한 유저의 목록으로 바로이동 가능한 기능

- #### 서치바 장르 검색 기능



## 4. 핵심 기능

- 영화에 기본 정보 제공(6760편)

- 영화 리뷰의 등록, 수정, 삭제 가능
  - 코멘트 등록가능
  - 좋아요 기능 추가
  - 평점 부여

- 영화 추천 기능
  - 장르 유사도 검사를 통한 영화 추천
  - **컨텐츠 기반 필터링**을 통한 영화 추천



## 5. 느낀 점

- 곽동현

  처음 시작한 순간부터 프로젝트를 끝낼 때 까지 벽에 계속 부딪히면서 작업을 했습니다. 무엇보다 크게 느낀것은 초기 기획단계에서 모델과 관계를 제대로 설정해야 이후 프로젝트를 진행할 때 수월하다는 것입니다. 하지만 처음으로 해보는 프로젝트 였던만큼 직접 부딪혀가면서 프로젝트가 어떻게 진행되는지, 어떻게 해야 효율적인지를 깨달았다고 생각하기 때문에 힘듦보다는 배움이 더 많았다고 생각합니다.

- 이혜진

  웹사이트를 만드는 프로젝트는 처음이였습니다. 처음에는 할수있겠다고 생각했으나 부딪혀보니 만만치 않았습니다. 프론트를 주로 맡았는데, python에 비해 생소한 언어로 진행하다보니 함수를 사용하는데 문법을 몰라서 막히는 경우도 종종 있었습니다. 막상 다 끝나고 보니 구현해내지 못해서 아쉬운 점과 더 꾸미지 못해서 아쉬운 점만 생각납니다. 배운점으로는 기초공사가 중요하다는 것입니다. 초반에 뭐가 뭔지 잘 모르는 상태에서 계획을 세우기보다 일단 부딪혀보자는 생각으로 시작했더니, 초반에는 어떻게 잘 풀리는듯 했지만 뒤로 갈수록 초반의 아쉬운점이 보였습니다. 다음에 초반에 계획을 제대로 세우고 시작한다면 더 좋은 결과를 낼 수 있을거라 생각합니다.