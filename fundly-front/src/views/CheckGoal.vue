<template>
  <div v-if="data" class="checkgoal-container"></div>
  <div v-else class="checkgoal-container">
    <h2 class="title">
      현재 설정되어 있는 목표가 없습니다.
      <br />
      함께 목표를 설정해볼까요?
    </h2>
    <RouterLink :to="{ name: 'setgoal' }"
      ><CustomButton :labelname="'목표 설정 하기'"/></RouterLink>
  </div>
</template>

<script setup>
import CustomButton from '@/components/button/CustomButton.vue'
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

.title {
  margin-bottom: 3rem;
}
</style>
