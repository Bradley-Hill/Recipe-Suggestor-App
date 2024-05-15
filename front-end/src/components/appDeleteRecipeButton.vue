<template>
  <button type="button" class="deleteBtn" v-on:click="deleteRecipe">Delete</button>
</template>

<script>
import axios from 'axios'
export default {
  name: 'DeleteRecipeButton',
  props: {
    recipeId: String
  },
  methods: {
    deleteRecipe() {
      axios({
        method: 'delete',
        url: 'http://localhost:5000/delete_recipe',
        data: { _id: this.recipeId }
      })
        .then((response) => {
          console.log(response.data)
          this.$emit('recipeDeleted', this.recipeId)
        })
        .catch((error) => {
          console.error(error)
        })
    }
  }
}
</script>

<style scoped></style>
