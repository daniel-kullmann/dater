import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {
      name: null,
      group: null,
      logged_in: false,
    },
    filter: {
    },
    data: {
      avalaible_slots: [],
    }
  },
  mutations: {

  },
  actions: {

  }
})
