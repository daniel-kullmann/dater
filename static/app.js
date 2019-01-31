Vue.options.delimiters = ['${', '}'];
var app = new Vue({
    el: '#app',
    data: {
        title: 'Whatever',
        mode: 'single',
        selectedDate: null,
    }
});
