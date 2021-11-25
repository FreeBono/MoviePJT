<template>
  <div>
    <h2 class="my-3">{{ detailMovieInfo.title }}'s Review</h2>
    <div class="mb-3">
      <label for="review-title" class="form-label">제목</label><br>
      <b-form-input v-model="reviewTitle" placeholder="제목을 입력하세요" id="review-title"></b-form-input>
    </div>
    <div class="mb-3">
      <label for="review-content" class="form-label">내용</label>
      <b-form-textarea v-model="reviewContent" id="review-content" class="form-control" placeholder="내용을 입력하세요" rows="10"></b-form-textarea>
    </div>
    <div class="mb-3">
      <label for="review-score" class="form-label">평점</label>
      <b-form-rating v-model="reviewScore" variant="warning" class="mb-2" id="review-score"></b-form-rating>
    </div>
    <b-button v-if="isEditReview" @click="updateReview" variant="outline-warning" title="빈칸은 등록되지 않습니다">수정</b-button>
    <b-button v-else variant="warning" disabled><b-spinner small></b-spinner>수정</b-button>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'EditReviewForm',
  data() {
    return {
      reviewTitle: null,
      reviewScore: null,
      reviewContent: null,
      isEditReview: true
    }
  },
  beforeCreate() {
    if (!localStorage.getItem('jwt')) {
      this.$router.push({name: 'Login'})
    }
  },
  methods: {
    ...mapActions(['userpoint']),
    updateReview() {
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
        this.isEditReview = false
        const review = {
          rank: this.reviewScore,
          title: this.reviewTitle,
          content: this.reviewContent,
          movie_id: this.detailMovieInfo.id,
          movietitle: this.detailMovieInfo.title
        }
        // console.log(review)
        this.$axios({
          method: 'put',
          url: `${SERVER_URL}/community/review/${this.reviewInfo.id}/`,
          headers: this.setToken,
          data: review
        })
        .then(res => {
          // console.log(res.data.id)
          this.$router.push({name: 'DetailReview', params: {reviewId: res.data.id}})
        })
        .catch(err => {
          console.log(err)
        })
      }
    }
  },
  computed: {
    ...mapState(['detailMovieInfo', 'reviewInfo']),
    ...mapGetters(['setToken']),
  },
  created() {
    document.title = 'GwakLee-Edit✍'
    this.reviewTitle = this.reviewInfo.title
    this.reviewScore = this.reviewInfo.rank
    this.reviewContent = this.reviewInfo.content
    this.reviewScore = this.reviewInfo.rank
  }
}
</script>

<style scoped>

</style>