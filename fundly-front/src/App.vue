<template>
  <div class="total-container">
    <Sidebar />
    <main><RouterView /></main>
  </div>
</template>

<script setup>
import Sidebar from "@/components/bar/Sidebar.vue";
</script>

<style scoped>
.total-container {
  width: 95%;
  height: 95%;
  display: flex;
  border: 0.3px solid var(--p-gray-300);
  border-radius: 30px;
}

main {
  height: 100%;
  width: 100%;
  flex: 3;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 3rem 0 3rem;
}

@media (max-width: 768px) {
  .total-container {
    width: 100%;
    height: 100%;
    border: none;
  }

  main {
    margin: 3rem 0 0 0;
  }
}
</style>
