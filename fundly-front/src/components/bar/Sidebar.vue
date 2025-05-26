<template>
  <nav class="side-bar collapse">
    <div class="basic-menu">
      <h3 class="menu-title">기본 메뉴</h3>
      <div class="basic-menu-list">
        <RouterLink v-for="menu in basicMenu" :key="menu.name" :to="{ name: menu.name[0] }"
          ><CustomTextButton
            :label-name="menu.labelName"
            :class-name="{ active: menu.name.includes(route.name) }"
        /></RouterLink>
      </div>
    </div>
    <div class="my-page">
      <h3 class="menu-title">마이 페이지</h3>
      <div class="my-page-list">
        <RouterLink v-for="menu in myPage" :key="menu.name" :to="{ name: menu.name[0] }"
          ><CustomTextButton
            :label-name="menu.labelName"
            :class-name="{ active: menu.name.includes(route.name) }"
        /></RouterLink>
        <CustomTextButton @click="confirmLogout" :label-name="'로그아웃'"> </CustomTextButton>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useRoute, useRouter } from 'vue-router'
import { ref } from 'vue'
import { useConfirm } from 'primevue/useconfirm'

import CustomTextButton from '@/components/button/CustomTextButton.vue'

const route = useRoute()
const router = useRouter()
const confirm = useConfirm()

const basicMenu = ref([
  {
    name: ['checkgoal', 'goaldetail'],
    labelName: '목표 확인 하기',
    path: '/',
  },
  {
    name: ['setgoal'],
    labelName: '목표 추가 하기',
    path: '/setgoal',
  },
  {
    name: ['checkproducts', 'productdetail'],
    labelName: '금융 상품 목록',
    path: '/checkproducts',
  },
  {
    name: ['recommendproducts'],
    labelName: '금융 상품 추천',
    path: '/recommendproducts',
  },
  {
    name: ['searchbank'],
    labelName: '주변 은행 찾기',
    path: '/searchbank',
  },
  {
    name: ['community', 'detail', 'writepost'],
    labelName: '커뮤니티',
    path: '/community',
  },
  {
    name: ['exchangerate'],
    labelName: '환율 계산기',
    path: '/exchangerate',
  },
])

const myPage = [
  {
    name: ['editpersonalInfo'],
    labelName: '개인 정보 변경',
    path: '/editpersonalInfo',
  },
  {
    name: ['likeproducts'],
    labelName: '찜한 상품 보기',
    path: '/likeproducts',
  },
  {
    name: ['qna'],
    labelName: '자주 묻는 질문',
    path: '/qna',
  },
]

// 로그아웃
const logout = () => {
  // 예: localStorage에 저장된 토큰 삭제
  localStorage.removeItem('access_token')
  localStorage.removeItem('refresh_token')
  localStorage.removeItem('user')

  // 로그인 페이지로 이동 (vue-router 사용 시)
  router.push({ name: 'login' })
}
const confirmLogout = () => {
  confirm.require({
    message: '로그아웃 하시겠습니까?',
    header: '확인',
    icon: 'pi pi-exclamation-triangle',
    rejectProps: {
      label: '로그인 유지 하기',
      severity: 'secondary',
      outlined: true,
    },
    acceptProps: {
      label: '로그아웃 하기',
    },
    accept: () => {
      logout()
    },
  })
}
</script>

<style scopped>
.side-bar {
  display: flex;
  flex-direction: column;
  align-items: end;
  justify-content: center;
  border-right: 0.3px solid var(--p-gray-300);
}

.menu-title {
  padding-right: 2rem;
  text-align: end;
}



.basic-menu-list,
.my-page-list {
  display: flex;
  flex-direction: column;
}

.basic-menu-list {
  width: 100%;
  margin-bottom: 4rem;
}

@media (max-width: 768px) {
  .collapse {
    display: none;
  }
}
</style>
