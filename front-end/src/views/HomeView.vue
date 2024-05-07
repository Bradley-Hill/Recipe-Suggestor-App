<template>
  <div class="homepage">
    <h1>Welcome to Home Page</h1>

    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit.<br />
      Earum explicabo quasi ut incidunt assumenda consequuntur esse.<br />
      Minus qui ea unde, sapiente quo voluptate atque esse alias quos nisi quasi quas.<br />
    </p>

    <!-- Your code goes here -->
  </div>
</template>

<script>
export default {
  name: 'HomeView'
  // Your component logic goes here
}
</script>

<style scoped>
p {
  font-size: 2rem;
  color: black;
}
.homepage {
  background-image: url('/homeBackground.jpg');
  background-size: cover;
  background-position: center;
}
/* Your styles go here */
</style>
