<template>
  <div class="review-kings" >
    <div class="box1" @click="goDetailReview(reviewId)" id="cursor-hover">{{reviewer.title}} </div>
    <hr>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  naem: 'ReviewKing',
  props: {
    reviewer: {
      type: Object
    }
  },
  methods: {
    ...mapActions(['goDetailReview']),
  },
  computed: {
    reviewId() {
      return this.reviewer.review_id
    }
  }
}
</script>

<style scoped>

</style>