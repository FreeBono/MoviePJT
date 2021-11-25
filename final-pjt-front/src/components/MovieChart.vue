<template>
  <div class="movie-chart">
    <span @click="goDetailMovie(movieId)" id="cursor-hover">{{movie.title}}</span>
    <hr>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'MovieChart',
  props: {
    movie: {
      type: Object
    }
  },
  methods: {
    ...mapActions(['goDetailMovie']),
  },
  computed: {
    movieId() {
      return this.movie.movie_id
    }
  }
}
</script>

<style scoped>

</style>