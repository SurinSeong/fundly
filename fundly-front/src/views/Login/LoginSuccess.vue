<template>
    <RouterView />
</template>
<script setup>

import { useRoute, useRouter } from 'vue-router';
import { onMounted } from 'vue';
import axiosInstance from '@/api/axiosInstance';

const route = useRoute()
const router = useRouter()

onMounted(async () => {
    console.log(route.query)
    const access = route.query.access
    const refresh = route.query.refresh
    const user = route.query.user

    console.log(access)

    if (access && refresh) {
        localStorage.setItem('access_token', access)
        localStorage.setItem('refresh_token', refresh)
        localStorage.setItem('user', user)

        const response = await axiosInstance.get(
            "http://127.0.0.1:8000/api/user/first-login/"
        )

        if (response.data.message) {
            alert("닉네임을 수정해주세요!")
            router.push('/edit/personalinfo')    // 개인 정보 수정페이지로 이동
        }
        else {
            router.push('/')
        }
    }
    else {
        alert('로그인 실패')
        router.push('/login')
    }
})

</script>