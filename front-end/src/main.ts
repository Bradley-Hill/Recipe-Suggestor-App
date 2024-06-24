import { createApp } from 'vue'
import App from './App.vue'
import {router} from "../src/router/index"
import './assets/global.css'
import "../src/config/axiosConfig"

const app = createApp(App)

app.use(router)

app.mount('#app')
