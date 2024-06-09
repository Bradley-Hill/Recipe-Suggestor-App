<template>
    <form @submmit.prevent="handleSubmit">
        <label for="Username">Username : 
            <input type="text" id="Username" v-model="username" required>
        </label>
        <label for="Password"> Password : 
            <input type="password" id="Password" v-model="password" required>
        </label>
        <button type="submit">Login</button>
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
                // Update the page to confirm the user is logged in
            } catch (error) {
                console.error('Failed to login',error);
            }
        }
    }
})
</script>