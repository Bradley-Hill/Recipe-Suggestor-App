<template>
  <form @submit.prevent="createUser">
    <fieldset>
      <legend>User Information</legend>
      <label for="username">Username:</label>
      <input id="username" v-model="username" type="text" required aria-required="true" />
      <label for="email">Email:</label>
      <input
        id="email"
        ref="emailRef"
        v-model="email"
        type="email"
        required
        aria-required="true"
        aria-describedby="emailError"
      />
      <p v-if="emailError" aria-live="polite">{{ emailError }}</p>
      <label for="password">Password:</label>
      <input
        id="password"
        v-model="password"
        type="password"
        required
        aria-required="true"
        minlength="8"
        aria-describedby="passwordError"
      />
      <p v-if="passwordError" aria-live="polite">{{ passwordError }}</p>
      <label for="confirmPassword">Confirm password:</label>
      <input
        id="confirmPassword"
        v-model="confirmPassword"
        type="password"
        required
        aria-required="true"
        aria-describedby="passwordError"
      />
      <p v-if="passwordError" aria-live="polite">{{ passwordError }}</p>
    </fieldset>
    <button type="submit">Create User</button>
  </form>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import axios from 'axios'

const username = ref('')
const email = ref('')
const emailRef = ref<HTMLInputElement | null>(null)
const password = ref('')
const confirmPassword = ref('')
const passwordError = ref('')
const emailError = ref('')

const validateEmail = (email: string) => {
  const regex =
    /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
  return regex.test(String(email).toLowerCase())
}

const validatePasswordLength = (password: string) => {
  return password.length >= 8
}

watch(email, () => {
  if (!validateEmail(email.value)) {
    emailError.value = 'Invalid email format.'
    if (emailRef.value) {
      emailRef.value.focus()
    }
  } else {
    emailError.value = ''
  }
})

watch(password, () => {
  if (!validatePasswordLength(password.value)) {
    passwordError.value = 'Password must be at least 8 characters long'
  } else {
    passwordError.value = ''
  }
})

watch(confirmPassword, () => {
  if (confirmPassword.value !== password.value) {
    passwordError.value = 'Passwords do not match.'
  } else {
    passwordError.value = ''
  }
})

const createUser = async () => {
  try {
    const response = await axios.post(`http://localhost:5000/createUser`, {
      username: username.value,
      email: email.value,
      password: password.value,
      confirmPassword: confirmPassword.value
    })
  } catch (error) {
    console.error(error)
  }
}
</script>

<style scoped></style>
