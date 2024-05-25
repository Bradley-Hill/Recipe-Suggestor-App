<template>
  <div>
    <form @submit.prevent="addRecipe">
      <label for="url">Recipe URL:</label>
      <input id="url" v-model="url" type="text" required />
      <button type="submit">Add Recipe</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      url: ''
    }
  },
  methods: {
    async addRecipe() {
      console.log('addRecipe method called')
      try {
        const response = await axios.post(`${import.meta.env.VITE_VUE_APP_BASE_API_URL}/add`, {
          url: this.url
        })
        console.log(response.data)
        this.url = ''
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>
