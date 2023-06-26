import { createApp } from 'vue';
import FourOhFour from './404App.vue';

const coin404App = createApp(FourOhFour);
coin404App.config.globalProperties.window = window;
coin404App.mount('#app');
