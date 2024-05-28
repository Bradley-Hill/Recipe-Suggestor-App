<template>
  <div
    class="card-container"
    :class="{ flip: isFlipped, expanded: isExpanded }"
    @click="isFlipped = !isFlipped"
  >
    <div class="front-card">
      <h2>{{ typedRecipe.name }}</h2>
      <img :src="typedRecipe.image_url" alt="Recipe Image" />
      <h3>Time to cook : {{ typedRecipe.total_time }} minutes.</h3>
      <!--  Add more structure for teh recipe info here -->
      <div v-if="isExpanded" class="expanded-content">
        <div class="ingredients">
          <h3>Ingredients</h3>
          <ul>
            <li v-for="(ingredients, index) in typedRecipe.ingredients" :key="index">
              {{ ingredients }}
            </li>
          </ul>
        </div>
        <div class="instructions">
          <ul>
            <li v-for="(instructions, index) in typedRecipe.instructions" :key="index">
              {{ instructions }}
            </li>
          </ul>
        </div>
      </div>

      <button @click.stop="isExpanded = !isExpanded">
        {{ isExpanded ? 'Show less' : 'Show more' }}
      </button>
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
    const isExpanded = ref(false)
    return { typedRecipe, isFlipped, isExpanded }
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
  transition: transform 0.3s ease-in-out;
}

.card-container.expanded {
  transform: scale(1.2);
  z-index: 1000;
  position: fixed;
  top: 10%;
  left: 10%;
  width: 70%;
  height: 70vh;
  z-index: 1000;
  border-radius: 0;
  margin: 0;
  padding: 0;
  overflow: auto;
  background: whitesmoke;
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
.back-card ul {
  max-height: 300px;
  overflow-y: hidden;
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
  max-height: 200px;
  border-radius: 0.5rem;
  object-fit: cover;
}

.expanded-content {
  overflow-y: auto;
  display: flex;
}

.expanded-content .ingredients,
.expanded-content .instructions {
  flex: 1;
  overflow: auto;
}
</style>
