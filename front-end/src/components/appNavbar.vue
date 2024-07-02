<template>
  <header class="navbar">
    <h1>BBC Good Food - Recipe Suggestions</h1>

    <router-link to="/">Home</router-link>
    <router-link to="/Login">Login</router-link>
    <router-link to="/SignUp">Sign Up</router-link>
    <router-link to="/ViewRecipes">View Recipes</router-link>
  </header>
</template>

<script>
export default {
  name: 'appNavbar'
}
</script>

<style scoped>
.navbar {
  display: flex;
  align-items: center;
  justify-content: space-around;
  font-family: 'Times New Roman', Times, serif;
  font-size: 1.5rem;
  background: rgb(85, 97, 110);
}

.router-link-active {
  color: black;
  font-weight: bold;
}
.router-link {
  text-decoration: none;
  color: antiquewhite;
}
</style>
