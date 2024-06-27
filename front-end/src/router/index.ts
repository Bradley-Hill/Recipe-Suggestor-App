import { createRouter, createWebHistory } from 'vue-router'
import axios from 'axios';
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ResultsView from '@/views/ResultsView.vue'
import AddRecipeView from '@/views/AddRecipeView.vue'
import ViewRecipesView from '@/views/ViewRecipesView.vue'
import UserDashboard from "@/views/UserDashboard.vue"

const routes = [
  { path: '/', component: HomeView },
  { path: '/Login', component: LoginView },
  { path: '/SignUp', component: SignUpView },
  { path: '/Results', component: ResultsView, meta:{requiresAuth:true} },
  { path: '/AddRecipe', component: AddRecipeView, meta:{requiresAuth:true} },
  { path: '/ViewRecipes', component: ViewRecipesView },
  { path: '/UserDashboard', component: UserDashboard, meta: {requiresAuth:true}}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

const http = axios.create({
  baseURL: `${import.meta.env.VITE_VUE_APP_BASE_API_URL}`,
});

http.interceptors.response.use(response=>{
  return response;
}, error =>{
  if(error.response.status === 401){
    if(error.response.data.error === "Token has expired"){
      localStorage.removeItem("token")
      router.push("/Login")
    }
  }
  return Promise.reject(error)
})

router.beforeEach((to,from,next) => {
  if(to.matched.some(record => record.meta.requiresAuth)){
    const token = localStorage.getItem("token")
    if (!token){
      next("/Login")
    } else {
      next()
    }
  } else {
    next()
  }
})

export  {router,http}
