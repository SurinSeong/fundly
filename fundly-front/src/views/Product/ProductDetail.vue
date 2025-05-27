<template>
  <div class="product-detail-container">
    <div class="product-container">
      <h2>
        {{ productName }}
        <Button 
          :icon="likeClass" 
          severity="danger" 
          variant="text" 
          rounded aria-label="Favorite"
          @click="handleIsLiked"
        />

        <span :class="likeClass" @click="handleIsLiked"></span>
      </h2>
      <h3>{{ companyName }}</h3>
    </div>
    <p class="join-way">{{ joinWay }}</p>
    <p class="description-title"><b>상세 설명</b></p>
    <pre class="description">{{ etcNote }}</pre>

    <div class="connect-to-data">
      <Select
        v-model="selectedGoal"
        :placeholder="placeholder"
        optionLabel="label"
        optionValue="value"
        :options="goalNames"
      ></Select>
      <div class="target-amount">
        <CustomInputNumber
          v-model="targetAmount"
          :input-id="'target-amount'"
          :input-placeholder="targetAmountPlaceholder"
          :unit="'만 원'"
        />
      </div>
      <div class="date-picker">
        <DatePicker
          :placeholder="startDatePlaceholder"
          date-format="yy/mm/dd"
          v-model="startDate"
          showButtonBar
        />
        <DatePicker
          :placeholder="endDatePlaceholder"
          date-format="yy/mm/dd"
          v-model="endDate"
          showButtonBar
        />
      </div>
      <Message v-if="isDateError" severity="error">시작 시기는 끝보다 앞서야 합니다.</Message>
      <div class="handle-end-date">
        <Button label="- 6개월" outlined @click="decrementEndDate"></Button>
        <Button label="+ 6개월" outlined @click="incrementEndDate"></Button>
      </div>
      <div class="connected" v-if="route.path.includes('connected')">
        <div class="current-amount">
          <p cla>현재 저축된 금액을 수정할 수 있습니다.</p>
          <CustomInputNumber input-id="current-amount" v-model="currentAmount" unit="만 원" />
        </div>
      </div>
    </div>

    <CustomButton
      @click="connectToGoal"
      :label-name="'목표와 연결하기'"
      type="submit"
      justify="end"
    />
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { useConfirm } from 'primevue/useconfirm'
import { onMounted, ref, watch, computed } from 'vue'

import Select from 'primevue/select'
import DatePicker from 'primevue/datepicker'
import CustomButton from '@/components/button/CustomButton.vue'
import Button from 'primevue/button'
import CustomInputNumber from '@/components/input/CustomInputNumber.vue'
import axiosInstance from '@/api/axiosInstance.js'
import Message from 'primevue/message'

const confirm = useConfirm()
const router = useRouter()
const route = useRoute()

// 파라미터에서 필요한 값 가져오기
const productId = Number(route.params.id)
const goalId = Number(route.params.goalid)
const comeFrom = route.params.comeFrom

// 상품 정보
const companyName = ref('')
const productName = ref('')
const joinWay = ref('')
const endInterestRate = ref('')
const etcNote = ref('')
const isLiked = ref(false)
const likeClass = computed(() => (isLiked.value ? 'pi pi-heart-fill' : 'pi pi-heart'))

const placeholder = ref('')
const targetAmountPlaceholder = ref('')
const startDatePlaceholder = ref('')
const endDatePlaceholder = ref('')
const companyInfo = ref('')
const productInfo = ref('')


// 목표에 연결
const goals = ref([])
const goalNames = ref([])
const selectedGoal = ref('')
const startDate = ref('')
const endDate = ref('')
const targetAmount = ref()
const currentAmount = ref()

const getMonthDifference = (startDate, endDate) => {
  const start = new Date(startDate)
  const end = new Date(endDate)

  const yearDiff = end.getFullYear() - start.getFullYear()
  const monthDiff = end.getMonth() - start.getMonth()

  return yearDiff * 12 + monthDiff + 1 // +1은 시작월 포함
}

const handleIsLiked = async () => {
  try{
    const response = await axiosInstance.post(
      'http://127.0.0.1:8000/api/wishlist/',
      {
        product_pk: productId,
        come_from: comeFrom,
      }
    )
    if (response.data.is_liked) {
      isLiked.value = true
    }
    else {
      isLiked.value = false
    }
  }
  catch (err) {
    console.error(err)
  }
}

// 6개월씩 감소시키는 버튼
const decrementEndDate = () => {
  // 기준 날짜: endDate가 있으면 그걸 기준으로
  const baseDate = endDate.value ? new Date(endDate.value) : new Date(startDate.value)

  if (!baseDate || isNaN(baseDate)) {
    console.error('유효한 날짜가 없습니다.')
    return
  }

  const newDate = new Date(baseDate)
  newDate.setMonth(newDate.getMonth() - 6)

  // YYYY-MM-DD 형식으로 저장
  endDate.value = newDate.toISOString().slice(0, 10)
}

