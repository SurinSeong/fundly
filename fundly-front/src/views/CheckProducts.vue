<!-- CheckProducts.vue -->

<template>
  <div class="checkproducts-container">
    <h2>시중에 공개된 예금, 적금 상품을 확인해보세요.</h2>
    <CustomDataTable
      :type="'products'"
      :searchplaceholder="'은행 이름 / 적금 이름'"
      :data="savings"
      :column-infos="columnInfos"
      :page-name="'productdetail'"
    >
    </CustomDataTable>
  </div>
</template>

<script setup>
import CustomDataTable from '@/components/table/CustomDataTable.vue'
import { ref } from 'vue'

const savings = ref([
  {
    id: 1,
    financial_company: '싸피은행',
    product_name: '1',
    interest_rate_6: '5%',
    interest_rate_12: '4%',
    interest_rate_24: '3%',
    interest_rate_36: '2%',
    over_36: '1%',
    join_way: '인터넷',
  },
  {
    id: 2,
    financial_company: '싸피은행',
    product_name: '2',
    interest_rate_6: '5%',
    interest_rate_12: '4%',
    interest_rate_24: '3%',
    interest_rate_36: '2%',
    over_36: '1%',
    join_way: '인터넷',
  },
  {
    id: 3,
    financial_company: '싸피은행',
    product_name: '3',
    interest_rate_6: '5%',
    interest_rate_12: '4%',
    interest_rate_24: '3%',
    interest_rate_36: '2%',
    over_36: '1%',
    join_way: '인터넷',
  },
  {
    id: 4,
    financial_company: '싸피은행',
    product_name: '4',
    interest_rate_6: '5%',
    interest_rate_12: '4%',
    interest_rate_24: '3%',
    interest_rate_36: '2%',
    over_36: '1%',
    join_way: '인터넷',
  },
  {
    id: 5,
    financial_company: '싸피은행',
    product_name: '5',
    interest_rate_6: '5%',
    interest_rate_12: '4%',
    interest_rate_24: '3%',
    interest_rate_36: '2%',
    over_36: '1%',
    join_way: '인터넷',
  },
  {
    id: 6,
    financial_company: '싸피은행',
    product_name: '6',
    interest_rate_6: '5%',
    interest_rate_12: '4%',
    interest_rate_24: '3%',
    interest_rate_36: '2%',
    over_36: '1%',
    join_way: '인터넷',
  },
  {
    id: 7,
    financial_company: '싸피은행',
    product_name: '7',
    interest_rate_6: '5%',
    interest_rate_12: '4%',
    interest_rate_24: '3%',
    interest_rate_36: '2%',
    over_36: '1%',
    join_way: '인터넷',
  },
  {
    id: 8,
    financial_company: '싸피은행',
    product_name: '8',
    interest_rate_6: '5%',
    interest_rate_12: '4%',
    interest_rate_24: '3%',
    interest_rate_36: '2%',
    over_36: '1%',
    join_way: '인터넷',
  },
  {
    id: 9,
    product_name: '9',
    financial_company: '싸피은행',
    interest_rate_6: '5%',
    interest_rate_12: '4%',
    interest_rate_24: '3%',
    interest_rate_36: '2%',
    over_36: '1%',
    join_way: '인터넷',
  },
])

const columnNames = Object.keys(savings.value[0]).slice(1)
const headers = [
  '은행 이름',
  '상품 이름',
  '6개월',
  '12개월',
  '24개월',
  '36개월',
  '36개월 이상',
  '가입 방법',
]

const columnInfos = ref([])

for (const i in columnNames) {
  const columnInfo = {
    field: columnNames[i],
    header: headers[i],
  }
  columnInfos.value.push(columnInfo)
}
</script>

<style scoped>
.checkproducts-container {
}
</style>
