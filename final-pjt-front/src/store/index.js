import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import Router from 'vue-router'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'
import _ from 'lodash'
// import { Vue } from 'vue'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)

Vue.use(Vuex)
Vue.use(Router)

const SERVER_URL = process.env.VUE_APP_SERVER_URL
const TMDB_API_KEY = process.env.VUE_APP_TMDB_API_KEY
const IMG_URL = process.env.VUE_APP_IMG_URL

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    userInfo: {id: null, username: null, point: 0},
    jwtToken: null,
    detailMovieInfo: {},
    upcomingMovies: [],
    popularMovies: [],
    topRatedMovies: [],
    latestMovies: [],
    topUsers: [],
    allMovies: [],
    bestReviewers: [],
    searchMovies: [],
    reviewInfo: {title: null, rank: null, content: null},
  },
  mutations: {
    SAVE_TOKEN(state, tk) {
      state.jwtToken = tk
    },
    LOGOUT(state) {
      state.userInfo = {id: null, username: null, point: 0}
      state.jwtToken = null
      state.detailMovieInfo = {}
      state.searchMovies = []
      state.reviewInfo = {title: null, rank: null, content: null}
    },
    SAVE_DETAIL_MOVIE(state, detailMovieInfo) {
      state.detailMovieInfo = detailMovieInfo
      const { poster_path, backdrop_path } = detailMovieInfo
      state.detailMovieInfo.poster_path = `${IMG_URL}${poster_path}`
      state.detailMovieInfo.backdrop_path = `${IMG_URL}${backdrop_path}`
    },
    UPDATE_USER_INFO(state, data) {
      state.userInfo = data
    },
    UPDATE_POINT(state, point) {
      state.userInfo.point = point
    },
    GET_POPULAR_MOVIES(state, data) {
      state.popularMovies = data
      const tmp = []
      data.forEach(movie => {
        tmp.push({movie_id: movie.movie_id, title: movie.title, poster_path: movie.poster_path})
      })
      const allInfo = state.allMovies.concat(tmp)
      state.allMovies = _.uniqBy(allInfo, 'movie_id')
      // state.popularMovies = null
    },
    GET_TOP_RANKED_MOVIES(state, data) {
      state.topRatedMovies = data
      const tmp = []
      data.forEach(movie => {
        tmp.push({movie_id: movie.movie_id, title: movie.title, poster_path: movie.poster_path})
      })
      const allInfo = state.allMovies.concat(tmp)
      state.allMovies = _.uniqBy(allInfo, 'movie_id')
      // state.topRatedMovies = null
    },
    GET_UPCOMING_MOVIES(state, data) {
      state.upcomingMovies = data
      const tmp = []
      data.forEach(movie => {
        tmp.push({movie_id: movie.movie_id, title: movie.title, poster_path: movie.poster_path})
      })
      const allInfo = state.allMovies.concat(tmp)
      state.allMovies = _.uniqBy(allInfo, 'movie_id')
      // state.upcomingMovies = null
    },
    GET_LATEST_MOVIES(state, data) {
      state.latestMovies = data
      const tmp = []
      data.forEach(movie => {
        tmp.push({movie_id: movie.movie_id, title: movie.title, poster_path: movie.poster_path})
      })
      const allInfo = state.allMovies.concat(tmp)
      state.allMovies = _.uniqBy(allInfo, 'movie_id')
      // state.latestMovies = []
    },
    SAVE_DETAIL_REVIEW(state, data) {
      state.reviewInfo = data
    },
    SAVE_TOP_USERS(state, data) {
      state.topUsers = data
    },
    SAVE_SEARCH_LIST(state, data) {
      state.searchMovies = data
      const tmp = []
      data.forEach(movie => {
        tmp.push({movie_id: movie.movie_id, title: movie.title, poster_path: movie.poster_path})
      })
      const allInfo = state.allMovies.concat(tmp)
      state.allMovies = _.uniqBy(allInfo, 'movie_id')
    },
    SAVE_REVIEW_KING(state, data) {
      state.bestReviewers = data
    }
  },
  actions: {
    saveToken({ commit }, tk) {
      commit('SAVE_TOKEN', tk)
    },
    logout({ commit }) {
      commit('LOGOUT')
    },
    saveDetailMovie({ commit }, movieId) {
      // console.log(movieId)
      axios({
        method: 'get',
        url:`https://api.themoviedb.org/3/movie/${movieId}?api_key=${TMDB_API_KEY}&language=ko-KR`,
      })
      .then(res => {
        commit('SAVE_DETAIL_MOVIE', res.data)
      })
      .catch(err => {
        console.log(err)
      })
    },
    userpoint({ state, commit }, where) {
      const tk = state.jwtToken
      const config = {Authorization: `JWT ${tk}`}
      axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/userpoint/`,
        headers: config,
        data: {where: where}
      })
      .then(res => {
        commit('UPDATE_POINT', res.data.point)
      })
      .catch(err => {
        console.log(err)
      })
    },
    getMovies({ commit }, where) {
      // const where = where
      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/${where}/`,
      })
      .then(res => {
        if (where === 'popular') {
          commit('GET_POPULAR_MOVIES', res.data)
        }
        if (where === 'top_rated') {
          commit('GET_TOP_RANKED_MOVIES', res.data)
        }
        if (where === 'upcoming') {
          commit('GET_UPCOMING_MOVIES', res.data)
        }
        if (where === 'latest') {
          commit('GET_LATEST_MOVIES', res.data)
        }
      })
      .catch(err => {
        console.log(err)
      })
    },
    saveDetailReview({ commit }, data) {
      commit('SAVE_DETAIL_REVIEW', data)
    },
    goProfile(context, username) {
      router.push({name: 'Profile', params: {username: username}})
      .catch(() => {
        router.go(0)
      })
    },
    updateUserInfo({ commit }, data) {
      commit('UPDATE_USER_INFO', data)
      commit('UPDATE_POINT', data.point)
    },
    goDetailReview({ state, dispatch }, reviewId, reviewer) {
      const { username, point } = state.userInfo
      if (username !== reviewer) {
        if (point >= 20) {
          dispatch('userpoint', 'rr')
          router.push({ name: 'DetailReview', params: { reviewId: reviewId } })
        } else {
          alert('포인트가 부족하여 리뷰를 볼 수 없습니다. 😓\n200포인트가 필요해요!')
        }
      }
    },
    goDetailMovie(context, movieId) {
      router.push({ name: 'DetailMovie', params: { movieId: movieId } })
      // .catch(() => router.go(0))
    },
    saveTopUsers({ commit }, data) {
      commit('SAVE_TOP_USERS', data)
    },
    wantGoDetailMovie({ state, dispatch }, mId) {
      const tk = state.jwtToken
      const config = {Authorization: `JWT ${tk}`}
      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/givemovieid/${mId}/`,
        headers: config,
      })
      .then(res => {
        dispatch('goDetailMovie', res.data[0].movie_id)
      })
      .catch(err => {
        console.log(err)
      })
    },
    saveSearchList({ commit }, data) {
      commit('SAVE_SEARCH_LIST', data)
    },
    saveReviewKing({ commit }, data) {
      commit('SAVE_REVIEW_KING', data)
    }
  },
  getters: {
    setToken(state) {
      const tk = state.jwtToken
      const config = {Authorization: `JWT ${tk}`}
      return config
    }
  },
  modules: {
  }
})
