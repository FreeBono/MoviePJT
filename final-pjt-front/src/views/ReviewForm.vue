<template>
  <!-- <div class="review-background" :style="{ backgroundImage: 'url(' + this.detailMovieInfo.backdrop_path + ')'}"> -->
  <div class="review-background">
    <h2 class="my-3">{{ detailMovieInfo.title }}'s Review</h2>
    <div class="mb-3">
      <label for="review-title" class="form-label"><h4>제목</h4></label><br>
      <b-form-input v-model="reviewTitle" placeholder="제목을 입력하세요" id="review-title" size="lg"></b-form-input>
    </div>
    <div class="mb-3">
      <label for="review-content" class="form-label"><h4>내용</h4></label>
      <b-form-textarea v-model="reviewContent" id="review-content" class="form-control" placeholder="내용을 입력하세요" rows="10"></b-form-textarea>
    </div>
    <div class="mb-3">
      <label for="review-score" class="form-label"><h4>평점</h4></label>
      <b-form-rating v-model="reviewScore" variant="warning" class="mb-2" id="review-score" size="lg"></b-form-rating>
    </div>
    <b-button v-if="btnBoolean" @click="addReview" variant="outline-success" title="빈칸은 등록되지 않습니다" class="mb-3">등록</b-button>
    <b-button v-else variant="success" disabled class="mb-3"><b-spinner small></b-spinner>둥록</b-button>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewForm',
  data() {
    return {
      reviewTitle: null,
      reviewScore: 5,
      reviewContent: null,
      btnBoolean: true,
    }
  },
  beforeCreate() {
    if (!localStorage.getItem('jwt')) {
      this.$router.push({name: 'Login'})
    }
  },
  methods: {
    ...mapActions(['userpoint']),
    addReview() {
      if (this.reviewScore < 0 || this.reviewScore > 5) {
        alert('평점은 0에서 5 사이의 숫자를 입력하세요!')
        this.reviewScore = null
      } else if (!this.reviewTitle.trim()) {
        this.reviewTitle = null
        alert('제목을 입력하세요.\n빈값은 입력할 수 없습니다!')
      } else if (!this.reviewContent.trim()) {
        this.reviewContent = null
        alert('내용을 입력하세요.\n빈값은 입력할 수 없습니다!')
      } else {
        this.btnBoolean = false
        const review = {
          rank: this.reviewScore,
          title: this.reviewTitle,
          content: this.reviewContent,
          movie_id: this.detailMovieInfo.id,
          movietitle: this.detailMovieInfo.title,
        }
        // console.log(review)      // 리뷰에 잘 들어갔는지 확인
        // 리뷰 DB에 저장해 달라는 요청
        this.$axios({
          method: 'post',
          url: `${SERVER_URL}/community/review/`,
          headers: this.setToken,
          data: review
        })
        .then(res => {
          // console.log(res.data)      // 응답 잘 받아왔는지 확인
          // 응답 받으면 포인트 올려달라는 요청 보내고
          this.userpoint('wr')
          // Detail Review 페이지로 넘어간다
          this.$router.push({name: 'DetailReview', params: {reviewId: res.data.id}})
        })
        .catch(err => {
          console.log(err)
        })
      }
    },
  },
  computed: {
    ...mapState(['detailMovieInfo']),
    ...mapGetters(['setToken']),
  },
  created() {
    document.title = 'GwakLee-Review✍'
  }
}
</script>

<style>
/* .review-background {
  opacity: 0.5;
} */
</style>