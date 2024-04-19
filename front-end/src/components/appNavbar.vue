<template>
  <header class="navbar">
    <h1>I will be a navbar</h1>

    <router-link to="/">Home</router-link>
    <router-link to="/Login">Login</router-link>
    <router-link to="/SignUp">Sign Up</router-link>
    <router-link to="/Results">Results</router-link>
    <router-link to="/AddRecipe">Add Recipe</router-link>
    <router-link to="/ViewRecipes">View Recipes</router-link>
  </header>
</template>

<script>
export default {
  name: 'appNavbar'
}
</script>

<style scoped></style>
