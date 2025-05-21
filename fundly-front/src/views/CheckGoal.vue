<template>
  <div v-if="data" class="checkgoal-container"></div>
  <div v-else class="checkgoal-container">
    <h2>
      현재 설정되어 있는 목표가 없습니다.
      <br />
      함께 목표를 설정해볼까요?
    </h2>
    <RouterLink :to="{ name: 'setgoal' }"
      ><Button class="btn" label="목표 설정하러 가기"></Button
    ></RouterLink>
  </div>
</template>

<script setup>
import { Button } from 'primevue'
import { RouterLink } from 'vue-router'
import { ref } from 'vue'
const data = ref()
</script>

<style scoped>
.checkgoal-container {
  text-align: center;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.btn {
  background-color: var(--p-indigo-500) !important;
  color: var(--p-primary-100) !important;
  border: none;
}
</style>
