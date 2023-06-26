import { createApp } from 'vue';
import Root from './RootApp.vue';

const RootApp = createApp(Root);
RootApp.config.globalProperties.window = window;
RootApp.mount('#app');
