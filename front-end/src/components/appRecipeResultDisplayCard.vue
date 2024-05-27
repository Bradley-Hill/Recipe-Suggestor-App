<template>
  <div class="card-container" :class="{ flip: isFlipped }" @click="isFlipped = !isFlipped">
    <div class="front-card">
      <h2>{{ typedRecipe.name }}</h2>
      <img :src="typedRecipe.image_url" alt="Recipe Image" />
      <!--  Add more structure for teh recipe info here -->
    </div>
    <div class="back-card">
      <h2>{{ typedRecipe.name }}</h2>
      <h3>Time to cook : {{ typedRecipe.total_time }} minutes</h3>
      <ul>
        <li v-for="(ingredient, index) in typedRecipe.ingredients" :key="index">
          {{ ingredient }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, computed, ref } from 'vue'
import type { Recipe } from '@/interfaces/Recipe'

export default defineComponent({
  name: 'appRecipeResultDisplayCard',
  components: {},
  props: {
    recipe: {
      type: Object as () => Recipe,
      required: true
    }
  },
  setup(props) {
    const typedRecipe = computed(() => props.recipe as Recipe)
    const isFlipped = ref(false)
    return { typedRecipe, isFlipped }
  }
})
</script>

<style scoped>
.card-container {
  position: relative;
  width: 19rem;
  height: 350px;
  perspective: 1000px;
  backface-visibility: hidden;
}
.front-card,
.back-card {
  position: absolute;
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  padding: 1.25rem;
  border: 1px solid #ccc;
  box-shadow: 2px 2px 6px 0 rgba(0, 0, 0, 0.2);
  margin: 1.25rem;
  border-radius: 0.5rem;
  backface-visibility: hidden;
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}

.back-card {
  transform: rotateY(-180deg);
  position: absolute;
  width: 100%;
  height: 100%;
}
.card-container.flip .front-card {
  transform: rotateY(180deg);
}
.card-container.flip .back-card {
  transform: rotateY(0);
}

.front-card:hover {
  transform: scale(1.05);
  box-shadow: 4px 4px 10px 0 rgba(0, 0, 0, 0.2);
}

.front-card h2 {
  margin-bottom: 10px;
  text-align: center;
}

.front-card img {
  width: 100%;
  height: 100%;
  border-radius: 0.5rem;
  object-fit: cover;
}
</style>
