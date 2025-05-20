import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { definePreset } from '@primeuix/themes'
import Lara from '@primeuix/themes/lara'

import PrimeVue from 'primevue/config'
import App from './App.vue'
import router from './router'
import Button from 'primevue/button'

const MyPreset = definePreset(Lara, {
  semantic: {
    primary: {
      50: '{slate.50}',
      100: '{slate.100}',
      200: '{slate.200}',
      300: '{slate.300}',
      400: '{slate.400}',
      500: '{slate.500}',
      600: '{slate.600}',
      700: '{slate.700}',
      800: '{slate.800}',
      900: '{slate.900}',
      950: '{slate.950}',
    },
  },
  components: {
    button: {
      root: {
        primary: {
          background: '{slate.900}',
          color: 'white',
          border: '{slate.900}',
          hoverBg: '{slate.800}',
          focusShadow: '0 0 0 2px #ffffff, 0 0 0 4px {slate.700}',
        },
        label: {
          fontWeight: 400,
        },
      },
      text: {
        primary: {
          color: '{slate.900}',
          fontWeight: 100,

          hoverBg: '{slate.100}',
          focusShadow: '0 0 0 2px #ffffff, 0 0 0 4px {slate.700}',
        },
      },
      outlined: {
        primary: {
          fontWeight: 100,
          color: '{slate.900}',
          border: '{slate.500}',
          hoverBg: '{slate.100}',
          focusShadow: '0 0 0 2px #ffffff, 0 0 0 4px {slate.700}',
        },
      },
    },
  },
})

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(PrimeVue, {
  theme: {
    preset: MyPreset,
  },
})

app.component('Button', Button)
app.mount('#app')
