import { createRouter, createWebHistory } from 'vue-router';
import Login from '../components/login.vue';
import Register from '../components/Register.vue';
import FlowerRecognition from '../components/FlowerRecognition.vue';
import Camera from '../components/Camera.vue'; 

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login, meta: { animation: 'slide-left' } },
  { path: '/register', component: Register, meta: { animation: 'slide-right' } },
  { path: '/flower', component: FlowerRecognition , meta: { animation: 'slide-right'  }},
  { path: '/camera', component: Camera , meta: { animation: 'slide-left'  }}
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
