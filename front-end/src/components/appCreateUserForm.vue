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
    <button :disabled="isLoading" type="submit">Create User</button>
  </form>
  <p v-if="successMessage" aria-live="polite">{{ successMessage }}</p>
</template>

<script setup lang="ts">
import type { ErrorResponse } from '@/interfaces/ErrorResponse';
import { ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { AxiosError } from 'axios';

const username = ref('')
const email = ref('')
const emailRef = ref<HTMLInputElement | null>(null)
const password = ref('')
const confirmPassword = ref('')
const passwordError = ref('')
const emailError = ref('')
const isLoading = ref(false)
const successMessage = ref('')
const router = useRouter()

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
    passwordError.value = 'Passwords must be at least 8 characters long'
  } else if (confirmPassword.value !== password.value) {
    passwordError.value = 'Passwords do not match'
  } else {
    passwordError.value = ''
  }
})

watch(confirmPassword, () => {
  if (!validatePasswordLength(password.value)) {
    passwordError.value = 'Passwords must be at least 8 characters in length.'
  } else if (confirmPassword.value !== password.value) {
    passwordError.value = 'Passwords do not match'
  } else {
    passwordError.value = ''
  }
})

const createUser = async () => {
  try {
    isLoading.value = true
    const response = await axios.post(`${import.meta.env.VITE_VUE_APP_BASE_API_URL}/createUser`, {
      username: username.value,
      email: email.value,
      password: password.value,
      confirmPassword: confirmPassword.value
    })

    if (response.status === 200 && response.data.message) {
      successMessage.value = response.data.message
      username.value = ''
      email.value = ''
      password.value = ''
      confirmPassword.value = ''
      // Redirect after delay
      setTimeout(() => {
        router.push('/Login')
      }, 2000)
    } else {
      successMessage.value = 'Failed to create new User'
    }
  } catch (error) {
  console.error(error);
  // Type assertion to inform TypeScript about the error structure
  const axiosError = error as AxiosError; // Assuming AxiosError is imported from 'axios'
  if (axiosError.response && axiosError.response.data) {
    const data: ErrorResponse=axiosError.response.data;
    successMessage.value = data.message || 'An unknown error occurred';
  } else {
    successMessage.value = 'An unknown error occurred';
  }
} finally {
  isLoading.value = false;
}
}
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
input[type='password'],
input[type='email'] {
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

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

button:hover:not(:disabled) {
  background-color: #0056b3;
}
</style>
