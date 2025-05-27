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
              :page-name="'connectedproductdetail'"
              :params="{
                goalid: goalId,
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
import { ref, onMounted } from 'vue'
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
})

// 데이터 설정
const chartData = ref()
const chartOptions = ref()
const date = new Date()
const year = date.getFullYear()
const month = date.getMonth()
const setChartData = () => {
  const documentStyle = getComputedStyle(document.documentElement)

  return {
    labels: [`${year}-${month}`],
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

// 데이터 추가 로직 작성
const addData = async () => {
  try {
  } catch (error) {}
}

// Dialog 설정 - 목표 삭제 확인용
const menu = ref()
const confirm = useConfirm()
const lastClickEvent = ref(null)

const deleteGoal = async () => {
  try {
    await axiosInstance.delete(`http://127.0.0.1:8000/api/goals/${goalId}/`)
    router.push('/')
  } catch (err) {
    console.log(err)
  }
}
const showConfirmDelete = () => {
  if (!lastClickEvent.value) return // 방어코드 추가

  confirm.require({
    message: '정말 삭제하시겠습니까?',
    header: '목표 삭제 하기',
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
      deleteGoal()
    },
    reject() {},
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
    ],
  },
])

const toggle = (event) => {
  lastClickEvent.value = event
  menu.value.toggle(event)
}
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
