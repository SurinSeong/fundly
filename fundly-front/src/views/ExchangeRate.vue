<template>
  <div class="exchange-container">
    <h2>환율</h2>
    <div class="money">
      <Form:get>
        <InputNumber id="won" v-model="input"></InputNumber>
        <label for="won">₩</label>
      </Form:get>
    </div>
    <div class="money">
      <Form:get>
        <InputNumber id="dollar" v-model="output"></InputNumber>
        <label for="dollar">$</label>
      </Form:get>
    </div>
  </div>
</template>

<script setup>
import InputNumber from 'primevue/inputnumber';

import { Form } from '@primevue/forms'

import { ref } from 'vue'

const input = ref(0)
const output = ref(0)
</script>

<style scoped>
label {
  padding-left: 1rem;
}
.money {
  margin-bottom: 1rem;
} 
</style>
