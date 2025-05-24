<template>
  <div class="goal-container">
    <Form>
      <div class="goal">
        <div class="goal-name">
          <CustomInputText
            :label-name="'어떤 목표를 달성하고 싶으신가요?'"
            v-model="goalName"
            :is-icon="true"
            :icon-class="'pi pi-star'"
            :input-id="'target-amount'"
            :input-placeholder="'예) 전세 자금 마련하기'"
          />
        </div>
        <div class="target-amount">
          <CustomInputNumber
            :label-name="'목표 금액을 알려주세요.'"
            v-model="targetAmount"
            :is-icon="true"
            :icon-class="'pi pi-star'"
            :input-id="'target-amount'"
            :input-placeholder="'0'"
            :unit="'원'"
          />
        </div>
        <div class="target-period">
          <h3>시작 시기와 끝 시기를 알려주세요.</h3>
          <div class="date-picker">
            <DatePicker
              placeholder="시작 날짜"
              date-format="yy/mm/dd"
              v-model="startDate"
              showButtonBar
            />
            <DatePicker
              placeholder="끝 날짜"
              date-format="yy/mm/dd"
              v-model="endDate"
              showButtonBar
            />
          </div>
        </div>
        <div class="goal-method">
          <label for="product-type"
            ><h3>목표를 달성할 방식을 알려주세요.</h3></label
          >
          <SelectButton
            id="product-type"
            v-model="selectedProductType"
            :options="productType"
            optionLabel="name"
            multiple
            aria-labelledby="multiple"
            fluid
          />
        </div>
      </div>
      <CustomButton
        @click="setGoal"
        label-name="목표 설정하기"
        type="submit"
        justify="end"
      ></CustomButton>
    </Form>
  </div>
</template>

<script setup>
import CustomInputNumber from "@/components/input/CustomInputNumber.vue";
import CustomInputText from "@/components/input/CustomInputText.vue";
import SelectButton from "primevue/selectbutton";
import CustomButton from "@/components/button/CustomButton.vue";
import DatePicker from "primevue/datepicker";
import axiosInstance from "@/api/axiosInstance";

import { Form } from "@primevue/forms";
import { ref } from "vue";

const goalName = ref("");
const targetAmount = ref("");
const selectedProductType = ref([]);
const startDate = ref("");
const endDate = ref("");
const productType = ref([
  { name: "적금", value: "적금" },
  { name: "예금", value: "예금" }
]);

// 상품 타입에 따라 DB에 저장하는 방식 달라짐
const getProductTypeCode = selection => {
  if (selection.includes("적금") && selection.includes("예금")) return "A";
  if (selection.includes("적금")) return "S";
  if (selection.includes("예금")) return "D";
  return "D"; // 기본값
};

const setGoal = async () => {
  const productTypeCode = getProductTypeCode(selectedProductType.value);

  try {
    const response = await axiosInstance.post(
      "http://127.0.0.1:8000/api/goals/",
      {
        goal_name: goalName.value,
        total_target_amount: Number(targetAmount.value),
        product_type: productTypeCode,
        start_date: startDate.value.toISOString().slice(0, 10),
        end_date: endDate.value.toISOString().slice(0, 10)
      }
    );
    console.log(response.data);

    console.log("목표 설정 완료:", response.data);
  } catch (err) {
    console.error("에러 발생:", err);
  }
};
</script>

<style scoped>
.goal-container {
  width: 60%;
}

.goal {
  margin-bottom: 2rem;
}

.date-picker {
  display: flex;
  gap: 1rem;
}
</style>
