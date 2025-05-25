<template>
  <label :for="iconClass"
    ><h3>{{ labelName }}</h3></label
  >
  <IconField>
    <InputIcon v-if="isIcon">
      <i :class="iconClass" style="color: var(--p-amber-400)" />
    </InputIcon>
    <InputNumber
      :id="inputId"
      :value="modelValue"
      :placeholder="inputPlaceholder"
      @update:modelValue="value => emit('update:modelValue', value)"
      fluid
    />
    <InputIcon>
      <span>{{ unit }}</span>
    </InputIcon>
  </IconField>
</template>

<script setup>
import IconField from "primevue/iconfield";
import InputIcon from "primevue/inputicon";
import InputNumber from "primevue/inputnumber";

defineProps({
  labelName: String,
  isIcon: Boolean,
  iconClass: String,
  iconColor: String,
  modelValue: Number,
  inputId: String,
  inputPlaceholder: String,
  unit: String
});

const emit = defineEmits(["update:modelValue"]);
</script>

<style scopped></style>
