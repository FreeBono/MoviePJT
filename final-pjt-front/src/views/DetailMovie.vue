<template>
  <div class="detail-movie">
    <div class="d-flex justify-content-between align-items-center">
      <h1 class="my-4" id="detail-movie-title">{{ detailMovieInfo.title }}</h1>
      <div @click="goReviewForm" class="fas fa-keyboard fa-3x" style="color:teal; opacity:0.5" id="cursor-hover" title="리뷰 작성"></div>
    </div>
    <hr class="detail-movie-hr">
    <div class="d-flex flex-row contents">
      <img :src="detailMovieInfo.poster_path" @click="bigPoster(detailMovieInfo.poster_path)" alt="poster" class="detail-movie-poster">
      <div class="br"></div>
      <img v-if="!detailMovieInfo.video" :src="detailMovieInfo.backdrop_path" alt="backdrop" class="backdrop-or-video">
    </div>
    <div class="overview my-3">
      {{ detailMovieInfo.overview }}
    </div>
    <div class="etc row mb-3">
      <div v-if="detailMovieInfo.runtime" class="col-4">
        <h5>상영시간</h5><p>{{ detailMovieInfo.runtime }}분</p>
      </div>
      <div v-if="detailMovieInfo.tagline" class="col-4">
        <h5>tagline</h5><p>{{ detailMovieInfo.tagline }}</p>
      </div>
      <div v-if="detailMovieInfo.release_date" class="col-4">
        <h5>release date</h5><p>{{ detailMovieInfo.release_date }}</p>
      </div>
      <div v-if="detailMovieInfo.homepage" class="col-4">
        <h5>홈페이지</h5><p @click="goHompage" id="cursor-hover">{{ detailMovieInfo.homepage }}</p>
      </div>
      <div v-if="detailMovieInfo.popularity" class="col-4">
        <h5>인기도</h5><p>{{ detailMovieInfo.popularity }}</p>
      </div>
      <div v-if="detailMovieInfo.vote_average" class="col-4">
        <h5>평점</h5><p>{{ detailMovieInfo.vote_average }}</p>
      </div>
      <div v-if="detailMovieInfo.genres.length > 0" class="col-4">
        <h5>장르</h5><span v-for="genreItem in detailMovieInfo.genres" :key="genreItem.id">{{ genreItem.name }} </span>
      </div>
    </div>
    <hr class="detail-movie-hr">
    <div class="rec-3-movie">
      <h4>Recommend Similar Genre Movie</h4>
      <div class="row row-cols-1 row-cols-md-3 g-4 d-flex justify-content-around my-2">
        <div v-for="movie in recoMovieList" :key="movie.id" class="col" id="detail-movie-col">
          <div @click="goDetailMovie(movie.id)" class="card" id="cursor-hover" title="따닥!">
            <img :src="movie.poster_path" class="card-img-top" alt="poster img">
            <div class="card-footer">
              <p class="card-text text-truncate">{{ movie.title }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapState, mapActions } from 'vuex'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
const IMG_URL = process.env.VUE_APP_IMG_URL

export default {
  name: 'DetailMovie',
  data() {
    return {
      recoMovieList: [],
    }
  },
  created() {
    document.title = 'GwakLee-Movie🎬'
    const {movieId} = this.$route.params
    // store에서 tmdb로 요청보내서 detailMovieInfo 저장
    this.saveDetailMovie(movieId)
    // 이 영화에 맞는 추천영화 3개 요청
    this.$axios({
      method: 'post',
      url: `${SERVER_URL}/movies/recmovie/`,
      headers: this.setToken,
      data: {movieId: movieId}
    })
    .then(res => {
      // console.log(res.data)
      res.data.forEach(recoM => {
        this.recoMovieList.push({
          id: recoM.movie_id,
          title: recoM.title,
          poster_path: `${IMG_URL}${recoM.poster_path}`,
          vote_average: recoM.vote_average,
          overview: recoM.overview,
        })
      })
    })
    .catch(err => {
      console.log(err)
    })
  },
  computed: {
    ...mapState(['detailMovieInfo']),
    ...mapGetters(['setToken']),
  },
  methods: {
    ...mapActions(['saveDetailMovie', 'goDetailMovie']),
    goReviewForm() {
      this.$router.push({name: 'ReviewForm', params: {movieId: this.detailMovieInfo.id}})
    },
    goHompage(e) {
      const hpUrl = e.target.innerText
      window.open(hpUrl)
    },
    bigPoster(url_poster) {
      window.open(url_poster)
    }
  }
}
</script>

<style>
.detail-movie-poster {
  width: 30%;
  cursor: zoom-in;
}
.contents > .br {
  width: 3%;
}
.backdrop-or-video {
  width: 67%;
}
#detail-movie-col {
  width: 20%;
}
.detail-movie-hr {
  margin-bottom: 2rem;
  margin-top: 0;
  border: 0;
  height: 5px;
  background-color: teal;
}
</style>