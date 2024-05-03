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
      try {
        const response = await axios.post(
          'http://localhost:5000/add',
          { url: this.url },
          { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }
        )
        console.log(response.data)
        this.url = ''
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>
