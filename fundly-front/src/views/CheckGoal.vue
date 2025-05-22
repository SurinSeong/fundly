<template>
  <div v-if="data" class="checkgoal-container">
    <RouterLink
      class="decorate  fix-size"
      :to="{ name: 'goaldetail', params: { goalid: goalId } }"
    >
      <Card>
        <template #title>
          {{ title }}
        </template>
        <template #content>
          <ProgressBar :value="value"></ProgressBar>
          {{ targetPeriod }}
        </template>
      </Card>
    </RouterLink>
    <RouterLink class="decorate  fix-size" :to="{ name: 'setgoal' }">
      <Card>
        <template #title>
          목표 추가하기
        </template>
        <template #content>
          <span class="pi pi-plus"></span>
        </template>
      </Card>
    </RouterLink>
  </div>
  <div v-else class="checkgoal-container">
    <h2 class="title">
      현재 설정되어 있는 목표가 없습니다.
      <br />
      함께 목표를 설정해볼까요?
    </h2>
    <RouterLink :to="{ name: 'setgoal' }"
      ><CustomButton :labelname="'목표 설정 하기'"
    /></RouterLink>
  </div>
</template>

<script setup>
import CustomButton from "@/components/button/CustomButton.vue";
import Card from "primevue/card";
import ProgressBar from "primevue/progressbar";
import { RouterLink } from "vue-router";
import { ref } from "vue";

const data = ref("epdlxj");
const title = ref("유학 자금 마련하기");
const goalId = ref(1);
const targetPeriod = ref("3년");
const currentAmount = ref(500);
const targetAmount = ref(2000);
const value = (currentAmount.value / targetAmount.value) * 100;
console.log(value);
</script>

<style scoped>
.checkgoal-container {
  text-align: center;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.title {
  margin-bottom: 3rem;
}

.decorate {
  text-decoration: none;
}

.fix-size {
  width: 30%;
  height: 30%;
}
</style>
