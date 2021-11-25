<template>
  <b-navbar id="nav" toggleable="md" type="light" variant="faded">
    <!-- 로고 -->
    <b-navbar-brand>
      <router-link :to="{name: 'MovieHome'}" title="main page">
        <img @click="userpoint('logo')" src="@/assets/banana.gif" alt="Logo" height="50">
      </router-link>
    </b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <!-- 햄버거 -->
    <b-collapse class="justify-content-between" id="nav-collapse" is-nav>
      <!-- left -->
      <div></div>
      <!-- center: 언제든 보일 검색창 -->
      <b-navbar-nav><SearchBar/></b-navbar-nav>
      <!-- right: etc -->
      <b-navbar-nav class="me-1">
        <!-- 로그인 하면 보일거 -->
        <b-nav-dropdown v-if="userInfo.username" right>
          <template #button-content>
            <b-icon icon="person-circle" aria-hidden="true"></b-icon>
          </template>
          <b-dropdown-item disabled>{{ userInfo.point }} Point</b-dropdown-item>
          <b-dropdown-divider></b-dropdown-divider>
          <b-dropdown-item @click="goProfile(userInfo.username)">Profile</b-dropdown-item>
          <b-dropdown-item @click.native="logout">LogOut</b-dropdown-item>
        </b-nav-dropdown>
        <b-nav-item v-if="userInfo.username">
          <router-link :to="{name: 'Community'}" class="text-dark text-decoration-none">Community</router-link>
        </b-nav-item>
        <!-- User dropbox -->
        <!-- 로그인 안하면 보일거 -->
        <b-nav-item v-if="!userInfo.username">
          <router-link :to="{name: 'Signup'}" class="text-dark text-decoration-none">Signup</router-link>
        </b-nav-item>
        <b-nav-item v-if="!userInfo.username">
          <router-link :to="{name: 'Login'}" class="text-dark text-decoration-none">Login</router-link>
        </b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
import SearchBar from '@/components/SearchBar'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Navbar',
  components: {
    SearchBar,
  },
  methods: {
    ...mapActions(['goProfile', 'userpoint']),
    logout() {
      localStorage.removeItem('jwt')
      this.$store.dispatch('logout')
      this.$router.push({name: 'MovieHome'})
      .catch(() => {
        this.$router.go(0)
      })
    }
  },
  computed: {
    ...mapState(['userInfo'])
  }
}
</script>

<style scoped>
#nav a {
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  font-weight: bold;
  /* color: #42b983; */
}
</style>