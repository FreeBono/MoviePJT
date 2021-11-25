<template>
  <div class="profile">
    <br>
    <br>
    <!-- point img -->
    <i v-if="profileInfo.point < 500" class="fas fa-baby fa-7x" style="color: #FF8C0A; opacity: 0.4"></i>
    <i v-else-if="profileInfo.point < 1000" class="fas fa-child fa-7x" style="color: #FF8C0A; opacity: 0.6"></i>
    <i v-else-if="profileInfo.point < 2000" class="fas fa-walking fa-7x" style="color: #FF8C0A; opacity: 0.8"></i>
    <i v-else class="fas fa-skiing fa-7x" style="color: #FF8C0A"></i>
    <br>
    <br>
    <br>
    <br>
    <div class="d-flex justify-content-between">
      <div class="col-3" style="font-size:3em; color:teal; opacity:0.5;">
        {{profileInfo.username}}
        <hr style="color:black;">
      </div>
      <div v-if="profileInfo.username !== userInfo.username" class="col-3 ">
        <button v-if="isFollow" class="follow-btn" style="background-color: #6EE0FF; color:white; border-radius: 5px;" @click="changeFollow">UnFollow</button>
        <button v-else class="follow-btn" style="background-color: teal; opacity:0.5; color:white; border-radius: 5px;" @click="changeFollow">Follow</button>
      </div>
    </div>
    <br>
    <br>
    <h5 class="d-flex justify-content-between" style="color:gray">
      <div class="col-3" >
        <div id="followers" >{{ followings }}</div>
        <div>팔로우</div>
      </div >
      <div class="col-3">
        <div id="followings" >{{ followers }}</div>
        <div>팔로워</div>
      </div>
      <div class="col-3">
        <div c>{{profileInfo.point}}</div>
        <div>포인트</div>
      </div>
      <div class="col-3">
        <div >{{profileInfo.userreviews.length}}</div>
        <div> 리뷰수  </div>
      </div>
    </h5>
    <br>
    <br>
    <div class="reivew-list">
      <div class="d-flex" style="color:#FF8C0A;font-size:20px;">
        <div class="col-3">Movie</div>
        <div class="col-5">Title</div>
        <div class="col-1">Rating</div>
        <div class="col-1">Like</div>
        <div class="col-2">Contents</div>
      </div>
      <hr style="color:#FF8C0A;">
      <div v-for="review in profileInfo.userreviews" :key="review.id" class="d-flex justify-content-between reviews ">
        <div class='col-3' style="text-align:left;" @click="wantGoDetailMovie(review.movie)">{{ review.movietitle }}</div>
        <div class='col-5' style="text-align:left;" @click="goDetailReview(review.id, review.username)">{{ review.title }}</div>
        <div class='col-1' @click="goDetailReview(review.id, review.username)">{{ review.rank }}</div>
        <div class='col-1' @click="goDetailReview(review.id, review.username)">{{ review.like.length }}</div>
        <div class='col-2 text-center my-3'>
          <button style="background-color: teal; opacity:0.5; color:white; border-radius: 5px;" v-b-modal:[`edit-modal-${review.id}`]>Detail</button>
          <b-modal :id="`edit-modal-${review.id}`">
            <h2>Content</h2>
            <br>
            {{review.content}}
          </b-modal>
        </div>
        
      </div>
    </div>
  </div>
</template>


<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL
import { mapGetters, mapState, mapActions } from 'vuex'

export default {
  name: 'Profile',
  data() {
    return {
      profileInfo: {},
      followers: 0,
      followings: 0,
      isFollow: false,
    }
  },
  methods: {
    ...mapActions(['goDetailReview', 'wantGoDetailMovie']),
    changeFollow() {
      // console.log(this.profileInfo.username)
      // 프로필 페이지 주인의 이름을 담아서 요청
      this.$axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/follow/`,
        headers: this.setToken,
        data: {profileName: this.profileInfo.username}
      })
      .then(res => {
        const { following, follower_count } = res.data
        const followBtn = document.querySelector('.follow-btn')
        const followersTag = document.querySelector('#followers')
        followBtn.innerText = following ? 'Unfollow' : 'Follow'
        followersTag.innerText = follower_count
      })
      .catch(err => {
        console.log(err)
      })
    },
    makeDate(datetime) {
      const old = ''+datetime
      return old.substring(0,10)
    },
  },
  created() {
    document.title = 'GwakLee-Profile🎅'
    // 이 페이지 user의 정보 받아오기
    const profileName = this.$route.params.username
    this.$axios({
      method: 'get',
      url: `${SERVER_URL}/accounts/profile/${profileName}`,
      headers: this.setToken,
    })
    // 프로필 정보 저장
    .then(res => {
      console.log(res.data)
      const profileInfo = res.data[0]
      // console.log(profileInfo)
      const { followers, followings } = profileInfo
      const followerList = []
      this.profileInfo = profileInfo
      this.followers = followers.length
      this.followings = followings.length
      followers.forEach(follower => {
        followerList.push(follower.id)
      })
      if (followerList.length && followerList.includes(this.userInfo.id)) {
        this.isFollow = true
      }
    })
    .catch(err => {
      console.log(err)
    })
  },
  computed: {
    ...mapGetters(['setToken']),
    ...mapState(['userInfo'])
  }
}
</script>


<style scoped>


</style>