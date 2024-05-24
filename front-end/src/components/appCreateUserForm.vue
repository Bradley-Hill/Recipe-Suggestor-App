<template>
  <form @submit.prevent="createUser">
    <label for="username">Username:</label>
    <input id="username" v-model="username" type="text" required />
    <label for="email">Email:</label>
    <input id="email" v-model="email" type="text" required />
    <label for="password">Password:</label>
    <input id="password" v-model="password" type="password" required />
    <p v-if="passwordError">{{ passwordError }}</p>
    <label for="confirmPassword">Confirm password:</label>
    <input id="confirmPassword" v-model="confirmPassword" type="password" required />
    <p v-if="passwordError">{{ passwordError }}</p>
    <button type="submit">Create User</button>
  </form>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import axios from 'axios'

const username = ref('')
const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const passwordError = ref('')

watch(password, () => {
  passwordError.value = ''
})
watch(confirmPassword, () => {
  passwordError.value = ''
})

const createUser = async () => {
  if (password.value === confirmPassword.value) {
    try {
      const response = await axios.post(`${process.env.VUE_APP_API_BASE_URL}/createUser`, {
        username: username.value,
        email: email.value,
        password: password.value,
        confirmPassword: confirmPassword.value
      })
    } catch (error) {}
  } else {
    passwordError.value = 'Passwords do not match.'
  }
}
</script>

<style scoped></style>
