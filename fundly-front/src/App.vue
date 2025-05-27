<template>
  <div
    class="login"
    :class="{
      'total-container': route.name != 'login',
    }"
  >
    <ConfirmDialog></ConfirmDialog>

    <Sidebar class="side-bar" v-if="route.name != 'signup' && route.name != 'login'" />
    <IntroductionBar v-else-if="route.name != 'signup'" />
    <main><RouterView /></main>
  </div>
</template>

<script setup>
import Sidebar from '@/components/bar/Sidebar.vue'
import IntroductionBar from '@/components/bar/IntroductionBar.vue'
import { ConfirmDialog } from 'primevue'
import { useRoute } from 'vue-router'

const route = useRoute()
</script>

<style scoped>
.login {
  display: grid;
  grid-template-columns: 1fr; /* 루트 컨테이너 */
  width: 100%;
  height: 100%;
}

.total-container {
  display: grid;
  grid-template-columns: 2fr 4fr; /* 좌:사이드바(1/3), 우:메인(2/3) */
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  height: 100%;
}



main {
  padding: 2rem 3rem;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  height: 100%;
}

h1,
h2,
h3,
h4,
h5,
h6,
p {
  margin: 0;
}

@media (max-width: 768px) {
  .total-container {
    grid-template-columns: 1fr; /* 모바일에선 한 줄 */
  }

  main {
    padding: 1rem;
    margin-top: 2rem;
  }
}
</style>
