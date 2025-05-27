<template>
  <div class="recommended-result-container">
    <h1>추천 결과 확인하기</h1>
    <RouterCard
    
    />
  </div>
  

</template>

<script setup>
  import RouterCard from '@/components/card/RouterCard.vue';
  import { ref, onMounted } from 'vue';
  import axiosInstance from '@/api/axiosInstance';
  
  onMounted(async() => {
    const response = await axiosInstance.get(
        "http://127.0.0.1:8000/api/recommendation/"
    )

    console.log(response.data)
  })
</script>

<style scoped>

</style>