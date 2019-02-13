<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/select/12345">Select</router-link> |
      <router-link v-if="logged_in == null" to="/login">Login</router-link>
      <router-link v-else to="/logout">Logout</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      logged_in: null
    };
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
