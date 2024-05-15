<template>
  <div class="recipe-card">
    <h2>{{ typedRecipe.name }}</h2>
    <img :src="typedRecipe.image_url" alt="Recipe Image" />
    <!--  Add more structure for teh recipe info here -->
    <DeleteRecipeButton
      :recipeId="typedRecipe._id"
      @recipeDeleted="$emit('recipeDeleted', $event)"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from 'vue'
import DeleteRecipeButton from './appDeleteRecipeButton.vue'

interface Recipe {
  name: string
  image_url: string
  _id: string
}

export default defineComponent({
  name: 'appRecipeDisplayCard',
  components: { DeleteRecipeButton },
  props: {
    recipe: {
      type: Object as () => Recipe,
      required: true
    }
  },
  setup(props) {
    const typedRecipe = computed(() => props.recipe as Recipe)
    return { typedRecipe }
  }
})
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
