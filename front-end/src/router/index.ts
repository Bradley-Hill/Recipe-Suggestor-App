import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ResultsView from '@/views/ResultsView.vue'
import AddRecipeView from '@/views/AddRecipeView.vue'
import ViewRecipesView from '@/views/ViewRecipesView.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/login', component: LoginView },
  { path: '/SignUp', component: SignUpView },
  { path: '/Results', component: ResultsView },
  { path: '/AddRecipe', component: AddRecipeView },
  { path: '/ViewRecipes', component: ViewRecipesView }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
