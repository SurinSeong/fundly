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
  width: 100%;
  height: 100%;
  display: flex;
}

.total-container {
  width: 100%;
  max-width: 1200px;
  height: 100%;
  display: flex;
  margin: 0 auto;
}

main {
  height: 100%;
  width: 100%;
  flex: 3;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 3rem 0 3rem;
}
.side-bar {
  flex: 1;
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
    width: 100%;
    height: 100%;
    border: none;
  }

  main {
    margin: 3rem 0 0 0;
  }
}
</style>
