<template>
  <div>
    <form>
      <input v-model="ingredient1" placeholder="Enter an ingredient" />
      <input v-model="ingredient2" placeholder="Enter an ingredient" />
      <input v-model="ingredient3" placeholder="Enter an ingredient" />
      <input v-model="ingredient4" placeholder="Enter an ingredient" />
      <button class="inline-flex items-center justify-center gap-2 rounded-lg border border-blue-200 bg-blue-100 px-2 py-1 text-sm font-semibold leading-5 text-blue-800 hover:border-blue-300 hover:text-blue-900 hover:shadow-sm focus:ring focus:ring-blue-300/25 active:border-blue-200 active:shadow-none dark:border-blue-200 dark:bg-blue-200 dark:hover:border-blue-300 dark:hover:bg-blue-300 dark:focus:ring-blue-500/50 dark:active:border-blue-200 dark:active:bg-blue-200" type="button" @click="searchRecipes">Search</button>
    </form>
    <!-- <ul>
      <li v-if="typeof recipes === 'string'">{{ recipes }}</li>
      <li v-for="recipe in recipes" :key="recipe._id">{{ recipe.name }}</li>
    </ul> -->
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      ingredient1: '',
      ingredient2: '',
      ingredient3: '',
      ingredient4: ''
      // recipes: []
    }
  },
  methods: {
    async searchRecipes() {
      const ingredients = [
        this.ingredient1,
        this.ingredient2,
        this.ingredient3,
        this.ingredient4
      ].filter(Boolean)
      const response = await axios.post(`${import.meta.env.VITE_VUE_APP_BASE_API_URL}/search`, {
        ingredients
      })
      if (response.data.length === 0) {
        this.recipes = 'No Matching Recipes Found'
      } else {
        this.$emit('search-results', response.data)
      }
    }
  }
}
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  width: auto;
  height: 10rem;
}
</style>
