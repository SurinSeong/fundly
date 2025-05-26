<template>
  <div class="goal-container">
    <Form>
      <div class="goal">
        <div class="goal-name">
          <h3>어떤 목표를 달성하고 싶으신가요?</h3>
          <CustomInputText
            v-model="goalName"
            :is-icon="true"
            :icon-class="'pi pi-star'"
            :input-id="'goal-name'"
            :input-placeholder="'예) 전세 자금 마련하기'"
          />
        </div>

        <div class="target-amount">
          <h3>목표 금액을 설정해주세요.</h3>
          <CustomInputNumber
            v-model="targetAmount"
            :key="targetAmountKey"
            :is-icon="true"
            :icon-class="'pi pi-star'"
            :input-id="'target-amount'"
            :input-placeholder="'0'"
            :unit="'만 원'"
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
          <label for="product-type">
            <h3>목표를 달성할 방식을 알려주세요.</h3>
          </label>
          <SelectButton
            id="product-type"
            v-model="selectedProductType"
            :key="selectedProductTypeKey"
            :options="productType"
            optionValue="value" 
            optionLabel="name"
            multiple
            aria-labelledby="multiple"
            fluid
          />
        </div>
      </div>

      <CustomButton
        @click="saveGoal"
        :label-name="isEditMode ? '목표 수정하기' : '목표 설정하기'"
        type="submit"
        justify="end"
      />
    </Form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import axiosInstance from "@/api/axiosInstance";

import CustomInputNumber from "@/components/input/CustomInputNumber.vue";
import CustomInputText from "@/components/input/CustomInputText.vue";
import SelectButton from "primevue/selectbutton";
import CustomButton from "@/components/button/CustomButton.vue";
import DatePicker from "primevue/datepicker";
import { Form } from "@primevue/forms";

const route = useRoute();
const router = useRouter();
const goalId = route.params.goalid;
const isEditMode = !!goalId;

const goalName = ref("");
const targetAmount = ref(null);
const selectedProductType = ref(null);
const startDate = ref("");
const endDate = ref("");

const targetAmountKey = ref(0);
const selectedProductTypeKey = ref(0);

const productType = ref([
  { name: "적금", value: "적금" },
  { name: "예금", value: "예금" }
]);

const getProductTypeCode = selection => {
  if (selection.includes("적금") && selection.includes("예금")) return "A";
  if (selection.includes("적금")) return "S";
  if (selection.includes("예금")) return "D";
  return "D";
};

const saveGoal = async () => {
  console.log(selectedProductType.value);
  
  const productTypeCode = getProductTypeCode(selectedProductType.value);
  console.log(productTypeCode)
  const payload = {
    goal_name: goalName.value,
    total_target_amount: Number(targetAmount.value) * 10000,
    product_type: productTypeCode,
    start_date: startDate.value.toISOString().slice(0, 10),
    end_date: endDate.value.toISOString().slice(0, 10)
  };

  try {
    if (isEditMode) {
      await axiosInstance.put(
        `http://127.0.0.1:8000/api/goals/${goalId}/`,
        payload
      );
      console.log("목표 수정 완료");
    } else {
      await axiosInstance.post("http://127.0.0.1:8000/api/goals/", payload);
      console.log("목표 설정 완료");
    }
    router.replace("/");
  } catch (err) {
    console.error("에러 발생:", err);
  }
};

onMounted(async () => {
  if (isEditMode) {
    try {
      const response = await axiosInstance.get(
        `http://127.0.0.1:8000/api/goals/${goalId}/`
      );
      const data = response.data;

      goalName.value = data.goal_name;
      targetAmount.value = Number(data.total_target_amount) / 10000;
      targetAmountKey.value++;

      if (data.product_type === "A") {
        selectedProductType.value = ["적금", "예금"];
      } else if (data.product_type === "S") {
        selectedProductType.value = ["적금"];
      } else if (data.product_type === "D") {
        selectedProductType.value = ["예금"];
      }
      selectedProductType.value = [...selectedProductType.value];
      selectedProductTypeKey.value++;
      startDate.value = new Date(data.start_date);
      endDate.value = new Date(data.end_date);
    } catch (err) {
      console.error("목표 정보 불러오기 실패:", err);
    }
  }
});
</script>

<style scoped>
h3 {
  margin-bottom: 1rem;
}
.goal-container {
  width: 100%;
}
.goal {
  margin-bottom: 2rem;
}
.goal-name,
.target-amount,
.target-period {
  margin-bottom: 1rem;
}
.date-picker {
  display: flex;
  gap: 1rem;
}
</style>
