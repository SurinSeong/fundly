<template>
  <label :for="iconclass"
    ><h3>{{ labelname }}</h3></label
  >
  <IconField>
    <InputIcon v-if="isicon">
      <i :class="iconclass" style="color: var(--p-amber-400)" />
    </InputIcon>
    <InputText
      :id="inputid"
      :v-model="inputtext"
      :placeholder="inputplaceholder"
      :type="inputtype"
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
import InputText from "primevue/inputtext";


defineProps({
  labelname: String,
  isicon: Boolean,
  iconclass: String,
  iconcolor: String,
  inputtext: String,
  inputid: String,
  inputplaceholder: String,
  inputtype: String
});
</script>

<style scopped></style>
