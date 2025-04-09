import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AddMovieFormView from '../views/AddMovieFormView.vue'
import MoviesView from '../views/MoviesView.vue' // Import MoviesView

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/movies/create',
      name: 'addMovie',
      component: AddMovieFormView
    },
    {
      path: '/movies', // Add this route
      name: 'movies',
      component: MoviesView
    }
  ]
})

export default router