// 6개월씩 증가시키는 버튼
const incrementEndDate = () => {
  // 기준 날짜를 endDate가 있으면 그걸 기준으로, 없으면 startDate로
  const baseDate = endDate.value ? new Date(endDate.value) : new Date(startDate.value)

  if (!baseDate || isNaN(baseDate)) {
    console.error('유효한 날짜가 없습니다.')
    return
  }

  const newDate = new Date(baseDate)
  newDate.setMonth(newDate.getMonth() + 6)

  // YYYY-MM-DD 형식으로 저장
  endDate.value = newDate.toISOString().slice(0, 10)
}
const isDateError = ref(false)

watch([startDate, endDate], ([newStart, newEnd]) => {
  if (newStart && newEnd) {
    const start = new Date(newStart)
    const end = new Date(newEnd)
    isDateError.value = start > end
  } else {
    isDateError.value = false
  }
})

onMounted(async () => {
  const response = await axiosInstance.get(
    `http://127.0.0.1:8000/api/finance/products/${comeFrom}/${productId}/`,
  )
  productInfo.value = response.data.product
  console.log(productInfo.value)

    // 찜 확인용
    const wishlistResponse = await axiosInstance.get('http://127.0.0.1:8000/api/wishlist/')

    const wishlist = wishlistResponse.data
    const productInfo = { id: productId, come_from: comeFrom }

    isLiked.value = wishlist.some(item => {
      const product = item.financial_product || item.additional_product
      return product?.id === productInfo.id && product?.come_from === productInfo.come_from
    })

    const companyInfo = response.data.product


  const goalsResponse = await axiosInstance.get('http://127.0.0.1:8000/api/goals/')

  companyInfo.value = response.data.product

  companyName.value = companyInfo.value.financial_company.company_name
  productName.value = companyInfo.value.product_name
  joinWay.value = companyInfo.value.join_way
  endInterestRate.value = companyInfo.value.end_interest_rate
  etcNote.value = companyInfo.value.etc_note

  goals.value = goalsResponse.data

  goalNames.value = goals.value.map((goal) => ({
    label: goal.goal_name,
    value: goal.id,
  }))
  if (route.path.includes('connected')) {
    const connectedToGoalData = await axiosInstance.get(`http://127.0.0.1:8000/api/goals/${goalId}`)
    const matchedGoal = goalNames.value.find(
      (goal) => goal.label === connectedToGoalData.data.goal_name,
    )
    if (matchedGoal) {
      selectedGoal.value = matchedGoal.value // ✔️ Select 박스에 기본 선택값 표시됨
    }
  } else {
    placeholder.value = '연결할 목표를 설정해주세요.'
    targetAmountPlaceholder.value = '목표 금액을 설정해주세요.'
    startDatePlaceholder.value = '납입 시작 날짜'
    endDatePlaceholder.value = '납입 끝 날짜'
  }
})


const confirmCheckGoal = (goalId) => {
  confirm.require({
    message: `목표 페이지로 이동합니다.`,
    header: '목표와 성공적으로 연결되었어요!',
    icon: 'pi pi-check',
    rejectProps: {
      label: '상품 더 둘러보기',
      outlined: true,
    },
    acceptProps: {
      label: '목표 확인 하기',
    },
    accept: () => {
      router.replace(`/checkgoal/${goalId}`)
    },
    reject: () => {
      router.replace('/checkproducts')
    },
  })
}

const connectToGoal = async () => {
  try {
    const goalObj = goals.value.find((goal) => goal.id === selectedGoal.value)
    console.log(goalObj)

    if (!goalObj) {
      console.error('해당 목표를 찾을 수 없습니다.')
      return
    }
    const goalId = goalObj.id
    const durationMonths = getMonthDifference(startDate.value, endDate.value)

    const payload = {
      goal: goalId,
      financial_product: productId,
      start_date: new Date(startDate.value).toISOString().slice(0, 10),
      target_amount: targetAmount.value * 10000,
      duration_months: durationMonths,
    }

    await axiosInstance.post('http://127.0.0.1:8000/api/custom/', payload)
    confirmCheckGoal(goalId)
  } catch (error) {
    console.log(error)
  }
}

watch(selectedGoal, (newGoalId) => {
  const selected = goals.value.find((goal) => goal.id === newGoalId)
  console.log(selected)
  if (!selected) return

  // 선택된 목표의 정보로 값 채우기
  if (selected.start_date) startDate.value = selected.start_date
  if (selected.end_date) endDate.value = selected.end_date

  if (selected.total_target_amount) {
    targetAmount.value = selected.total_target_amount / 10000 // 원 → 만 원 단위로 변환
  }
  if (route.path.includes('connected')) {
    const currentGoal = ref('')
    currentGoal.value = selected.connected_to_goal.find(
      (product) => product.financial_product === productId,
    )
    currentAmount.value = currentGoal.value.current_amount / 10000
  }
})
</script>

<style scoped>
.product-detail-container {
  width: 100%;
}

.product-container {
  display: flex;
  justify-content: space-between;
}

.join-way {
  text-align: end;
}

.description {
  text-decoration: none;
  font-size: 1rem;
  font-family: noto-sans;
  white-space: pre-wrap;
  margin-bottom: 2rem;
}

.date-picker {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.target-amount {
  margin-bottom: 1rem;
}

.connect-to-data {
  width: 75%;
  margin-bottom: 1rem;
}

.handle-end-date {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
}
</style>
