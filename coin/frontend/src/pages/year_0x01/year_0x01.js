import { createApp } from 'vue';
import Year0x01 from './Year_0x01.vue';

const year0x01 = createApp(Year0x01);
year0x01.config.globalProperties.window = window;
year0x01.mount('#app');
