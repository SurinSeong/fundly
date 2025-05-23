<!-- RouterCard.vue -->
<template>
  <RouterLink class="decorate" :to="{ name: pagename, params: params }">
    <Card :class="backgroundcolor" class="hover card center">
      <template #title>
        {{ cardtitle }}
      </template>
      <template #content>
        <ul
          v-for="product in productlist"
          :key="product.finance_product ?? product.additional_product"
        >
          <li>{{ product.title }}</li>
        </ul>
        <p class="text-end">{{ startdate }}</p>
        <ProgressBar v-if="isprogressbar" :value="value"></ProgressBar>
        <div v-if="isicon" class="icon-container">
          <div class="icon">
            <i :class="iconclass"></i>
          </div>
        </div>
        <p v-if="isdurationmonths" class="text-end">{{ durationmonths }} 개월</p>
      </template>
    </Card>
  </RouterLink>
</template>

<script setup>
import Card from 'primevue/card'
import ProgressBar from 'primevue/progressbar'
import { RouterLink } from 'vue-router'

defineProps({
  pagename: String,
  params: Object,
  cardtitle: String,
  startdate: String,
  isicon: Boolean,
  iconclass: String,
  productlist: Array,
  isprogressbar: Boolean,
  isdurationmonths: Boolean,
  value: Number,
  durationmonths: Number,
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

.backgroundcolor {
  color: var(--p-primary-50);
  background-color: var(--p-indigo-300);
}
</style>
