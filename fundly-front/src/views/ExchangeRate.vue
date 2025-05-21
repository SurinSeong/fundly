<template>
  <div class="exchange-container">
    <h2>환율</h2>
    <div class="money">
      <Form:get>
        <CustomInputNumber :inputid="'won'" v-model="input" :unit="'₩'"></CustomInputNumber>
      </Form:get>
    </div>
    <div class="money">
      <Form:get>
        <CustomInputNumber :inputid="'dollar'" v-model="output" :unit="'$'"></CustomInputNumber>
      </Form:get>
    </div>
  </div>
</template>

<script setup>
import InputNumber from "primevue/inputnumber";
import CustomInputNumber from "@/components/input/CustomInputNumber.vue";
import { Form } from "@primevue/forms";

import { ref } from "vue";

const input = ref();
const output = ref();
</script>

<style scoped>
.exchange-container {
  width: 60%;
}

label {
  padding-left: 1rem;
}
.money {
  margin-bottom: 1rem;
}
</style>
