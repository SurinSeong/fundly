<template>
    <RouterView />
</template>
<script setup>

import { useRoute, useRouter } from 'vue-router';
import { onMounted } from 'vue';

const route = useRoute()
const router = useRouter()

onMounted(() => {
    console.log(route.query)
    const access = route.query.access
    const refresh = route.query.refresh
    const user = route.query.user

    console.log(access)

    if (access && refresh) {
        localStorage.setItem('access_token', access)
        localStorage.setItem('refresh_token', refresh)
        localStorage.setItem('user', user)
        router.push('/')    // 홈으로 이동
    }
    else {
        alert('로그인 실패')
        router.push('/login')
    }
})

</script>