<template>
  <div class="goal-container">
    <Form>
      <div class="goal">
        <div class="goal-name">
          <label for="goal-name"><h3>목표를 알려주세요.</h3></label>
          <IconField>
            <InputIcon>
              <i class="pi pi-star" style="color: var(--p-amber-400)" />
            </InputIcon>
            <InputText
              id="goal-name"
              v-model="goalName"
              placeholder="예) 목돈 만들기, 유학 자금 모으기"
              fluid
            />
          </IconField>
        </div>
        <div class="target-amount">
          <label for="target-amount"><h3>목표 금액을 알려주세요.</h3></label>
          <IconField>
            <InputIcon>
              <i class="pi pi-star" style="color: var(--p-amber-400)" />
            </InputIcon>
            <InputNumber id="target-amount" v-model="targetAmount" placeholder="0" fluid />
            <InputIcon>
              <span>원</span>
            </InputIcon>
          </IconField>
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
        <Button class="btn" label="목표 설정하기" type="submit"></Button>
      </div>
    </Form>
  </div>
</template>

<script setup>
import InputText from 'primevue/inputtext'
import InputNumber from 'primevue/inputnumber'
import IconField from 'primevue/iconfield'
import InputIcon from 'primevue/inputicon'
import SelectButton from 'primevue/selectbutton'
import { Form } from '@primevue/forms'
import { ref } from 'vue'

const goalName = ref('')
const targetAmount = ref('')
const selectedProductType = ref([])
const productType = ref([
  { name: '적금', value: '적금' },
  { name: '예금', value: '예금' },
])
</script>

<style scoped>
.goal-container {
  width: 100%;
}

.goal {
  margin-bottom: 2rem;
}

.btn-container {
  display: flex;
  justify-content: flex-end;
}

.btn {
  background-color: var(--p-indigo-500) !important;
  color: var(--p-primary-100) !important;
  border: none;
}
</style>
