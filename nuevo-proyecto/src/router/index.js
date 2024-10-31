import { createRouter, createWebHistory } from 'vue-router'; 
import HomeView from '../views/HomeView.vue'; 
import ClassesView from '../views/ClassesView.vue'; 
import SignupView from '../views/SignupView.vue'; 
import ClassDetail from '../views/ClassDetail.vue';
import ContactView from '../views/ContactView.vue';
import AboutView from '../views/AboutView.vue';
import AddClassView from '../views/AddClassView.vue'; // Importa el nuevo componente
import PasswordCheck from '../views/PasswordCheck.vue'; // Importar el componente de verificación de contraseña

const routes = [
  { path: '/', name: 'home', component: HomeView },
  { path: '/classes', name: 'classes', component: ClassesView },
  { path: '/classes/:id', name: 'classDetail', component: ClassDetail },
  { path: '/signup', name: 'signup', component: SignupView },
  { path: '/contact', name: 'contact', component: ContactView },
  { path: '/about', name: 'about', component: AboutView },
  { path: '/add_class', name: 'add_class', component: AddClassView }, // Añadir la ruta para agregar clase
  { path: '/password_check', name: 'password_check', component: PasswordCheck } // Nueva ruta para la verificación
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
