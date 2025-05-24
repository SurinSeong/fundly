<template>
  <div class="login-container">
    <h1>로그인</h1>
    <Form v-slot="$form" @submit="onFormSubmit">
      <div class="login-field">
        <CustomInputText :label-name="'아이디'" :input-type="'id'" />
        <CustomInputText :label-name="'비밀번호'" :input-type="'password'" />
      </div>
      <CustomButton label-name="로그인" :justify="'end'" />
    </Form>
    <div class="social-login">
      <SocialLoginButton
        v-for="social in socialLoginButtons"
        @click="social.handleFunction"
        :key="social.name"
        :socialname="social.name"
        :src-path="social.srcPath"
      />
    </div>
    <div class="sign-up">
      <p>아직 회원이 아니신가요?</p>
      <RouterLink :to="{ name: 'signup' }">회원 가입 하러 가기</RouterLink>
    </div>
  </div>
</template>

<script setup>
import { Form } from '@primevue/forms'
import { RouterLink } from 'vue-router'
import { ref, onMounted } from 'vue'

import CustomInputText from '@/components/input/CustomInputText.vue'
import CustomButton from '@/components/button/CustomButton.vue'
import SocialLoginButton from '@/components/button/SocialLoginButton.vue'
import googleLogo from '@/assets/googlelogo.png'
import kakaoLogo from '@/assets/kakaologo.png'

const CLIENT_ID = import.meta.env.VITE_GOOGLE_CLIENT_ID
const KAKAO_JS_KEY = import.meta.env.VITE_KAKAO_JS_KEY

onMounted(() => {
  if (typeof window.Kakao !== 'undefined' && !window.Kakao.isInitialized()) {
    window.Kakao.init(KAKAO_JS_KEY)
  }
})

const handleGoogleLogin = () => {
  const redirectUri = 'http://localhost:5173/api/auth/google/callback/'
  const oauthUrl = `https://accounts.google.com/o/oauth2/v2/auth?client_id=${CLIENT_ID}&redirect_uri=${redirectUri}&response_type=code&scope=email profile`

  window.location.href = oauthUrl
}
const handleKakaoLogin = () => {
  if (window.Kakao) {
    window.Kakao.Auth.authorize({
      redirectUri: 'http://localhost:5173/api/auth/kakao/callback/',
    })
  } else {
    console.error('❌ Kakao SDK not available')
  }
}
const socialLoginButtons = ref([
  {
    handleFunction: handleGoogleLogin,
    name: 'google',
    srcPath: googleLogo,
  },
  {
    handleFunction: handleKakaoLogin,
    name: 'kakao',
    srcPath: kakaoLogo,
  },
])

const onFormSubmit = ({ valid }) => {
  if (valid) {
  }
}
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
