<!-- GoalDetail.vue -->
<template>
  <div class="goaldetail-container">
    <div class="top">
      <div class="goal-title">
        <h1>{{ goalData.goal_name }}</h1>
        <div class="edit-delete">
          <Button
            type="button"
            icon="pi pi-ellipsis-v"
            @click="toggle"
            aria-haspopup="true"
            aria-controls="overlay_menu"
            text
          />
          <Menu ref="menu" id="overlay_menu" :model="items" :popup="true" />
        </div>
      </div>
      <h3>시작이 반, 조금 더 힘내봐요!</h3>
      <div class="chart-container">
        <Chart
          type="bar"
          :data="chartData"
          :options="chartOptions"
          class="h-[30rem]"
          indexAxis="y"
          fluid
        />
      </div>
    </div>
    <div class="bottom">
      <div class="goal-products">
        <Carousel :value="products" circular="">
          <template #item="slotProps">
            <RouterCard
              class="card-item"
              :page-name="'productdetail'"
              :params="{
                comeFrom: slotProps.data.financial_product ? 'original' : 'additional',
                id: slotProps.data.financial_product ?? slotProps.data.additional_product,
              }"
              :is-progressbar="true"
              :is-duration-months="true"
              :start-date="slotProps.data.start_date"
              :card-title="slotProps.data.product_name"
              :value="(slotProps.data.current_amount / slotProps.data.target_amount) * 100"
              :duration-months="slotProps.data.duration_months"
            ></RouterCard>
          </template>
        </Carousel>
      </div>
      <div class="recommendation">
        <h3 class="title">
          <i class="pi pi-check-circle" style="font-size: 1rem"></i>
          금융 상품 추천
        </h3>
        <!-- <RouterLink
          v-for="product in productList"
          :key="product.id"
          :to="{ name: 'productdetail', params: { comeFrom: `${goal.come_from}`, id: product.id } }"
        >
          <CustomTextButton :label-name="product.title">
            {{ product.title }}
          </CustomTextButton>
        </RouterLink> -->
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter, RouterLink } from 'vue-router'
import Chart from 'primevue/chart'
import RouterCard from '@/components/card/RouterCard.vue'
import CustomTextButton from '@/components/button/CustomTextButton.vue'
import Carousel from 'primevue/carousel'
import { useConfirm } from 'primevue/useconfirm'
import Button from 'primevue/button'
import Menu from 'primevue/menu'
import axiosInstance from '@/api/axiosInstance'

const route = useRoute()
const router = useRouter()
const goalId = route.params.goalid

const goalData = ref({})
const products = ref(null)
const totalTargetAmount = ref(0)

const userStore = useUserStore();
onMounted(async () => {
  await userStore.fetchUser();

});

const username = computed(() => userStore.user?.username ?? "");
const birthDate = ref(null)
const workType = ref("")
const salary = ref("")
const assets = ref("")

onMounted(async () => {
  try {
    const response = await axiosInstance.get(`http://127.0.0.1:8000/api/goals/${goalId}`)
    goalData.value = response.data
    totalTargetAmount.value = goalData.value.total_target_amount
    products.value = response.data.connected_to_goal

    const enrichedProducts = []
    for (const product of products.value) {
      const productComeFrom = product.financial_product ? 'original' : 'additional'
      
      const productDetail = await axiosInstance.get(
        `http://127.0.0.1:8000/api/finance/products/${productComeFrom}/${product.financial_product}`,
      )
      enrichedProducts.push({
        ...product,
        product_name: productDetail.data.product.product_name,
      })
    }
    products.value = enrichedProducts
    console.log(products.value)

    chartData.value = setChartData()
    chartOptions.value = setChartOptions()
  } catch (error) {
    console.log(error)
  }



  const userinfo = await axiosInstance.get(
    "http://127.0.0.1:8000/api/user/profile/"
  )

  birthDate.value = userinfo.data.birth_date
  workType.value = userinfo.data.work_type
  salary.value = userinfo.data.salary
  assets.value = userinfo.data.assets

  const payload = {
    username: username.value,
    birth_date: birthDate.value,
    work_type: workType.value,
    assets: assets.value,
    salary: salary.value,
    goal: goalData.value.goal_name,
  }

  console.log(payload)

  await axiosInstance.post(
    "http://127.0.0.1:8000/api/recommendation/",
    payload
  )
})

