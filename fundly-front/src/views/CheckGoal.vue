<template>
  <div v-if="data" class="checkgoal-container">
    <RouterCard
      class="card-item"
      :pagename="'goaldetail'"
      :params="{ goalid: goalId }"
      :cardtitle="title"
      :isprogressbar="true"
      :isdurationmonths="true"
      :value="value"
      :durationmonths="durationmonths"
    ></RouterCard>
    <RouterCard
      class="card-item"
      :pagename="'setgoal'"
      :cardtitle="'목표 추가하기'"
      :isicon="true"
      :isprogressbar="false"
      :iconclass="'pi pi-plus'"
      :isdurationmonths="false"
      :backgroundcolor="'backgroundcolor'"
    ></RouterCard>
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
import CustomButton from '@/components/button/CustomButton.vue'
import RouterCard from '@/components/card/RouterCard.vue'
import { Card } from 'primevue'
import { RouterLink } from 'vue-router'
import { ref } from 'vue'

const data = ref('epdlxj')
const title = ref('유학 자금 마련하기')
const goalId = ref(1)
const durationmonths = ref('12')

const currentAmount = ref(500)
const targetAmount = ref(2000)
const value = (currentAmount.value / targetAmount.value) * 100
</script>

<style scoped>
.checkgoal-container {
  text-align: center;
  width: 100%;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  align-items: center;
}

.title {
  margin-bottom: 3rem;
}

.card-item {
  flex: 0 0 calc(20% - 1rem);
  aspect-ratio: 3/2;
  box-sizing: border-box;
}
</style>
