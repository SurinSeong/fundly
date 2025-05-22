<template>
  <div class="login-container">
    <h1>로그인</h1>
    <Form:post>
      <div class="login-field">
        <CustomInputText :labelname="'아이디'" :inputtype="'id'" />
        <CustomInputText :labelname="'비밀번호'" :inputtype="'password'" />
      </div>
      <CustomButton labelname="로그인" :justify="'end'" />
    </Form:post>
    <div class="social-login">
      <SocialLoginButton
        v-for="social in socialLoginButtons"
        :key="social.name"
        :socialname="social.name"
        :srcpath="social.srcpath"
      />
    </div>
    <div class="sign-up">
      <p>아직 회원이 아니신가요?</p>
      <RouterLink :to="{ name: 'signup' }">회원 가입 하러 가기</RouterLink>
    </div>
  </div>
</template>

<script setup>
import { Form } from "@primevue/forms";
import { RouterLink } from "vue-router";
import { ref } from "vue";

import CustomInputText from "@/components/input/CustomInputText.vue";
import CustomButton from "@/components/button/CustomButton.vue";
import SocialLoginButton from "@/components/button/SocialLoginButton.vue";
import googleLogo from "@/assets/googlelogo.png";
import kakaoLogo from "@/assets/kakaologo.png";

const socialLoginButtons = ref([
  {
    name: "google",
    srcpath: googleLogo
  },
  {
    name: "kakao",
    srcpath: kakaoLogo
  }
]);
</script>

<style scoped>
.login-container {
  width: 70%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.login-field {
  margin-bottom: 2rem;
}

.social-login {
  width: 100%;
  display: flex;
  justify-content: space-evenly;
  margin-top: 2rem;
}
.sign-up {
  text-align: center;
  margin-top: 2rem;
}
</style>