const chartData = ref()
const chartOptions = ref()
const date = new Date()
const setChartData = () => {
  const documentStyle = getComputedStyle(document.documentElement)

  return {
    labels: ['2025-05'],
    datasets: [
      {
        type: 'bar',
        label: '적금',
        backgroundColor: documentStyle.getPropertyValue('--p-indigo-700'),
        data: [50, 25, 12, 48, 90, 76, 42],
      },
      {
        type: 'bar',
        label: '예금',
        backgroundColor: documentStyle.getPropertyValue('--p-indigo-500'),
        data: [21, 84, 24, 75, 37, 65, 34],
      },
      {
        type: 'bar',
        label: '그 외',
        backgroundColor: documentStyle.getPropertyValue('--p-indigo-300'),
        data: [41, 52, 24, 74, 23, 21, 32],
      },
    ],
  }
}
const setChartOptions = () => {
  const documentStyle = getComputedStyle(document.documentElement)
  const textColor = documentStyle.getPropertyValue('--p-text-color')
  const textColorSecondary = documentStyle.getPropertyValue('--p-text-muted-color')
  const surfaceBorder = documentStyle.getPropertyValue('--p-content-border-color')

  return {
    indexAxis: 'y',
    maintainAspectRatio: false,
    aspectRatio: 0.8,
    plugins: {
      tooltip: {
        mode: 'index',
        intersect: false,
      },
      legend: {
        labels: {
          color: textColor,
        },
      },
    },
    scales: {
      x: {
        stacked: true,
        ticks: {
          color: textColorSecondary,
        },
        grid: {
          color: surfaceBorder,
        },
        max: totalTargetAmount.value,
      },
      y: {
        stacked: true,
        ticks: {
          color: textColorSecondary,
        },
        grid: {
          color: surfaceBorder,
        },
      },
    },
  }
}

// 목표 수정
const editGoal = async () => {
  try {
    router.push(`/checkgoal/edit/${goalId}`)
  } catch (err) {
    console.log(err)
  }
}

const addData = async () => {
  try {
    // 데이터 추가 로직 작성
  } catch (error) {}
}

const menu = ref()
const confirm = useConfirm()
const lastClickEvent = ref(null)

const deletePost = async () => {
  try {
    await axiosInstance.delete(`http://127.0.0.1:8000/api/goals/${goalId}/`)
    router.push('/')
  } catch (err) {
    console.log(err)
  }
}

const showConfirmDelete = () => {
  confirm.require({
    message: '정말 삭제하시겠습니까?',
    header: '삭제 하기',
    icon: 'pi pi-exclamation-triangle',
    rejectProps: {
      label: '취소',
      severity: 'secondary',
      outlined: true,
    },
    acceptProps: {
      label: '삭제 하기',
    },
    accept() {
      deletePost()
    },
    reject() {
      // 취소 시 처리
    },
    target: lastClickEvent.value?.currentTarget,
  })
}

const items = ref([
  {
    items: [
      { label: '목표 수정', icon: 'pi pi-pen-to-square', command: editGoal },
      {
        label: '목표 삭제',
        icon: 'pi pi-times',
        command: showConfirmDelete,
      },
      { label: '데이터 추가', icon: 'pi pi-plus', command: addData },
    ],
  },
])

const toggle = (event) => {
  lastClickEvent.value = event
  menu.value.toggle(event)
}

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
  saving: saving.value,
  deposit: deposit.value,
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

<style scoped>
.goaldetail-container {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: space-between;
}

.top {
  width: 100%;
}

.goal-title {
  display: flex;
  justify-content: space-between;
}

.chart-container {
  width: 100%;
  margin: 1rem 0 1rem 0;
}
.title {
  text-align: center;
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
