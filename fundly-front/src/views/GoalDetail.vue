<template>
  <div class="goaldetail-container">
    <Card class="card" v-for="deposit in goal.deposit" :key="deposit.name">
      <template #title>{{ deposit.title }}</template>
      <template #content>
        {{ year }} - {{ month }}
        <ProgressBar
          :value="(deposit.currentAmount / deposit.predictAmount) * 100"
        />
        {{ deposit.predictAmount }} 만 원
      </template>
    </Card>
  </div>
</template>

<script setup>
import { ref } from "vue";
import Card from "primevue/card";
import ProgressBar from "primevue/progressbar";

const date = new Date();
const year = date.getFullYear();
const month = date.getMonth();
const deposit = ref([
  {
    id: 1,
    title: "싸피 청년 우대 예금",
    predictAmount: 500,
    currentAmount: 200,
    startDate: "2025-05-24"
  },
  {
    id: 2,
    title: "싸피 청년 우대 예금",
    predictAmount: 500,
    currentAmount: 200,
    startDate: "2025-05-24"
  },
  {
    id: 3,

    title: "싸피 청년 우대 예금",
    predictAmount: 500,
    currentAmount: 200,
    startDate: "2025-05-24"
  }
]);
const saving = ref([
  {
    title: "싸피 청년 우대 적금",
    predictAmount: 1500,
    currentAmount: 300,
    startDate: "2025-05-24"
  }
]);
const goal = ref({
  title: "유학 자금 마련하기",
  targetAmount: 2000,
  currentAmount: 500,
  saving: 200,
  deposit: 300,
  saving: saving,
  deposit: deposit
});
</script>

<style scopped>
.goaldetail-container {
  width: 100%;
  display: flex;
  justify-content: space-evenly;
}

.card {
  width: 30%;
}
</style>
