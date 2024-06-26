import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'jquery/src/jquery.js'
import 'bootstrap/dist/js/bootstrap.min.js'
import 'remixicon/fonts/remixicon.css'
import '../src/custom_css/style.css'
import '../src/custom_js/script.js'

createApp(App).use(store).use(router).mount('#app')
