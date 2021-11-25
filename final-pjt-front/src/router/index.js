import Vue from 'vue'
import VueRouter from 'vue-router'

import Community from '@/views/Community'
import DetailMovie from '@/views/DetailMovie'
import DetailReview from '@/views/DetailReview'
import EditReviewForm from '@/views/EditReviewForm'
import Login from '@/views/Login'
import MovieHome from '@/views/MovieHome'
import Profile from '@/views/Profile'
import RecommendMovies from '@/views/RecommendMovies'
import ReviewForm from '@/views/ReviewForm'
import SearchList from '@/views/SearchList'
import Signup from '@/views/Signup'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MovieHome',
    component: MovieHome
  },
  {
    path: '/movies/recommend',
    name: 'RecommendMovies',
    component: RecommendMovies
  },
  {
    path: '/movie/:movieId',
    name: 'DetailMovie',
    component: DetailMovie
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/accounts/:username',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/community',
    name: 'Community',
    component: Community
  },
  {
    path: '/movie/:movieId/review',
    name: 'ReviewForm',
    component: ReviewForm
  },
  {
    path: '/review/:reviewId',
    name: 'DetailReview',
    component: DetailReview
  },
  {
    path: '/review/:reviewId/edit',
    name: 'EditReviewForm',
    component: EditReviewForm
  },
  {
    path: '/serch/:searchText',
    name: 'SearchList',
    component: SearchList
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
