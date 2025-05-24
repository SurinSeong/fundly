<!-- RouterCard.vue -->
<template>
  <Card :class="backgroundcolor" class="hover card center">
    <template #title>
      {{ cardtitle }}
    </template>
    <template #content>
      <div
        v-for="product in productlist"
        :key="product.finance_product ?? product.additional_product"
      >
        <RouterLink :to="{ name: pagename, params: { productid: product.id } }" class="decorate"
          ><CustomTextButton :labelname="product.title"></CustomTextButton
        ></RouterLink>
      </div>
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
</template>

<script setup>
import Card from 'primevue/card'
import ProgressBar from 'primevue/progressbar'
import CustomTextButton from '../button/CustomTextButton.vue'
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
