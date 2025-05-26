<!-- CheckProducts.vue -->
<template>
  <div class="checkproducts-container">
    <h2 class="product-title">시중에 공개된 예금, 적금 상품을 확인해보세요.</h2>
    <div class="select-container">
      <Select
        v-model="productType"
        :options="['전체', '예금', '적금']"
        placeholder="상품 유형 필터"
        class="mb-3"
        style="min-width: 10rem"
        size="small"
      />
    </div>
    <CustomDataTable
      v-if="filteredProducts.length > 0 && columnInfos.length > 0"
      :type="'products'"
      :search-placeholder="'은행 이름 / 상품 이름'"
      :data="filteredProducts"
      :column-infos="columnInfos"
      :page-name="'productdetail'"
    >
    </CustomDataTable>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watchEffect } from 'vue'
import CustomDataTable from '@/components/table/CustomDataTable.vue'
import Select from 'primevue/select'
import axiosInstance from '@/api/axiosInstance.js'

const totalProducts = ref([])
const officialProducts = ref([])
const additionalProducts = ref([])
const productType = ref('전체')

onMounted(async () => {
  const response = await axiosInstance.get('http://127.0.0.1:8000/api/finance/products/')
  officialProducts.value = response.data.official_products || []
  additionalProducts.value = response.data.additional_products || []
  totalProducts.value = officialProducts.value.concat(additionalProducts.value)
})

const columnNames = computed(() => {
  if (totalProducts.value.length === 0) return []
  return ['financial_company', 'product_name', 'product_type']
})
const headers = ['은행 이름', '상품 이름', '상품 유형']

const columnInfos = ref([])

watchEffect(() => {
  if (columnNames.value.length > 0 && columnInfos.value.length === 0) {
    columnInfos.value = columnNames.value.map((name, idx) => ({
      field: name,
      header: headers[idx] || name,
    }))
  }
})

// 필터링된 상품 데이터
const filteredProducts = computed(() => {
  if (productType.value === '전체') {
    return totalProducts.value
  }

  const typeMapping = {
    예금: 'D',
    적금: 'S',
  }

  const filterType = typeMapping[productType.value]
  return totalProducts.value.filter((product) => product.product_type === filterType)
})
</script>

<style scoped>
.product-title {
  margin-bottom: 1rem;
}
.checkproducts-container {
  width: 60%;
}

.select-container {
  margin-bottom: 1rem;
  display: flex;
  justify-content: flex-end;
}
</style>
