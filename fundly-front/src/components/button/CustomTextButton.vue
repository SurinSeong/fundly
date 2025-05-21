<template>
  <Button class="btn" :class="classname" :label="labelname" text />
</template>

<script setup>
import Button from "primevue/button";
defineProps({
  classname: Object,
  labelname: String,
});
</script>

<style scopped>
.btn:hover {
  background-color: var(--p-indigo-50) !important;
  color: var(--p-indigo-700) !important;
}

.btn.active {
  background-color: var(--p-indigo-50);
  color: var(--p-indigo-700);
}

.btn:focus {
  background-color: var(--p-indigo-50);
  color: var(--p-indigo-700);
}
</style>
