<template>
  <div>
    <h1>Sign Up Page</h1>
  </div>
  <div class="createUserFormContainer">
    <appCreateUserForm></appCreateUserForm>
  </div>
</template>

<script>
import appCreateUserForm from '@/components/appCreateUserForm.vue'
export default {
  name: 'SignUpView',
  components: { appCreateUserForm }
}
</script>

<style scoped></style>
