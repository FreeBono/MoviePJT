<template>
  <div class="detail-review">
    <br>
    <br>
    <div align="left" class="review-title" >
      <div style="font-size:3rem">{{ reviewInfo.movietitle }}</div>
      <div>
        <hr style="height:5px; color:#46CCFF;">
      </div>
      <div class="d-flex justify-content-between my-2">
        <div style="font-size:1.5rem">제목 : {{ reviewInfo.title }}</div>
        <div style="font-size:1.25rem" @click="goProfile(reviewInfo.username)" class="username">작성자: {{ reviewInfo.username }}</div>
      </div>
      <div></div>
      <div class="rank" style="font-size:1.25rem; my-2">평점: {{ reviewInfo.rank }}</div>
      <hr>
      <div class="review-content my-2" style="font-size:1.5rem">리뷰내용</div>
      <div >{{ reviewInfo.content }}</div>
    
      <br>
      <div class="created mt-5" style="font-size:0.9rem">처음작성시각: {{ makeDate(reviewInfo.created_at) }} {{ makeTime(reviewInfo.created_at) }}</div>
      <div class="updated my-2" style="font-size:0.9rem">최종수정시각: {{ makeDate(reviewInfo.updated_at) }} {{ makeTime(reviewInfo.updated_at) }}</div>
      
    </div>
    <div v-if="reviewInfo.username === userInfo.username" class="two-btn d-flex">
      <div class="edit-review-btn d-flex">
        <b-button class="mx-2" v-if="isEditReview" @click="updateReview" variant="outline-warning">수정</b-button>
        <b-button v-else variant="warning" disabled><b-spinner small></b-spinner>수정</b-button>
      </div>
      <div class="del-review-btn">
        <b-button v-if="isDelReview" @click="delReview" variant="outline-danger">삭제</b-button>
        <b-button v-else variant="danger" disabled><b-spinner small></b-spinner>삭제</b-button>
      </div>
    </div>
    <button v-if="reviewInfo.username === userInfo.username" @click="likemotion" class="review-like-btn btn btn-outline-dark far fa-heart fa-5x"></button>
    <div v-else>
      <button v-if="isLike" @click="dislikeReview" class="review-like-btn btn btn-danger fas fa-heart fa-5x"></button>
      <button v-else @click="likeReview" class="review-like-btn btn btn-outline-dark far fa-heart fa-5x"></button>
    </div>
    <div>
      <span class="like-count" style="font-size:1.5rem; color:#EB0000;">{{ likeCount }}</span>
    </div>
    <hr>
    <!-- 댓글 작성 -->
    <div class="d-flex justify-content-between comment-form">
      <input v-model="newcomment" @keyup.enter.exact="createComment" size="70" placeholder="댓글을 입력하세요">
      <div class="comment-add-btn" style="color:#46CCFF;">
        <b-button v-if="isAddCom" @click="createComment" variant="outline-info" style="background-color:#46CCFF; color:white">등록</b-button>
        <b-button v-else variant="outline-info" disabled style="background-color:#46CCFF; color:white"><b-spinner small></b-spinner>등록</b-button>
      </div>
    </div>
    <hr class="mb-0">
    <!-- 댓글보기 -->
    <div class="comment-list">
      <div v-for="comment in comments" :key="comment.id" class="d-flex justify-content-between align-items-center" style="border-bottom-style:solid; border-width:1px; border-color:gray">
        <div>
          <div align="left" @click="goProfile(comment.username)" style="font-size:1.25rem; font-weight:bold;">{{comment.username}}</div>
          <div align="left" :title="comment.username">{{ comment.content }}</div>
        </div>
        <div class="d-flex" >
          {{ makeDate(comment.updated_at) }} {{ makeTime(comment.updated_at) }}&nbsp;&nbsp;
          <div  v-if="comment.username === userInfo.username" class="comment-del-btn">
            <b-button v-if="isDelCom" @click="delComment(comment.id)" variant="outline-danger" size="sm">삭제</b-button>
            <b-button v-else variant="danger" disabled size="sm" ><b-spinner small></b-spinner >삭제</b-button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'DetailReview',
  data() {
    return {
      newcomment: '',
      comments: null,
      likeCount: 0,
      isLike: false,
      isEditReview: true,
      isDelReview: true,
      isAddCom: true,
      isDelCom: true
    }
  },
  beforeCreate() {
    if (!localStorage.getItem('jwt')) {
      this.$router.push({name: 'Login'})
    }
  },
  computed: {
    ...mapState(['reviewInfo', 'userInfo']),
    ...mapGetters(['setToken']),
  },
  methods: {
    ...mapActions(['saveDetailReview', 'goProfile', 'userpoint']),
    makeDate(datetime) {
      const old = ''+datetime
      return old.substring(0,10)
    },
    makeTime(datetime) {
      const old = ''+datetime
      return old.substring(11,19)
    },
    likemotion() {
      return alert('당신은 나르시스트...? 🚀')
    }
    ,
    updateReview() {
      // ReviewFrom으로 reviewInfo를 가지고 간다.
      this.isEditReview = false
      this.$router.push({name: 'EditReviewForm', params: {reviewId: this.$route.params.reviewId}})
    },
    delReview() {
      if (confirm('정말... 삭제를 원해?') == true) {
        this.isDelReview = false
        this.$axios({
          method: 'delete',
          url: `${SERVER_URL}/community/review/${this.reviewInfo.id}/`,
          headers: this.setToken
        })
        .then(() => {
          this.$router.push({name: 'Community'})
        })
        .catch(err => { console.log(err) })
      } else {
        this.isDelReview = true
        return
      }
    },
    createComment() {
      this.isAddCom = false
      this.$axios({
        method: 'post',
        url: `${SERVER_URL}/community/review/${this.reviewInfo.id}/comment/`,
        headers: this.setToken,
        data: {content: this.newcomment}
      })
      .then(() => {
        this.newcomment = null
        this.getComments()
      })
      .then(() => {
        this.userpoint('wc')
        this.isAddCom = true
      })
      .catch(err => {
        console.log(err)
      })
    },
    getComments() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/community/review/${this.reviewInfo.id}/comment/`,
        headers: this.setToken,
      })
      .then(res => {
        // console.log(res.data)
        this.comments = res.data
      })
      .catch(err => {console.log(err)})
    },
    delComment(commentId) {
      this.isDelCom = false
      this.$axios({
        method: 'delete',
        url: `${SERVER_URL}/community/comment/${commentId}`,
        headers: this.setToken,
      })
      .then(() => {
        this.isDelCom = true
        this.getComments()
      })
      .catch(err => { console.log(err) })
    },
    likeReview() {
      // console.log('좋아요 누름!')
      this.$axios({
        method: 'post',
        url: `${SERVER_URL}/community/like/`,
        headers: this.setToken,
        data: {reviewId: this.reviewInfo.id}
      })
      .then(res => {                                              // 좋아요 숫자, 버튼 변경
        const { liked, count } = res.data
        // console.log(liked, count)
        const likeCountTag = document.querySelector('.like-count')
        likeCountTag.innerText = count
        this.isLike = liked
      })
      .then(() => {                                               // 좋아요 받은사람 point
        this.userpoint(this.reviewInfo.username)
      })
      .catch(err => {
        console.log(err)
      })
    },
    dislikeReview() {
      // console.log('좋아요 누름!')
      this.$axios({
        method: 'post',
        url: `${SERVER_URL}/community/like/`,
        headers: this.setToken,
        data: {reviewId: this.reviewInfo.id}
      })
      .then(res => {                                              // 좋아요 숫자, 버튼 변경
        const { liked, count } = res.data
        // console.log(liked, count)
        const likeCountTag = document.querySelector('.like-count')
        likeCountTag.innerText = count
        this.isLike = liked
      })
      .catch(err => {
        console.log(err)
      })
    }
  },

  created() {
    document.title = 'GwakLee-Review🎬'
    // params의 reviewId 가지고 해당 review 달라고 get 요청 보내기
    const {reviewId} = this.$route.params
    this.$axios({
      method: 'get',
      url: `${SERVER_URL}/community/review/${reviewId}/`,
      headers: this.setToken
    })
    .then(res => {
      // 그 리뷰 store에 저장하기
      // console.log(res.data)
      this.saveDetailReview(res.data)
      // 초기 좋아요 버튼 모양 결정하기
      const { like } = res.data
      this.likeCount = like.length
      if (like.length && like.includes(this.userInfo.id)) {
        this.isLike = true
      }
    })
    .then(() => {
      // 저장된 리뷰에 맞는 comments들 전부 불러오기
      this.getComments()
    })
    .catch(err => {
      console.log(err)
    })
  }
}
</script>

<style scoped>
.review-like-btn {
  border: 2;
  outline: 0;
  height:50px;
  width: 50px;
  padding:0;
}

div {
  word-break:break-all;
}
</style>