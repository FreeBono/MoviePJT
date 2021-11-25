<template>
  <div class="search-list">
    <h1 class="my-4">검색한거 보여주는 페이지</h1>
    <hr>
    <div v-if="similarMovies.length > 0">
      <h3>검색어와 관계있는 영화</h3>
      <div class="row row-cols-1 row-cols-md-6 g-4 my-3">
        <div v-for="movie in similarMovies" :key="movie.movie_id" class="col">
          <div @click="goDetailMovie(movie.id)" class="card">
            <img :src="movie.poster_path" class="card-img-top poster-img btn" alt="movie poster" height="320">
          </div>
        </div>
      </div>
      <div v-if="etcMovies.length > 0">
        <hr>
        <h3>기타 추천 영화</h3>
        <div class="row row-cols-1 row-cols-md-6 g-4 my-3">
          <div v-for="movie in etcMovies" :key="movie.movie_id" class="col">
            <div @click="goDetailMovie(movie.id)" class="card">
              <img :src="movie.poster_path" class="card-img-top poster-img btn" alt="movie poster" height="320">
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <h3>유사한 영화가 없습니다</h3>
      <p>이런 영화는 어떠세요??</p>
      <div class="row row-cols-1 row-cols-md-6 g-4 my-3">
        <div v-for="movie in etcMovies" :key="movie.movie_id" class="col">
          <div @click="goDetailMovie(movie.id)" class="card">
            <img :src="movie.poster_path" class="card-img-top poster-img btn" alt="movie poster" height="320">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { mapState, mapActions } from 'vuex'
const IMG_URL = process.env.VUE_APP_IMG_URL

export default {
  name: 'SearchList',
  data() {
    return {
      similarMovies: [],
      etcMovies: []
    }
  },
  computed: {
    ...mapState(['searchMovies']),
  
  },
  methods :{
    ...mapActions(['goDetailMovie'])
  },
  created() {
    this.searchMovies.forEach(movie => {
      if (movie.similarity > 0) {
        this.similarMovies.push({
          id: movie.movie_id,
          title: movie.title,
          poster_path: `${IMG_URL}${movie.poster_path}`,
          overview: movie.overview,
          similarity: movie.similarity,
        })
      } else {
        this.etcMovies.push({
          id: movie.movie_id,
          title: movie.title,
          poster_path: `${IMG_URL}${movie.poster_path}`,
          overview: movie.overview,
          similarity: movie.similarity,
        })
      }
    })
  }
}
</script>

<style scoped>

</style>