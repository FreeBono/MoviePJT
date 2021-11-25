<template>
  <div class="upcoming-movies">
    <div id="carouselCaptions" class="carousel carousel-dark slide" data-bs-ride="carousel">
      <div class="carousel-inner" >
        <div @click="goDetailMovie(movies[0].id)" class="carousel-item active" >
          <a href="" ></a>
          <img :src="movies[0].backdrop_path" class="d-block w-100" alt="movie img" height="240" style="border-radius: 7px;">
          <div id="foot" class="carousel-caption d-none d-md-block">
            <a vertical-align="bottom" align="left" style=" position:realtive; background-color: rgba(0, 0, 0, 0.7); display:block; width:100%; color:white;">
              <p style="font-style:italic; color:yellow; font-weight: bold; vertical-align:bottom;">UPCOMING MOVIE</p>
              <p style="font-size:small; text-align:justify vertical-align:bottom;">{{ movies[0].title }}    ({{ movies[0].original_title }}) {{movies[0].release_date}}</p>
            </a>
            
          </div>
        </div>
        <div @click="goDetailMovie(movies[1].id)" class="carousel-item">
          <img :src="movies[1].backdrop_path" class="d-block w-100" alt="movie img" height="240" style="border-radius: 7px;">
          <div id="foot" class="carousel-caption d-none d-md-block">
            <a vertical-align="bottom" align="left" style=" position:realtive; background-color: rgba(0, 0, 0, 0.7); display:block; width:100%; color:white;">
              <p style="font-style:italic; color:yellow; font-weight: bold; vertical-align:bottom;">UPCOMING MOVIE</p>
              <p style="font-size:small; font-style: bold; text-align:justify vertical-align:bottom;">{{ movies[1].title }}    ({{ movies[1].original_title }}) {{movies[1].release_date}}</p>
            </a>
          </div>
        </div>
        <div @click="goDetailMovie(movies[2].id)" class="carousel-item">
          <img :src="movies[2].backdrop_path" class="d-block w-100" alt="movie img" height="240" style="border-radius: 7px;">
          <div id="foot" class="carousel-caption d-none d-md-block">
            <a vertical-align="bottom" align="left" style=" position:realtive; background-color: rgba(0, 0, 0, 0.7); display:block; width:100%; color:white;">
              <p style="font-style:italic; color:yellow; font-weight: bold; vertical-align:bottom;">UPCOMING MOVIE</p>
              <p style="font-size:small; font-style: bold; text-align:justify vertical-align:bottom;">{{ movies[2].title }}    ({{ movies[2].original_title }}) {{movies[2].release_date}}</p>
            </a>
          </div>
        </div>
        <div @click="goDetailMovie(movies[3].id)" class="carousel-item">
          <img :src="movies[3].backdrop_path" class="d-block w-100" alt="movie img" height="240" style="border-radius: 7px;">
          <div id="foot" class="carousel-caption d-none d-md-block">
            <a vertical-align="bottom" align="left" style=" position:realtive; background-color: rgba(0, 0, 0, 0.7); display:block; width:100%; color:white;">
              <p style="font-style:italic; color:yellow; font-weight: bold; vertical-align:bottom;">UPCOMING MOVIE</p>
              <p style="font-size:small; font-style: bold; text-align:justify vertical-align:bottom;">{{ movies[3].title }}    ({{ movies[3].original_title }}) {{movies[3].release_date}}</p>
            </a>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselCaptions" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselCaptions" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
const IMG_URL = process.env.VUE_APP_IMG_URL

export default {
  name: 'UpcomingMovie',
  data() {
    return {
      movies: []
    }
  },
  methods: {
    ...mapActions(['goDetailMovie']),
  },
  created() {
    const upcomingMovies = this.upcomingMovies
    upcomingMovies.forEach(upcomingMovie => {
      this.movies.push({
        id: upcomingMovie.movie_id,
        title: upcomingMovie.title,
        overview: upcomingMovie.overview,
        release_date: upcomingMovie.release_date,
        original_title: upcomingMovie.original_title,
        backdrop_path: `${IMG_URL}${upcomingMovie.backdrop_path}`,
      })
    })
  },
  computed: {
    ...mapState(['upcomingMovies']),
    imgSrc () {
      const imgPath = this.upcomingMovie.backdrop_path
      return `${IMG_URL}${imgPath}`
    },
    upcomingMovieId () {
      return this.upcomingMovie.movie_id
    }
  }
}
</script>


<style scoped>
.upcoming-movies {
  width: 50%;
  height: 15rem;
  background-color: aliceblue;
}

p {
  text-align: start;
  margin-left: 10px;
  margin: 5px 0px 5px 5px;
  color: white;

}

#foot{
  /* position :absolute; */
  clear:left;
  float:left;
  padding:0%
}

#inbox {
  width: 100%;
}
</style>