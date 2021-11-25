<template>
  <span class="search-bar">
    <!-- Searchbar & button -->
    <input @keyup.enter="sendInputText" @input="submitAutoComplete" v-model="inputText" size="40" type="text" placeholder="Please enter a word">&nbsp;
    <b-button @click="clickBtn" variant="outline-dark" size="sm" class="mb-1">Search</b-button>
    <!-- autocomplete -->
    <div class="candidate autocomplete">
      <div @click="sendInputText" style="cursor: pointer" v-for="(res, idx) in result" :key="idx">
        {{ res.title }}
      </div>
    </div>
  </span>
</template>

<script>
import { mapState, mapActions } from 'vuex'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'SearchBar',
  data() {
    return {
      inputText: '',
      what: 'title',
      result: [],
      sendText: '',
    }
  },
  methods: {
    ...mapActions(['saveSearchList']),
    sendInputText(event) {
      if (Boolean(event.key) == true) {             // Enter
        // console.log(this.inputText)
        this.sendText = this.inputText
      } else {                                      // click
        this.sendText = event.target.innerText
        // console.log(sendText)
      }
      this.axiosMovies()
    },
    clickBtn() {
      this.sendText = this.inputText
      this.axiosMovies()
    },
    axiosMovies() {
      this.$axios({
        method: 'get',
        url: `${SERVER_URL}/movies/search/${this.what}/${this.sendText}/`,
      })
      // 잘 받아오면 store의 searchList에 저장하고 SearchList로 페이지 넘기기
      .then(res => {
        // console.log(res.data)
        this.saveSearchList(res.data)
        this.$router.push({name: 'SearchList', params: {searchText: this.sendText}})
        this.$router.go(0)
      })
      .catch(err => {
        console.log(err)
      })
    },
    submitAutoComplete(event) {
      this.inputText = event.target.value
      const autocomplete = document.querySelector('.autocomplete')
      if (this.inputText) {
        autocomplete.classList.remove('candidate')
        this.result = this.allMovies.filter(movie => {
          const title = movie.title
          return title.match(this.inputText)
        })
      } else {
        autocomplete.classList.add('candidate')
      }
    }
  },
  computed: {
    ...mapState(['allMovies']),
  }
}
</script>

<style scoped>
.candidate {
  display: none;
}
</style>