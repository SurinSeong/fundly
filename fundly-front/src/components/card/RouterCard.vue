<!-- RouterCard.vue -->
<template>
  <RouterLink class="decorate" :to="{ name: pageName, params: params }">
    <Card :class="backgroundcolor" class="hover card center">
      <template #title>
        {{ cardTitle }}
      </template>
      <template #content>
        {{ cardContent }}
        <ul
          v-for="product in productList"
          :key="product.finance_product ?? product.additional_product"
        >
          <li>{{ product.title }}</li>
        </ul>
        <p class="text-end">{{ startDate }}</p>
        <ProgressBar v-if="isProgressbar" :value="value"></ProgressBar>
        <div v-if="isIcon" class="icon-container">
          <div class="icon">
            <i :class="[iconClass, {'no-border': !isCircle}]"></i>
          </div>
        </div>
        <p v-if="isDurationMonths" class="text-end">{{ durationMonths }} 개월</p>
      </template>
    </Card>
  </RouterLink>
</template>

<script setup>
import Card from 'primevue/card'
import ProgressBar from 'primevue/progressbar'
import { RouterLink } from 'vue-router'

defineProps({
  pageName: String,
  params: Object,
  cardTitle: String,
  cardContent: String,
  startDate: String,
  isIcon: Boolean,
  isCircle: Boolean,
  iconClass: String,
  productList: Array,
  isProgressbar: Boolean,
  isDurationMonths: Boolean,
  value: Number,
  durationMonths: Number,
  backgroundcolor: String,
})

</script>

<style scoped>
.decorate {
  text-decoration: none;
}

.hover {
  transition: background-color 0.3s ease;
}

.hover:hover {
  color: var(--p-primary-900);
  background-color: var(--p-indigo-50);
}

.card {
  height: 100%;
}

.text-end {
  text-align: end;
}

.pi {
  padding: 0.4rem;
  border: 0.1px solid;
  border-radius: 1rem;
}

.no-border {
  border: none !important;
}

.backgroundcolor {
  color: var(--p-primary-50);
  background-color: var(--p-indigo-300);
}
</style>
