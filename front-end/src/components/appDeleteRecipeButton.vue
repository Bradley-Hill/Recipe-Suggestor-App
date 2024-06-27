<template>
  <button class="inline-flex items-center justify-center gap-2 rounded-lg border border-blue-200 bg-blue-100 px-2 py-1 text-sm font-semibold leading-5 text-blue-800 hover:border-blue-300 hover:text-blue-900 hover:shadow-sm focus:ring focus:ring-blue-300/25 active:border-blue-200 active:shadow-none dark:border-blue-200 dark:bg-blue-200 dark:hover:border-blue-300 dark:hover:bg-blue-300 dark:focus:ring-blue-500/50 dark:active:border-blue-200 dark:active:bg-blue-200" type="button" v-on:click="deleteRecipe">Delete</button>
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

<style scoped>

</style>
