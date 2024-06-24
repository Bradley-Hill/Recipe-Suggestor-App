<template>
  <div>
    <form @submit.prevent="addRecipe">
      <label for="url">Recipe URL:</label>
      <input id="url" v-model="url" type="text" required />
      <button type="submit">Add Recipe</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import {http} from "@/router/index"

export default {
  data() {
    return {
      url: ''
    }
  },
  created(){
    this.checkExpiredToken()
  },
  methods: {
    async checkExpiredToken(){
      try{
        await http.get("/add")
        console.log("Token is not Expired")
      } catch (error){
        console.error("Error verifying token expiration: ", error);
      }
    },
    async addRecipe() {
      console.log('addRecipe method called')
      try {
        const response = await axios.post(`${import.meta.env.VITE_VUE_APP_BASE_API_URL}/add`, {
          url: this.url
        })
        console.log(response.data)
        this.url = ''
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>
