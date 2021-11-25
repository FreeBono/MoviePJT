<template>
  <div id="app" class="container">
    <Navbar/>
    <router-view/>
    <footer class="sticky-bottom">
      <span class="me-3">email: aaa@gmail.com / bbb@naver.com</span>
      <span>used: TMDB API / django / vue.js</span>
    </footer>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'

export default {
  name: 'App',
  components: {
    Navbar,
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#cursor-hover {
  cursor: pointer;
}
body {
  height: 100%;
}

</style>
