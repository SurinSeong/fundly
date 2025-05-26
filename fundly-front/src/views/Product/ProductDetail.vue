<template>
  <div class="product-detail-container">
    <div class="product-container">
      <h2>{{ productName }}</h2>
      <h3>{{ companyName }}</h3>
    </div>
    <p class="join-way">{{ joinWay }}</p>
    <p class="description-title"><b>상세 설명</b></p>
    <pre class="description">{{ etcNote }}</pre>

    <div class="connect-to-data">
      <Select
        v-model="selectedGoal"
        placeholder="연결할 목표를 선택해주세요."
        optionLabel="label"
        optionValue="value"
        :options="goalNames"
      ></Select>
      <div class="target-amount">
        <CustomInputNumber
          v-model="targetAmount"
          :input-id="'target-amount'"
          :input-placeholder="'해당 상품의 목표 금액을 알려주세요.'"
          :unit="'만 원'"
        />
      </div>
      <div class="date-picker">
        <DatePicker
          placeholder="납입 시작 날짜"
          date-format="yy/mm/dd"
          v-model="startDate"
          showButtonBar
        />
        <DatePicker
          placeholder="납입 마지막 날짜"
          date-format="yy/mm/dd"
          v-model="endDate"
          showButtonBar
        />
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
import { useRoute } from 'vue-router'
import { onMounted, ref } from 'vue'
import Select from 'primevue/select'
import DatePicker from 'primevue/datepicker'
import CustomButton from '@/components/button/CustomButton.vue'
import CustomInputNumber from '@/components/input/CustomInputNumber.vue'
import axiosInstance from '@/api/axiosInstance.js'

const route = useRoute()
const productId = Number(route.params.id)
const comeFrom = route.params.comeFrom

// 상품 정보
const companyName = ref('')
const productName = ref('')
const joinWay = ref('')
const endInterestRate = ref('')
const etcNote = ref('')

// 목표에 연결
const goals = ref([])
const goalNames = ref([])
const selectedGoal = ref('')
const startDate = ref('')
const endDate = ref('')
const targetAmount = ref()
const getMonthDifference = (startDate, endDate) => {
  const start = new Date(startDate)
  const end = new Date(endDate)

  const yearDiff = end.getFullYear() - start.getFullYear()
  const monthDiff = end.getMonth() - start.getMonth()

  return yearDiff * 12 + monthDiff + 1 // +1은 시작월 포함
}

onMounted(async () => {
  try {
    const response = await axiosInstance.get(
      `http://127.0.0.1:8000/api/finance/products/${comeFrom}/${productId}`,
    )
    const goalsResponse = await axiosInstance.get('http://127.0.0.1:8000/api/goals/')

    const companyInfo = response.data.product

    companyName.value = companyInfo.financial_company.company_name
    productName.value = companyInfo.product_name
    joinWay.value = companyInfo.join_way
    endInterestRate.value = companyInfo.end_interest_rate
    etcNote.value = companyInfo.etc_note

    goals.value = goalsResponse.data

    goalNames.value = goals.value.map((goal) => ({
      label: goal.goal_name,
      value: goal.id,
    }))

    console.log('goalNames:', goalNames.value)
    console.log('goals:', goals.value)
  } catch (error) {
    console.log(error)
  }
})
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
      start_date: startDate.value.toISOString().slice(0, 10),
      target_amount: targetAmount.value * 10000,
      duration_months: durationMonths,
    }
    console.log(payload)

    await axiosInstance.post('http://127.0.0.1:8000/api/custom/', payload)
  } catch (error) {
    console.log(error)
  }
}
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
}

.target-amount {
  margin-bottom: 1rem;
}

.connect-to-data {
  width: 75%;
}
</style>
