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
        <RouterCard
          v-if="!isUserInfo"
          class="card-item"
          :page-name="'setgoal'"
          :card-title="'개인 정보 설정하기'"
          :is-icon="true"
          :is-progressbar="false"
          :icon-class="'pi pi-chevron-right'"
          :is-round="true"
          :is-flex="true"
          :is-duration-months="false"
        >
        </RouterCard>
        <RouterLink
          v-for="product in recommendationProductList"
          :key="product.id"
          :to="{ name: 'productdetail', params: { comeFrom: `${product.come_from}`, id: product.id } }"
        >
          <Button :label="product.product_name" text fluid="">
          </Button>
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user'
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter, RouterLink } from 'vue-router'
import Chart from 'primevue/chart'
import RouterCard from '@/components/card/RouterCard.vue'
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
const depositTotal = ref(0)
const savingTotal = ref(0)
const userStore = useUserStore()

onMounted(async () => {
  await userStore.fetchUser()
})

const recommendationProductList = ref([])
const isUserInfo = ref(true)
const username = computed(() => userStore.user?.username ?? '')
const birthDate = ref(null)
const workType = ref('')
const salary = ref('')
const assets = ref('')

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
        product_type: productDetail.data.product.product_type,
      })
    }
    products.value = enrichedProducts
    console.log(products.value)

    chartData.value = setChartData()
    chartOptions.value = setChartOptions()
  } catch (error) {
    console.log(error)
  }
  for (const product of products.value) {
    if (product.product_type === 'D') {
      depositTotal.value += goalData.value.curreent_amount
    } else {
      savingTotal.value += goalData.value.current_amount
    }
  }

  const userinfo = await axiosInstance.get('http://127.0.0.1:8000/api/user/profile/')
  console.log(userinfo.data)
  const requiredFields = ['assets', 'birth_date', 'salary', 'work_type']

  const isAnyFieldMissing = requiredFields.some(
    (field) => !userinfo.data[field],
  )

  if (isAnyFieldMissing) {
    isUserInfo.value = false
  } else {
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
      'http://127.0.0.1:8000/api/recommendation/',
      payload,
    )
    const recommendation = await axiosInstance.get(
      'http://127.0.0.1:8000/api/recommendation/'
    )

    recommendationProductList.value = recommendation.data.products
    console.log(recommendationProductList.value)
  }
})

// 데이터 설정
const chartData = ref()
const chartOptions = ref()
const date = new Date()
const year = date.getFullYear()
const month = date.getMonth() + 1
const setChartData = () => {
  const documentStyle = getComputedStyle(document.documentElement)

  return {
    labels: [`${year}-${month}`],
    datasets: [
      {
        type: 'bar',
        label: '적금',
        backgroundColor: documentStyle.getPropertyValue('--p-indigo-700'),
        data: [savingTotal.value],
      },
      {
        type: 'bar',
        label: '예금',
        backgroundColor: documentStyle.getPropertyValue('--p-indigo-500'),
        data: [depositTotal.value],
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
