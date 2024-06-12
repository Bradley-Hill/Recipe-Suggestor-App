<template>
    <form @submit.prevent="handleSubmit">
        <fieldset>
        <label for="Username">Username : 
            <input type="text" id="Username" v-model="username" required>
        </label>
        <label for="Password"> Password : 
            <input type="password" id="Password" v-model="password" required>
        </label>
        <button type="submit">Login</button>
    </fieldset>
    </form>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';

export default defineComponent({
    data() {
        return {
            username: '',
            password: '',
        }
    },
    methods: {
        async handleSubmit(){
            try {
                const response = await axios.post(`${import.meta.env.VITE_VUE_APP_BASE_API_URL}/login`, {
                    username: this.username,
                    password: this.password
                });
                if(response.data.success){
                    window.localStorage.setItem("token", response.data.token);
                // Update the page to confirm the user is logged in
                } else {
                    console.error("Error: ", response.data.error)
                }
            } catch (error) {
                console.error('Failed to login',error);
            }
        }
    }
})
</script>

<style scoped>
fieldset {
  border: 1px solid #ddd;
  padding: 20px;
  border-radius: 5px;
  margin-bottom: 20px;
}

form {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  max-width: 500px; /* Limit the width of the form */
  margin: 0 auto; /* Center the form */
}

input[type='text'],
input[type='password'] {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

button {
  padding: 10px 20px;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}
</style>