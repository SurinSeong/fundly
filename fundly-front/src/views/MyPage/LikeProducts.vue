<template>
  <div class="likeproducts-container">
    <div class="title">
      <h1>
          <i class="pi pi-cart-plus" style="font-size: 1.8rem"></i>
          찜한 상품 보기
      </h1>
    </div>
    <div class="card-grid">
      <RouterCard
        v-for="wish in wishlist"
        :key="wish.id"
        class="card-item"
        :page-name="'productdetail'"
        :params="{ id: `${wish.id}`, comeFrom: `${wish.come_from}` }"
        :card-title="wish.product_name"
        :card-content="wish.financial_company.company_name"
        :is-icon="true"
        :icon-class="'pi pi-heart-fill'"
        :is-circle="false"
      >
      </RouterCard>
    </div>
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
  padding: 1rem;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  justify-content: center;
}

.card-item {
  flex: 0 0 calc(20% - 1rem);
  aspect-ratio: 3/2;
  box-sizing: border-box;
}
</style>