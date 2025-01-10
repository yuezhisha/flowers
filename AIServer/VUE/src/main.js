import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios'
// 将 CSRF Token 设置到 Axios 请求头
axios.defaults.xsrfCookieName = 'csrftoken';  // Django 默认的 CSRF Cookie 名称
axios.defaults.xsrfHeaderName = 'X-CSRFToken';  // Django 默认的 CSRF Header 名称
axios.defaults.withCredentials = true;

createApp(App).use(router).mount('#app');
