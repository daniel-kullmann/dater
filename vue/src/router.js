import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import SelectAppointment from './views/SelectAppointment.vue'
import Login from './views/Login.vue'
import Logout from './views/Logout.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/select/:id',
      name: 'select',
      component: SelectAppointment
    },
    {
      path: '/login/',
      name: 'login',
      component: Login
    },
    {
      path: '/logout/',
      name: 'logout',
      component: Logout
    }
  ]
})
