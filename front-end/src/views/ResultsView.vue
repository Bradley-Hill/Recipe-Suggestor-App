<template>
  <div>
    <h1>Results Page</h1>
  </div>
  <div class="searchForm">
    <AppIngredientForm></AppIngredientForm>
  </div>
  <div class="recipeDisplayContainer">
    <appRecipeDisplayCard></appRecipeDisplayCard>
  </div>
</template>

<script>
import AppIngredientForm from '@/components/appIngredientForm.vue'
import appRecipeDisplayCard from '@/components/appRecipeDisplayCard.vue'
export default {
  name: 'ResultsView',
  components: { AppIngredientForm, appRecipeDisplayCard },
  data() {
    return { recipes: [] }
  }
}
</script>

<style scoped></style>
