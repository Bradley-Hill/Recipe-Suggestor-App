<template>
  <div>
    <input v-model="ingredient1" placeholder="Enter an ingredient" />
    <input v-model="ingredient2" placeholder="Enter an ingredient" />
    <input v-model="ingredient3" placeholder="Enter an ingredient" />
    <input v-model="ingredient4" placeholder="Enter an ingredient" />
    <button @click="searchRecipes">Search</button>
    <ul>
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
      const ingredients = [this.ingredient1, this.ingredient2, this.ingredient3, this.ingredient4]
      const response = await axios.post('/search', { ingredients })
      this.recipes = response.data
    }
  }
}
</script>

<style scoped>
div {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: auto;
}
</style>
