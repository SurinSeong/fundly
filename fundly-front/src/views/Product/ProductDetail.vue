<template>
  <div class="product-detail-container">
    <h2>{{ productName }}</h2>
    <h3>{{ companyName }}</h3>
    <p>{{ joinWay }}</p>
    <pre>{{ endInterestRate }}</pre>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { onMounted, ref } from 'vue'
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
onMounted(async () => {
  try {
    const response = await axiosInstance.get(
      `http://127.0.0.1:8000/api/finance/products/${comeFrom}/${productId}`,
    )
    const companyInfo = response.data.product
    console.log(companyInfo)

    companyName.value = companyInfo.financial_company.company_name
    productName.value = companyInfo.product_name
    joinWay.value = companyInfo.join_way
    endInterestRate.value = companyInfo.end_interest_rate
    console.log(response.data)
  } catch (error) {
    console.log(error)
  }
})
</script>

<style scoped>
.product-detail-container {
  width: 60%;
}
</style>
