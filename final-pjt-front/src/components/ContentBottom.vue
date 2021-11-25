<template>
  <div class="d-flex flex-row content-bottom justify-content-between">
    <div class="popular">
      <div align="left" class="mx-2 mt-3" style="vertical-align:middle;"><i class="fas fa-grip-lines-vertical fa-2x mt-2" style="color:gold"></i><h4 class="mx-1 my-3" style="display:inline-block; font-weight: bolder; ">Popular Movies</h4></div>
      <hr style="height:5px; color:teal" class="mt-0">
      <div align="left" class="popular-chart mx-3">
        <div class="chart">
          <MovieChart style="font-size:medium" v-for="movie in popularMovies" :key="movie.id" :movie="movie"/>
        </div>
      </div>
    </div>
    <div class="top-rated">
      <div align="left" class="mx-2 mt-3" style="vertical-align:middle;"><i class="fas fa-grip-lines-vertical fa-2x mt-2" style="color:gold"></i><h4 class="mx-1 my-3" style="display:inline-block; font-weight: bolder; ">Top-Rated Movies</h4></div>
      <hr style="height:5px; color:teal" class="mt-0">
      <div align="left" class="top-rated-chart mx-3">
        <div>
          <MovieChart style="font-size:medium" v-for="movie in topRatedMovies" :key="movie.id" :movie="movie"/>
        </div>
      </div>
    </div>
    <div class="review-king">
      <div align="left" class="mx-2 mt-3" style="vertical-align:middle;"><i class="fas fa-grip-lines-vertical fa-2x mt-2" style="color:gold"></i><h4 class="mx-1 my-3" style="display:inline-block; font-weight: bolder; ">HOT baNaNas</h4></div>
      <hr style="height:5px; color:teal" class="mt-0">
      <div align="left" class="top-rated-chart mx-3">
        <div>
          <ReviewKing style="font-size:medium" v-for="reviewer in bestReviewers" :key="reviewer.id" :reviewer="reviewer"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieChart from '@/components/MovieChart'
import ReviewKing from '@/components/ReviewKing'
import { mapState, mapActions, mapGetters } from 'vuex'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ContentBottom',
  components: {
    MovieChart,
    ReviewKing,
  },
  created() {
    this.getMovies('popular')
    this.getMovies('top_rated')
    this.$axios({
      method: 'get',
      url: `${SERVER_URL}/community/reviewking/`,
      
    })
    .then(res => {
      // console.log(res.data)
      this.saveReviewKing(res.data)
    })
    .catch(err => {
      console.log(err)
    })
  },
  computed: {
    ...mapState(['popularMovies', 'topRatedMovies', 'bestReviewers']),
    ...mapGetters(['setToken'])
  },
  methods: {
    ...mapActions(['getMovies', 'saveReviewKing']),
  }
}
</script>

<style scoped>
.popular {
  /* width: 30%; */
  margin-left : 2%;
  border-right-style: solid;
  padding-right : 50px;
  border-color : skyblue;
  border-width: 1px;
  /* background-color: gainsboro; */
}

.review-king {
  width: 30%;
  margin-right : 30px;
  border-left-style: solid; 
  padding-left : 50px;
  border-color : skyblue;
  border-width: 1px;
  /* background-color: gainsboro;  */
}
</style>