<template>
  <div class="signup-container">
    <h1>회원가입</h1>
    <Form style="width: 100%">
      <CustomInputText
        v-model="username"
        :input-id="'user-id'"
        :label-name="'사용하실 닉네임을 입력해주세요.'"
        :isicon="true"
        :iconclass="'pi pi-star'"
      />
      <CustomInputText
        v-model="email"
        :input-id="'email'"
        :label-name="'로그인에 사용될 이메일 주소를 알려주세요.'"
        :isicon="true"
        :iconclass="'pi pi-star'"
      />
      <CustomInputText
        v-model="password"
        :input-id="'password'"
        :label-name="'사용하실 비밀번호를 입력해주세요.'"
        :input-type="'password'"
        :isicon="true"
        :iconclass="'pi pi-star'"
      />
      <CustomInputText
        v-model="passwordConfirm"
        :input-id="'password-confirm'"
        :label-name="'사용하실 비밀번호를 확인해주세요.'"
        :isicon="true"
        :input-type="'password'"
        :iconclass="'pi pi-star'"
        :error="error"
        :message="message"
      />
      <br />
      <CustomButton label-name="가입하기" :justify="'end'" @click="handleSignup" />
    </Form>
  </div>
</template>

<script setup>
import { Form } from '@primevue/forms'
import CustomInputText from '@/components/input/CustomInputText.vue'
import CustomButton from '@/components/button/CustomButton.vue'
import axiosInstance from '@/api/axiosInstance'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
const router = useRouter()

const username = ref('')
const password = ref('')
const passwordConfirm = ref('')
const email = ref('')
const error = ref(false)
const message = ref('')

const handleSignup = async () => {
  if (password.value != passwordConfirm.value) {
    error.value = true
    message.value = '비밀번호가 일치하지 않습니다. 다시 한 번 확인해주세요.'
  } else {
    error.value = false
    try {
      const res = await axiosInstance.post('http://127.0.0.1:8000/api/auth/signup/', {
        username: username.value,
        email: email.value,
        password1: password.value,
        password2: passwordConfirm.value,
      })

      const { access, refresh, user } = res.data

      // 토큰을 localStorage에 저장
      localStorage.setItem('access_token', access)
      localStorage.setItem('refresh_token', refresh)

      // 로그인 완료
      console.log(access)
      router.push('/')
    } catch (err) {
      console.error('⛔ 회원가입:', err.response?.data || err)
      alert('회원가입 실패')
      router.push('/signup')
    }
  }
}
</script>

<style scoped>
.signup-container {
  width: 30%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
