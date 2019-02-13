<template>
<div class="login">
  <div>
    <label for="login_name">Username: </label>
    <input type="text" name="login_name"/>
  </div>
  <div>
    <label for="login_password">Password: </label>
    <input type="password" name="login_password"/>
  </div>
  <div>
    <button name="Login" v-on:click="login();">Login</button>
  </div>
</div>
</template>

<script>
export default {
    name: 'login',
    components: {
    },
    data: function() {
        return {
        };
    },
    methods: {
        login: function() {
            console.log('log in');
        }
    }
}
</script>
