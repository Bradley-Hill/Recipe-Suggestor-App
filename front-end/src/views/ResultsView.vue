<template>
  <div>
    <h1>Results Page</h1>
  </div>
  <div class="searchForm">
    <AppIngredientForm @search-results="handleSearchResults"></AppIngredientForm>
  </div>
  <div class="recipeDisplayContainer">
    <p v-if="noResults">No recipes found</p>
    <appRecipeDisplayCard
      v-else
      v-for="recipe in recipes"
      :key="recipe._id"
      :recipe="recipe"
    ></appRecipeDisplayCard>
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from 'vue'
import AppIngredientForm from '@/components/appIngredientForm.vue'
import appRecipeDisplayCard from '@/components/appRecipeDisplayCard.vue'
import type { Recipe } from '@/interfaces/Recipe'
export default defineComponent({
  name: 'ResultsView',
  components: { AppIngredientForm, appRecipeDisplayCard },
  data(): { recipes: Recipe[]; noResults: boolean } {
    return { recipes: [], noResults: false }
  },
  computed: {
    hasResults() {
      return computed(() => this.recipes.length > 0)
    }
  },
  methods: {
    handleSearchResults(results: Recipe[]) {
      if (results.length === 0) {
        this.noResults = true
      } else {
        this.noResults = false
        this.recipes = results
      }
    }
  }
})
</script>

<style scoped>
.recipeDisplayContainer {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(19rem, 1fr));
  grid-gap: 1rem;
}
</style>
