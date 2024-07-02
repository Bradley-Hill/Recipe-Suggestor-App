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
    <p v-if="loginMessage">{{ loginMessage }}</p>
    </form>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

export default defineComponent({
    data() {
        return {
            username: '',
            password: '',
            loginMessage: "",
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
                this.loginMessage = "Login Successful! Redirecting..."
                const router = useRouter()
                setTimeout(()=>{
                    this.$router.push("/UserDashboard")
                },2000)
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

p{
    color: #4CAF50;
    font-size: 1.2rem;
    font-weight: bold;
    text-align: center;
    padding: 1rem;
    border: 1px solid #4CAF50;
    border-radius: 5px;
    margin-bottom: 1.2rem;
    background-color: #e8f5e9;

}
</style>