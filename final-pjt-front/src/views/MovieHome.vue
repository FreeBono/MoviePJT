<template>
  <div>
    <ContentTop class="content1"/>
    <br>
    <ContentMiddle class="content2"/>
    <br>
    <ContentBottom class="content3"/>
  </div>
</template>

<script>
import ContentTop from '@/components/ContentTop'
import ContentMiddle from '@/components/ContentMiddle'
import ContentBottom from '@/components/ContentBottom'
import { mapActions } from 'vuex'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieHome',
  components: {
    ContentTop,
    ContentMiddle,
    ContentBottom,
  },
  created() {
    document.title = 'GwakLee'
    this.getMovies('upcoming')
    this.$axios({
      method: 'get',
      url: `${SERVER_URL}/accounts/userlist/`,
    })
    .then(res => {
      // console.log(res.data)
      this.saveTopUsers(res.data)
      // this.topUsers = res.data
    })
    .catch(err => {
      console.log(err)
    })
  },
  methods: {
    ...mapActions(['getMovies', 'saveTopUsers'])
  }
}
</script>

<style scoped>
.content1 {
  height: 15rem;
  border-radius: 10px;
}
.content2 {
  /* background-color: #D6D6D6; */
  /* border: 1px solid; */
  border-radius: 10px;
  margin: auto;
}

</style>