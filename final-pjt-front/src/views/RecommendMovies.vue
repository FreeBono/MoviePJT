<template>


    <div>
      <h1 class="my-4">Premium Recommendation</h1>
      <h5>Select your favorite One</h5>
      <hr>
      <div class="row row-cols-1 row-cols-md-6 g-4 my-3">
        <div v-for="movie in casemovie" :key="movie.id" class="col">
          <div @click="choiceMovie(movie.id)" class="card">
            <img :src="movie.poster_path" class="card-img-top poster-img btn" alt="movie poster" height="320" type="button" data-bs-toggle="modal" data-bs-target="#modalId">
          </div>
        </div>
      </div>
      <div class="modal fade" id="modalId" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="modalLabel">I think..you will like these movies!</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <p v-for="(rec, idx) in recmovies" :key="idx">{{ idx+1 }}위 {{ rec.title }}</p>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div>
    </div>

</template>


<script>
import { mapGetters } from 'vuex'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
const IMG_URL = process.env.VUE_APP_IMG_URL

export default {
  name: 'RecommendMovies',
  data() {
    return {
  
      casemovie: [],
      recmovies: [],
    }
  },
  beforeCreate() {
    if (!localStorage.getItem('jwt')) {
      this.$router.push({name: 'Login'})
    }
  },

  created() {
    document.title = 'GwakLee-영화를 추천하지🕵️‍♂️'
    // 초기 영화 12개 달라는 요청
    this.$axios({
      method: 'get',
      url: `${SERVER_URL}/movies/casemovie/`,
      headers: this.setToken,
    })
    .then(res => {
      const moviesall = res.data
      moviesall.forEach(movieall => {
        this.casemovie.push({
          id: movieall.movie_id,
          title: movieall.title,
          poster_path: `${IMG_URL}${movieall.poster_path}`,
          overview: movieall.overview,
        })
      })
      // console.log(this.casemovie)
    })
    .catch(err => {
      console.log(err)
    })
  },
  computed: {
    ...mapGetters(['setToken']),
  },
  methods: {
    choiceMovie(movieId) {
      this.$axios({
        method: 'post',
        url: `${SERVER_URL}/movies/premiumrecmovie/`,
        headers: this.setToken,
        data: {movieId: movieId}
      })
      .then(res => {
        this.recmovies = res.data
      })
      .catch(err => {
        console.log(err)
      })
    },
  }
}
</script>

<style scoped>
.card {
  height: 20rem;
}
</style>