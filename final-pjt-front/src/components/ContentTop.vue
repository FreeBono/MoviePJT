<template>
  <div class="content-top">
    <div class="d-flex flex-row">
      <UpcomingMovie/>
      <div class="recommend">
        <img src="@/assets/question.gif" alt="recommend img" @click="showRecommend">
      </div>
      <div align="left" class="top-user">
        <div class="mx-2 my-2 py-1">
          <i class="fas fa-grip-lines-vertical fa-2x" style="color:red"></i>
          <h3 class="mb-0" style="display:inline-block; font-weight: bolder">
            <span>Top User</span>
          </h3>
        </div>
        <hr style="height:5px " class="mb-2 mt-0">
        <div style="font-size:large" class="row my-3 mx-2 d-flex align-items-center text-truncate" title="🥇">
          <i class="fas fa-crown fa-2x col-3"></i>
          <p @click="goProfile(topUsers[0].username)" class="col-6 top-user-info text-truncate text-center" id="cursor-hover">{{topUsers[0].username}}</p>
          <p class="top-user-info col-3">{{topUsers[0].point}}</p>
        </div> 
        <div style="font-size:large" class="row my-3 mx-2 d-flex align-items-center text-truncate" title="🥈">
          <i class="fas fa-crown fa-2x col-3" style="color:silver"></i>
          <p @click="goProfile(topUsers[1].username)" class="col-6 top-user-info text-truncate text-center" id="cursor-hover">{{topUsers[1].username}}</p>
          <p class="top-user-info col-3">{{topUsers[1].point}}</p>
        </div>
        <div style="font-size:large" class="row my-3 mx-2 d-flex align-items-center text-truncate" title="🥉">
          <i class="fas fa-crown fa-2x col-3" style="color:brown"></i>
          <p @click="goProfile(topUsers[2].username)" class="col-6 top-user-info text-truncate text-center" id="cursor-hover">{{topUsers[2].username}}</p>
          <p class="top-user-info col-3">{{topUsers[2].point}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import UpcomingMovie from '@/components/UpcomingMovie'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'ContentTop',
  components: {
    UpcomingMovie,
  },
  methods: {
    ...mapActions(['goProfile', 'userpoint']),
    showRecommend() {
      if (this.userInfo.username) {
        if (this.userInfo.point >= 200) {
          if (confirm('100~200point가 random으로 차감됩니다.\nPremium Service를 이용하시려면 확인버튼을 눌러주세요.') == true) {
            this.userpoint('pmr')
            this.$router.push({name: 'RecommendMovies'})
          } else {
            return
          }
        } else {
          alert('Premium Service를 이용할 수 없습니다.\n최소 200point가 필요합니다.')
        }
      } else {
        this.$router.push({name: 'Login'})
      }
    },
  },
  computed: {
    ...mapState(['upcomingMovies', 'topUsers', 'userInfo'])
  }
}
</script>

<style scoped>
.upcoming-movies {
  width: 50%;
  height: 15rem;
}
.recommend {
  width: 25%;
  height: 15rem;
}
.top-user {
  width: 25%;
  height: 15rem;
  background-color: oldlace;
  overflow: hidden;
}
.recommend > img {
  width: 100%;
  height: 15rem;
}
.fas {
  color : gold
}
.top-user-info {
  margin: 0;
}
</style>