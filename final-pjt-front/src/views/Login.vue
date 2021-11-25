<template>
  <div class="box">
    <b-form-group class="input-1" label="Your Name:" label-for="input-2" align="left">
      <b-form-input id="input-1" v-model="credentials.username" placeholder="Enter name" required></b-form-input>
    </b-form-group>
    <b-form-group class="input-1" label="Password:" label-for="input-2" align="left">
      <b-form-input @keyup.enter="loginSubmit" id="input-2" v-model="credentials.password" placeholder="password" required type="password"></b-form-input>
    </b-form-group>
    <br>
    <br>
    <b-button type="submit" variant="primary" @click="loginSubmit">Log In</b-button>&nbsp;&nbsp;
  </div>
</template>


<script>
import { mapActions, mapGetters } from 'vuex'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data() {
    return {
      credentials: {
        username: null,
        password: null,
      },
      point: 0,
    }
  },
  methods: {
    ...mapActions(['login', 'saveToken', 'updateUserInfo']),
    loginSubmit() {
      // console.log(this.credentials)
      // token 발급 요청 보내기
      this.$axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/api-token-auth/`,
        data: this.credentials,
      })
      .then(res => {
        // console.log(res.data)          // {token: '#'} 이것만 있음
        // 받은 token 잘 저장하고
        this.saveToken(res.data.token)
        localStorage.setItem('jwt', res.data.token)
      })
      // username주고 user정보 받아와서 userInfo 저장하기
      .then(() => {
        this.$axios({
          method: 'get',
          url: `${SERVER_URL}/accounts/profile/${this.credentials.username}`,
          headers: this.setToken,
        })
        .then(res => {
          const { id, point, username } = res.data[0]
          const userInfo = {id: id, point: point, username: username}
          this.updateUserInfo(userInfo)
        })
        .catch(err => {
          console.log(err)
        })
      })
      .then(() => {
        // this.$emit('login')
        alert('Welcome🚀')
        this.$router.push({name: 'MovieHome'})
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  computed: {
    ...mapGetters(['setToken'])
  },
  created() {
    document.title = 'GwakLee-Login'
  }
}
</script>

<style scoped>

</style>