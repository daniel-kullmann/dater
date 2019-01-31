<template>
  <div class="select-appointment">
    <h1>Select appointment</h1>
    <v-calendar>
    </v-calendar>
  </div>
</template>

<script>
// @ is an alias to /src
import Vue from 'vue';
import VCalendar from 'v-calendar';
import 'v-calendar/lib/v-calendar.min.css';

Vue.use(VCalendar, {
  firstDayOfWeek: 2,  // Monday
});

export default {
  name: 'home',
  components: {
  },
  data() {
    return {
      attrs: [
        {
          key: 'today',
          highlight: {
            backgroundColor: '#ff8080',
          },
          // Just use a normal style
          contentStyle: {
            color: '#fafafa',
          },
          dates: new Date(2018, 0, 1)
        },
      ],
    };
  },
};
</script>

