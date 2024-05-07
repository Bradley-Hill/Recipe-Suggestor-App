<template>
  <div>
    <h1>Results Page</h1>
  </div>
  <div class="searchForm">
    <AppIngredientForm></AppIngredientForm>
  </div>
</template>

<script>
import AppIngredientForm from '@/components/appIngredientForm.vue'
export default {
  name: 'ResultsView',
  components: { AppIngredientForm }
}
</script>

<style scoped></style>
