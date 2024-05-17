<template>
  <div>
    <form>
      <input v-model="ingredient1" placeholder="Enter an ingredient" />
      <input v-model="ingredient2" placeholder="Enter an ingredient" />
      <input v-model="ingredient3" placeholder="Enter an ingredient" />
      <input v-model="ingredient4" placeholder="Enter an ingredient" />
      <button type="button" @click="searchRecipes">Search</button>
    </form>
    <ul>
      <li v-if="typeof recipes === 'string'">{{ recipes }}</li>
      <li v-for="recipe in recipes" :key="recipe._id">{{ recipe.name }}</li>
    </ul>
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
      ingredient4: '',
      recipes: []
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
      const response = await axios.post('http://localhost:5000/search', {
        ingredients
      })
      if (response.data.length === 0) {
        this.recipes = 'No Matching Recipes Found'
      } else {
        this.recipes = response.data
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
