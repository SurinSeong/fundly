<template>
  <div class="goal-container">
    <Form>
      <div class="goal">
        <div class="goal-name">
          <CustomInputText
            :labelname="'어떤 목표를 달성하고 싶으신가요?'"
            :isicon="true"
            :iconclass="'pi pi-star'"
            :inputid="'target-amount'"
            :inputplaceholder="'예) 전세 자금 마련하기'"
          />
        </div>
        <div class="target-amount">
          <CustomInputNumber
            :labelname="'목표 금액을 알려주세요.'"
            :isicon="true"
            :iconclass="'pi pi-star'"
            :inputid="'target-amount'"
            :inputnumber="0"
            :inputplaceholder="'0'"
            :unit="'원'"
          />
        </div>
        <div class="goal-name">
          <label for=""><h3>목표를 달성할 방식을 알려주세요.</h3></label>
          <SelectButton
            v-model="selectedProductType"
            :options="productType"
            optionLabel="name"
            multiple
            aria-labelledby="multiple"
            fluid
          />
        </div>
      </div>
      <div class="btn-container">
        <CustomButton label="목표 설정하기" type="submit"></CustomButton>
      </div>
    </Form>
  </div>
</template>

<script setup>
import InputText from "primevue/inputtext";
import CustomInputNumber from "@/components/input/CustomInputNumber.vue";
import CustomInputText from "@/components/input/CustomInputText.vue";

import SelectButton from "primevue/selectbutton";
import CustomButton from "@/components/button/CustomButton.vue";
import { Form } from "@primevue/forms";
import { ref } from "vue";

const goalName = ref("");
const targetAmount = ref("");
const selectedProductType = ref([]);
const productType = ref([
  { name: "적금", value: "적금" },
  { name: "예금", value: "예금" }
]);
</script>

<style scoped>
.goal-container {
  width: 60%;
}

.goal {
  margin-bottom: 2rem;
}

.btn-container {
  display: flex;
  justify-content: flex-end;
}
</style>
