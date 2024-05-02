<template>
  <div>
    <h1>Add Recipe Page</h1>
    <appAddingRecipeForm />
  </div>
</template>

<script>
import appAddingRecipeForm from '../components/appAddingRecipeForm.vue'
export default {
  name: 'AddRecipeView',
  components: {
    appAddingRecipeForm
  }
}
</script>

<style scoped></style>
