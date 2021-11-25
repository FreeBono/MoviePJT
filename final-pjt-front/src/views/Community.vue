<template>
  <div id="app">
    <div class="d-flex justify-content-around my-3 mx-3 align-content-stretch " style="height:250px">
      <b-tabs class="col-4" content-class="mt-3" style= "width:370;">
        <b-tab title="HOT like" active>
          <div v-for="menu in menuList" :key="menu.id" :menu="menu" style="text-align:left; height:50; " class="row d-flex align-items-center" >
            <span class="badge col-2 rounded-pill bg-info text-white" >Hot!</span><span class="col-7 mb-2" @click="goDetailReview(menu.id)">{{menu.title}}&nbsp;</span>
            <span class="col-3 text-danger" style="text-align:right ">+{{menu.like.length}}</span>
            <hr>
          </div>
        </b-tab>
        <b-tab title="HOT comment">
          <div v-for="comment in comments" :key="comment.id" :comment="comment" style="text-align:left; height:50;" class="row d-flex align-items-center">
            <span class="badge col-2 rounded-pill bg-info text-white">Hot</span><span class="col-7 mb-2" @click="goDetailReview(comment.id)">{{comment.title}}&nbsp;</span>
            <span class="col-3 text-danger" style="text-align:right">+{{comment.comments.length}}</span>
            <hr>
          </div>
        </b-tab>
      </b-tabs>
      <b-embed
        class="col-6" 
        type="iframe"
        aspect="16by9"
        src="https://www.youtube.com/embed/YHWPSOAEhrg"
        allowfullscreen
        style = "width:540px; height:240px;"
      ></b-embed>
    </div>
    <br>
    <div class="overflow-auto ">
        <b-table id="my-table" class=" border border-black" :items="items" :fields="fields" :per-page="perPage" :current-page="currentPage" small >
          <template #cell(index)="data">{{ data.index + 1 + (currentPage-1)*10 }}</template>
          <template #cell(movietitle)="data" >
            <b v-if="inMovieTitle(data.item.movietitle)"
              @click="wantGoDetailMovie(data.item.movie)">{{data.item.movietitle}}&nbsp;&nbsp;
              <i class="fas fa-thumbs-up" style="color:#3CB4FF"></i>
            </b>
            <b v-else @click="wantGoDetailMovie(data.item.movie)">{{data.item.movietitle}}</b>
          </template>
          <template #cell(title)="data" >
            <b @click="goDetailReview(data.item.id)">{{data.item.title}}&nbsp;&nbsp;<span class="badge bg-warning" style="color:white">{{data.item.comments.length}}</span></b>
          </template>
          <template #cell(username)="data">
            <b v-if="data.item.username === topUsers[0].username" @click="goProfile(data.item.username)" title="🥇">
              <i class="fas fa-crown fa-xs" style="color:gold;"></i>&nbsp;&nbsp;{{data.item.username}}
            </b>
            <b v-else-if="data.item.username === topUsers[1].username" @click="goProfile(data.item.username)" title="🥈">
              <i class="fas fa-crown fa-xs" style="color:silver;"></i>&nbsp;&nbsp;{{data.item.username}}
            </b>
            <b v-else-if="data.item.username === topUsers[2].username" @click="goProfile(data.item.username)" title="🥉">
              <i class="fas fa-crown fa-xs" style="color:brown;"></i>&nbsp;&nbsp;{{data.item.username}}
            </b>
            <b v-else @click="goProfile(data.item.username)">{{data.item.username}}</b>
          </template>
          <template #cell(created_at)="data">
            <b >{{makeDate(data.item.created_at)}}</b>
          </template>
          
        </b-table>
      <br>
      <div class="overflow-auto">
        <b-pagination align="center" v-model="currentPage" pills :total-rows="rows" :per-page="perPage" aria-controls="my-table" size="lg">
        </b-pagination>
      </div>
    </div>
  </div>
</template>


<script>
import { mapGetters, mapActions, mapState } from 'vuex'
const SERVER_URL = process.env.VUE_APP_SERVER_URL


export default {
  name: 'community',
  data(){
      return{
        fields: ['index','movietitle','title','username','created_at'],
        items: [],
        menuList : [],
        reviews: [],
        comments: [],
        topRatedMovie : [],
        perPage : 10,
        currentPage : 1,
        cnt : 0
      }
  },
  computed : {
      rows(){
          return this.items.length;
      },
      ...mapState(['topUsers','topRatedMovies']),
      ...mapGetters(['setToken']),
  },
  beforeCreate() {
    if (!localStorage.getItem('jwt')) {
      this.$router.push({name: 'Login'})
    }
  },
  created() {
    document.title = 'GwakLee-Community'
    // 모든 review 다 달라는 요청 보내기
    this.$axios({
      method: 'get',
      url: `${SERVER_URL}/community/review/`,
      headers: this.setToken,
    })
    // 응답 받은 모든 리뷰 저장하기
    .then(res => {
      console.log(res.data)
      this.items = res.data
      this.reviews = res.data
      this.reviews.sort(function(a,b){
        if (a.like.length > b.like.length){
          return -1
        }
      })
      this.reviews.forEach(review => {
        if (this.menuList.length <= 3) {
          this.menuList.push(review)
        }
      })
      this.reviews.sort(function(a,b){
        if (a.comments.length > b.comments.length){
          return -1
        }
      })
      this.reviews.forEach(review => {
        if (this.comments.length <= 3) {
          this.comments.push(review)
        }
      })
      // console.log(this.comments)
    })
    .catch(err => {
      console.log(err)
    }),
    this.topRatedMovies.forEach(movie => {
      this.topRatedMovie.push(movie.title)
    })
  },
  methods: {
    ...mapActions(['goProfile', 'goDetailReview', 'wantGoDetailMovie']),
    makeDate(datetime) {
      const old = ''+datetime
      return old.substring(5,10)
    },
    inMovieTitle(movietitle) {
      return this.topRatedMovie.filter(top => top === movietitle).length === 0 ? false : true
    },
    // tabBar(reviews) {
    //   const revie = []
    //   this.reviews.forEach(review => {
    //     revie.push(review.title)
    //     revie.push(review.like.length)
    //   })
    }
}   
</script>

<style scoped>
#my-table {
  text-align: left;
}

template {
  background-color: #bbdefb;
}


</style>