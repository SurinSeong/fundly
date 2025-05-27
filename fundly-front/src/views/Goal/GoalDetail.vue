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
      <h3>{{ cheerUpMessage }}</h3>
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
              :value="
                Math.floor((slotProps.data.current_amount / slotProps.data.target_amount) * 100)
              "
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
          :to="{
            name: 'productdetail',
            params: { comeFrom: `${product.come_from}`, id: product.id },
          }"
        >
          <Button :label="product.product_name" text fluid=""> </Button>
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user'
import { ref, onMounted, computed, watchEffect } from 'vue'
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
const cheerUpMessage = ref('')

onMounted(async () => {
  try {
    const response = await axiosInstance.get(`http://127.0.0.1:8000/api/goals/${goalId}`)
    goalData.value = response.data
    totalTargetAmount.value = goalData.value.total_target_amount
    products.value = response.data.connected_to_goal

    const enrichedProducts = []
    for (const product of products.value) {
      const productComeFrom = product.financial_product ? 'original' : 'additional'

      // 여기서 product.financial_product가 null일 수도 있으니 방어코드 추가 권장
      const productId = product.financial_product ?? product.additional_product

      const productDetail = await axiosInstance.get(
        `http://127.0.0.1:8000/api/finance/products/${productComeFrom}/${productId}`,
      )

      enrichedProducts.push({
        ...product,
        product_name: productDetail.data.product.product_name,
        product_type: productDetail.data.product.product_type,
      })
    }
    products.value = enrichedProducts
  } catch (error) {
    console.log(error)
  }

  // 사용자 정보 요청 및 추천 상품 처리
  try {
    const userinfo = await axiosInstance.get('http://127.0.0.1:8000/api/user/profile/')
    const requiredFields = ['assets', 'birth_date', 'salary', 'work_type']
    const isAnyFieldMissing = requiredFields.some((field) => !userinfo.data[field])

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

      await axiosInstance.post('http://127.0.0.1:8000/api/recommendation/', payload)
      const recommendation = await axiosInstance.get('http://127.0.0.1:8000/api/recommendation/')
      recommendationProductList.value = recommendation.data.products
    }
  } catch (error) {
    console.log(error)
  }
})

// 총 적금 합산 (savingTotal)
const savingTotal = computed(() => {
  if (!products.value) return 0
  return products.value
    .filter((p) => p.product_type !== 'D')
    .reduce((sum, p) => sum + p.current_amount, 0)
})

// 총 예금 합산 (depositTotal)
const depositTotal = computed(() => {
  if (!products.value) return 0
  return products.value
    .filter((p) => p.product_type === 'D')
    .reduce((sum, p) => sum + p.current_amount, 0)
})

// 메시지 변화
const currentTotal = computed(() => {
  return depositTotal.value + savingTotal.value
})

watchEffect(() => {
  const rate = currentTotal.value / totalTargetAmount.value

  if (rate >= 1) {
    cheerUpMessage.value = '목표 달성! 축하해요! 🎉'
  } else if (rate >= 0.9) {
    cheerUpMessage.value = '거의 다 왔어요! 마지막 한 걸음만 더!'
  } else if (rate >= 0.8) {
    cheerUpMessage.value = '고지가 눈 앞이에요! 조금만 더 힘내요!'
  } else if (rate >= 0.7) {
    cheerUpMessage.value = '좋아요, 70%까지 왔어요!'
  } else if (rate >= 0.6) {
    cheerUpMessage.value = '벌써 반을 넘었어요! 꾸준함이 빛나고 있어요.'
  } else if (rate >= 0.5) {
    cheerUpMessage.value = '절반 달성! 여기서부터가 진짜예요!'
  } else if (rate >= 0.4) {
    cheerUpMessage.value = '반환점에 거의 다왔어요! 계속 가봐요!'
  } else if (rate >= 0.3) {
    cheerUpMessage.value = '서서히 힘이 붙기 시작했어요!'
  } else if (rate >= 0.2) {
    cheerUpMessage.value = '좋은 출발이에요! 계속해서 나아가요!'
  } else if (rate > 0) {
    cheerUpMessage.value = '시작이 반이에요! 잘하고 있어요!'
  } else {
    cheerUpMessage.value = '목표를 향해 첫 걸음을 내딛어봐요!'
  }
})

const date = new Date()
const year = date.getFullYear()
const month = date.getMonth() + 1

// 차트 데이터 computed
const chartData = computed(() => {
  const documentStyle = getComputedStyle(document.documentElement)

  return {
    labels: [`${year}-${month}`],
    datasets: [
      {
        type: 'bar',
        label: '적금',
        backgroundColor: documentStyle.getPropertyValue('--p-indigo-300'),
        data: [savingTotal.value],
      },
      {
        type: 'bar',
        label: '예금',
        backgroundColor: documentStyle.getPropertyValue('--p-indigo-600'),
        data: [depositTotal.value],
      },
    ],
  }
})

// 차트 옵션 computed
const chartOptions = computed(() => {
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
})

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
