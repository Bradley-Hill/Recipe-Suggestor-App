<template>
  <div>
    <h1>View Recipes Page</h1>
    <div class="DisplayCard-container">
      <AppRecipeDisplayCard
        v-for="recipe in recipes"
        :key="recipe._id"
        :recipe="recipe"
      ></AppRecipeDisplayCard>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import AppRecipeDisplayCard from '@/components/appRecipeDisplayCard.vue'
export default {
  name: 'ViewRecipesView',
  components: {
    AppRecipeDisplayCard
  },
  data() {
    return {
      recipes: []
    }
  },
  created() {
    axios
      .get('http://localhost:5000/view_all')
      .then((response) => {
        this.recipes = response.data
      })
      .catch((error) => {
        console.error(error)
      })
  }
}
</script>

<style scoped>
.DisplayCard-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(19rem, 1fr));
  grid-gap: 1rem;
}
</style>
