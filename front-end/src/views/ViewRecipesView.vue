<template>
  <div>
    <h1>View Recipes Page</h1>
    <AppRecipeDisplayCard
      v-for="recipe in recipes"
      :key="recipe._id"
      :recipe="recipe"
    ></AppRecipeDisplayCard>
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

        this.recipes.forEach((recipe) => {
          console.log(recipe._id)
        })
      })
      .catch((error) => {
        console.error(error)
      })
  }
}
</script>

<style scoped></style>
