<template>
  <label :for="inputId"
    ><h3>{{ labelName }}</h3></label
  >
  <IconField>
    <InputIcon v-if="isicon">
      <i :class="iconclass" style="color: var(--p-amber-400)" />
    </InputIcon>
    <InputText
      :id="inputId"
      :value="modelValue"
      :placeholder="inputplaceholder"
      :type="inputType"
      @input="(e) => emit('update:modelValue', e.target.value)"
      fluid
    />
    <Message v-if="error" size="small" severity="error" variant="simple" fluid>{{
      message
    }}</Message>

    <InputIcon> </InputIcon>
  </IconField>
</template>

<script setup>
import IconField from 'primevue/iconfield'
import InputIcon from 'primevue/inputicon'
import InputText from 'primevue/inputtext'
import Message from 'primevue/message'
defineProps({
  labelName: String,
  isicon: Boolean,
  iconclass: String,
  iconcolor: String,
  modelValue: String,
  inputId: String,
  inputplaceholder: String,
  inputType: String,
  error: Boolean,
  message: String,
})

const emit = defineEmits(['update:modelValue'])
</script>

<style scopped></style>
