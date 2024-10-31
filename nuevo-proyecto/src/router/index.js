import { createRouter, createWebHistory } from 'vue-router'; 
import HomeView from '../views/HomeView.vue'; 
import ClassesView from '../views/ClassesView.vue'; 
import SignupView from '../views/SignupView.vue'; 
import ClassDetail from '../views/ClassDetail.vue';
import ContactView from '../views/ContactView.vue';
import AboutView from '../views/AboutView.vue';

const routes = [
  { path: '/', name: 'home', component: HomeView },
  { path: '/classes', name: 'classes', component: ClassesView },
  { path: '/classes/:id', name: 'classDetail', component: ClassDetail },
  { path: '/signup', name: 'signup', component: SignupView },
  { path: '/contact', name: 'contact', component: ContactView },
  { path: '/about', name: 'about', component: AboutView }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
