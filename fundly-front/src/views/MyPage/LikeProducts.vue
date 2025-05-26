<template>
  <div class="likeproducts-container">
    <h1>찜한 상품 보기</h1>
    <RouterCard
      v-for="wish in wishlist"
      :key="wish.id"
      class="card-item"
      :page-name="'productdetail'"
      :params="{ id: `${wish.id}`, comeFrom: `${wish.come_from}` }"
      :card-title="wish.product_name"
      :is-icon="true"
      :icon-class="'pi pi-heart-fill'"
    >
    </RouterCard>
  </div>
</template>

<script setup>
import RouterCard from '@/components/card/RouterCard.vue'
import axiosInstance from '@/api/axiosInstance'
import { RouterLink } from 'vue-router'
import { onMounted, ref } from 'vue'

const wishlist = ref([])


onMounted(async () => {
  try {
    const response = await axiosInstance.get('http://127.0.0.1:8000/api/wishlist/')

    for (let i = 0; i < response.data.length; i++) {
      const products = response.data[i];
      if (products.financial_product) {
        wishlist.value.push(products.financial_product)
        console.log(products.financial_product)
      }
      
      if (products.additional_product) {
        wishlist.value.push(products.additional_product)
      }
    }
    console.log(wishlist.value)
  } 
  catch (err) {
    console.log(err)
  }
})
</script>

<style scoped>
.likeproducts-container {
  text-align: center;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
  align-items: center;
}

.card-item {
  flex: 0 0 calc(20% - 1rem);
  aspect-ratio: 3/2;
  box-sizing: border-box;
}
</style>