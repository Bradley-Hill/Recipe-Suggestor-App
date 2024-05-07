<template>
  <div class="recipe-card">
    <h2>{{ recipe.name }}</h2>
    <img :src="recipe.image_url" alt="Recipe Image" />
    <!--  Add more structure for teh recipe info here -->
    <button type="button" class="deleteBtn" v-on:click="deleteRecipe">Delete</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'appRecipeDisplayCard',
  props: {
    recipe: Object
  },
  methods: {
    deleteRecipe() {
      axios({
        method: 'delete',
        url: 'http://localhost:5000/delete_recipe',
        data: { _id: this.recipe._id }
      })
        .then((response) => {
          console.log(response.data)
          this.$emit('recipeDeleted', this.recipe._id)
        })
        .catch((error) => {
          console.error(error)
        })
    }
  }
}
</script>

<style scoped>
.recipe-card {
  display: flex;
  flex-direction: column;
  width: 19rem;
  padding: 1.25rem;
  border: 1px solid #ccc;
  box-shadow: 2px 2px 6px 0 rgba(0, 0, 0, 0.2);
  margin: 1.25rem;
  border-radius: 0.5rem;
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}

.recipe-card:hover {
  transform: scale(1.05);
  box-shadow: 4px 4px 10px 0 rgba(0, 0, 0, 0.2);
}

.recipe-card h2 {
  margin-bottom: 10px;
  text-align: center;
}

.recipe-card img {
  width: 100%;
  height: auto;
  border-radius: 0.5rem;
}
</style>
