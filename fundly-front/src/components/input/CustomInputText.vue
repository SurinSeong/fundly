<template>
  <label :for="iconclass"
    ><h3>{{ labelname }}</h3></label
  >
  <IconField>
    <InputIcon v-if="isicon">
      <i :class="iconclass" style="color: var(--p-amber-400)" />
    </InputIcon>
    <InputNumber
      :id="inputid"
      :v-model="inputnumber"
      :placeholder="inputplaceholder"
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
  labelname: String,
  isicon: Boolean,
  iconclass: String,
  iconcolor: String,
  inputid: String,
  inputplaceholder: String,
});
</script>

<style scopped></style>
