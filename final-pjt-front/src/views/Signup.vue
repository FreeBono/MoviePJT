<template>
  <div class="box">
    <b-form v-if="show">
      <b-form-group class="input-1" label="Your Name" label-for="input-2" align="left">
        <b-form-input v-model="credentials.username" placeholder="Enter name" required></b-form-input>
      </b-form-group>
      <b-form-group class="input-1" label="Password:" label-for="input-2" align="left">
        <b-form-input v-model="credentials.password" placeholder="password" required type="password"></b-form-input>
      </b-form-group>
      <b-form-group class="input-1" label="Password Confirmation:" label-for="input-2" align="left" >
        <b-form-input v-model="credentials.passwordConfirmation" placeholder="repeat your password" required @keyup.enter="signup" type="password"></b-form-input>
      </b-form-group>
      <br>
      <br>
      <b-button variant="primary" @click="signup">Submit</b-button>&nbsp;&nbsp;
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
  data() {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      },
      show: true
    }
  },
  methods: {
    signup() {
      // DB에 저장해 달라는 요청
      this.$axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/signup/`,
        data: this.credentials
      })
      // 응답이 잘 오면 Login 페이지로 push
      .then(() => {
        alert('가입을 환영합니다🎉')
        this.$router.push({name: 'Login'})
        // 회원가입시 자동로그인 emit으로 'login' 보내주고 원해는 페이지로 push하기
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  created() {
    document.title = 'GwakLee-회원가입'
  }
}
</script>

<style>
.box {
  left : 200px;
  border: 1px solid skyblue;
  margin-left: 25%;
  margin-top: 80px;
  padding: 20px;
  width: 50%;
  height: 500px;
  overflow: auto;
}

.input-1 {
  margin-top: 30px
}
</style>
