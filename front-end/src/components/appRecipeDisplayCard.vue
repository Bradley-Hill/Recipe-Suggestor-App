<template>
  <div class="recipe-card">
    <h2>{{ recipe.name }}</h2>
    <img :="recipe.image_url" alt="Recipe Image" />
    <!--  Add more structure for teh recipe info here -->
  </div>
</template>

<script>
export default {
  name: 'appRecipeDisplayCard',
  props: {
    recipe: Object
  }
}
</script>

<style scoped>
.recipe-card {
  width: 19rem;
  padding: 1.25rem;
  border: 1px solid #ccc;
  box-shadow: 2px 2px 6px 0 rgba(0, 0, 0, 0.2);
  margin: 1.25rem;
  border-radius: 0.5rem;
}

.recipe-card h2 {
  margin-bottom: 10px;
}

.recipe-card img {
  width: 100%;
  height: auto;
  border-radius: 0.5rem;
}
</style>
