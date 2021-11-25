<template>

  <!-- <div class="contnet-middle">
    <img v-for="movie in movies" :key="movie.id" :src="movie.poster_path" alt="poster img">
  </div> -->


  <div class="content-middle">
    <carousel :dots="false" :autoplay="true" :nav="false" :loop="true" :autoplayspped="12000" :autoplayHoverPause="true" :items="6">
      <img @click="goDetailMovie(movie.id)" class="carousel" v-for="movie in movies" :key="movie.id" :src="movie.poster_path" alt="poster img" id="cursor-hover">
    </carousel>
  </div>
</template>


<script>
import carousel from 'vue-owl-carousel'
import { mapState, mapActions } from 'vuex'
const IMG_URL = process.env.VUE_APP_IMG_URL

export default {
  name: 'ContentMiddle',
  data() {
    return {
      movies: []
    }
  },
  components: {
    carousel,
  },
  created() {
    this.getMovies('latest')
    const latestMs = this.latestMovies
    latestMs.forEach(latestmovie => {
      this.movies.push({
        id: latestmovie.movie_id,
        title: latestmovie.title,
        poster_path: `${IMG_URL}/${latestmovie.poster_path}`,
      })
    })
  },
  methods: {
    ...mapActions(['getMovies', 'goDetailMovie']),
  },
  computed: {
    ...mapState(['latestMovies'])
  }
}
</script>

<style scoped>
.content-middle {
  height: 17rem;
}
.carousel {
  position: relative;
  height: 100%;
  border-radius: 20px;
  overflow: hidden;
}
.carousel-text {
  position: absolute;
  bottom: 0;
  margin-left: 20px;
  z-index: 551;
  color: #ffffff;
}
.carousel-bg {
  width: 100%;
  position: absolute;
  bottom: 0;
  height: 100%;
  background: linear-gradient(transparent, #000000);
  opacity: 0.8;
  z-index: 550;
}
  .owl-carousel .owl-stage {
    display: flex;
  }

  .owl-carousel .owl-item img {
    width: 140px;
    height: 180px;
    padding-right: 10px;
    margin-top : 20px;
    margin-left : 10px;
    margin-right : 10px;
  }
</style>