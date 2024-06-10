<template>
  <div>
    <h1>Login Page</h1>
  </div>
  <div class="UserLoginFormContainer">
    <appUserLoginForm></appUserLoginForm>
  </div>
</template>

<script>
import appUserLoginForm from '@/components/appUserLoginForm.vue'
export default {
  name: 'LoginView',
  components: { appUserLoginForm 
},}
</script>

<style scoped></style>
