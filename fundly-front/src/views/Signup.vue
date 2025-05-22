<template>
  <div class="signup-container">
    <h1>회원가입</h1>
    <Form:post>
      <CustomInputText :labelname="'닉네임을 입력해주세요.'" :isicon="true" :iconclass="'pi pi-star'"/>
      <br>
      <CustomButton labelname="가입하기" :justify="'end'"/>
    </Form:post>
  </div>
</template>

<script setup>
import { Form } from "@primevue/forms";
import CustomInputText from "@/components/input/CustomInputText.vue";
import CustomButton from "@/components/button/CustomButton.vue";
</script>

<style scoped>
.signup-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
