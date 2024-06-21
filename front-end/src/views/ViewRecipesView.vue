<template>
  <div>
    <h1>View Recipes Page</h1>
    <div class="DisplayCard-container" v-if="!loading">
      <AppRecipeDisplayCard
        v-for="recipe in recipes"
        :key="recipe._id"
        :recipe="recipe"
        @recipeDeleted="removeRecipe"
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
      recipes: [],
      loading: true
    }
  },
  methods: {
    removeRecipe(recipeId) {
      this.recipes = this.recipes.filter((recipe) => recipe._id !== recipeId)
    }
  },
  beforeRouteEnter(to,from,next){
    axios.get(`${import.meta.env.VITE_VUE_APP_BASE_API_URL}/view_all`).then((response)=>{
      next(componentInstance => {
        componentInstance.recipes = response.data;
        componentInstance.loading = false;
      });
    }).catch((error)=>{
      console.error(error);
      next(componentInstance=>componentInstance.loading = false)
    })
  },
}
</script>

<style scoped>
.DisplayCard-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(19rem, 1fr));
  grid-gap: 1rem;
}
</style>
