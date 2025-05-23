<!-- GoalDetail.vue -->
<template>
  <div class="goaldetail-container">
    <div class="top">
      <h1>{{ goal.title }}</h1>
      <h3>시작이 반, 조금 더 힘내봐요!</h3>
    </div>
    <div class="bottom">
      <div class="goal-products">
        <Carousel :value="goalProducts" circular="">
          <template #item="slotProps">
            <RouterCard
              class="card-item"
              :pagename="'goalproductdetail'"
              :params="{
                goal: slotProps.data.goal,
                userid: slotProps.data.user,
                product: slotProps.data.finance_product ?? slotProps.data.additional_product,
              }"
              :isprogressbar="true"
              :isdurationmonths="true"
              :startdate="slotProps.data.start_date"
              :cardtitle="slotProps.data.title"
              :value="(slotProps.data.current_amount / slotProps.data.target_amount) * 100"
              :durationmonths="slotProps.data.duration_months"
            ></RouterCard>
          </template>
        </Carousel>
      </div>
      <div class="recommendation">
        <CustomCard
          :cardtitle="'금융 상품 살펴 보기'"
          :pagename="'productdetail'"
          :productlist="productList"
        >
        </CustomCard>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import RouterCard from '@/components/card/RouterCard.vue'
import CustomCard from '@/components/card/CustomCard.vue'
import Carousel from 'primevue/carousel'

const deposit = ref([
  {
    id: 1,
    goal: 1,
    user: 1,
    title: '싸피 청년 우대 예금',
    finance_product: 1,
    additional_product: null,
    option_product: 1,
    target_amount: 500,
    current_amount: 200,
    duration_months: 12,
    start_date: '2025-05-24',
  },
  {
    id: 2,
    goal: 1,
    user: 1,
    title: '예금 2',
    finance_product: null,
    additional_product: 2,
    option_product: 1,
    target_amount: 500,
    current_amount: 200,
    duration_months: 12,
    start_date: '2025-05-24',
  },
  {
    id: 3,
    goal: 1,
    user: 1,
    title: '예금 3',
    finance_product: 3,
    additional_product: null,
    option_product: 1,
    target_amount: 500,
    current_amount: 200,
    duration_months: 12,
    start_date: '2025-05-24',
  },
])
const saving = ref([
  {
    id: 4,
    goal: 1,
    user: 1,
    title: '적금 4',
    finance_product: 3,
    additional_product: null,
    option_product: 1,
    target_amount: 600,
    current_amount: 300,
    duration_months: 12,
    start_date: '2025-05-24',
  },
])
const goal = ref({
  title: '유학 자금 마련하기',
  target_amount: 2000,
  current_amount: 500,
  saving: 200,
  deposit: 300,
  saving: saving,
  deposit: deposit,
})

const goalProducts = goal.value.deposit.concat(goal.value.saving)

const productList = ref([
  {
    id: 1,
    goal: 1,
    user: 1,
    title: '추천 1',
    finance_product: 1,
    additional_product: null,
    option_product: 1,
    target_amount: 500,
    current_amount: 200,
    duration_months: 12,
    start_date: '2025-05-24',
  },
  {
    id: 2,
    goal: 1,
    user: 1,
    title: '추천 2',
    finance_product: null,
    additional_product: 2,
    option_product: 1,
    target_amount: 500,
    current_amount: 200,
    duration_months: 12,
    start_date: '2025-05-24',
  },
  {
    id: 3,
    goal: 1,
    user: 1,
    title: '추천 3',
    finance_product: 3,
    additional_product: null,
    option_product: 1,
    target_amount: 500,
    current_amount: 200,
    duration_months: 12,
    start_date: '2025-05-24',
  },
])
</script>

<style scopped>
.goaldetail-container {
  width: 60%;
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: space-between;
}

.card-item {
  flex: 0 0 calc(33.33% - 1rem);
}

.bottom {
  width: 100%;
  display: flex;
  gap: 1rem;
}

.goal-products {
  width: 65%;
}
.recommendation {
  width: 35%;
}
</style>
