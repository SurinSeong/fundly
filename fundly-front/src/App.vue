<template>
  <div class="total-container">
    <div class="side-bar collapse">
      <div class="basic-menu">
        <h3>기본 메뉴</h3>
        <div class="basic-menu-list">
          <RouterLink to="/"
            ><Button class="btn" :class="{ active: route.path === '/' }" label="목표 확인" text
          /></RouterLink>
          <RouterLink to="/setgoal"
            ><Button
              class="btn"
              :class="{ active: route.path === '/setgoal' }"
              label="목표 추가하기"
              text
          /></RouterLink>
          <RouterLink to="/checkproducts"
            ><Button
              class="btn"
              :class="{ active: route.path === '/checkproducts' }"
              label="금융 상품 확인"
              text
          /></RouterLink>
          <RouterLink to="/recommendproducts"
            ><Button
              class="btn"
              :class="{ active: route.path === '/recommendproducts' }"
              label="금융 상품 추천"
              text
          /></RouterLink>
          <RouterLink to="/searchbank"
            ><Button
              class="btn"
              :class="{ active: route.path === '/searchbank' }"
              label="주변 은행 / ATM 찾기"
              text
          /></RouterLink>
          <RouterLink to="/community"
            ><Button
              class="btn"
              :class="{ active: route.path === '/community' }"
              label="커뮤니티"
              text
          /></RouterLink>
          <RouterLink to="/exchangerate"
            ><Button
              class="btn"
              :class="{ active: route.path === '/exchangerate' }"
              label="환율 계산"
              text
          /></RouterLink>
        </div>
      </div>
      <div class="my-page">
        <h3>마이 페이지</h3>
        <div class="my-page-list">
          <RouterLink to="/edit/personalinfo"
            ><Button
              class="btn"
              :class="{ active: route.path === '/edit/personalinfo' }"
              label="개인 정보 수정"
              text
          /></RouterLink>
          <RouterLink to="/likeproducts"
            ><Button
              class="btn"
              :class="{ active: route.path === '/likeproducts' }"
              label="찜한 상품 확인"
              text
          /></RouterLink>
          <RouterLink to="/qna"
            ><Button
              class="btn"
              :class="{ active: route.path === '/qna' }"
              label="자주 묻는 질문"
              text
          /></RouterLink>
        </div>
      </div>
    </div>

    <div class="main"><RouterView /></div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useRoute } from 'vue-router'

const route = useRoute()
</script>

<style scoped>
.total-container {
  width: 95%;
  height: 95%;
  display: flex;
  border: 0.3px solid var(--p-gray-300);
  border-radius: 30px;
}

.side-bar {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 2rem;
  border-right: 0.3px solid var(--p-gray-300);
  padding-right: 2rem;
}

.main {
  height: 100%;
  width: 100%;
  display: flex;
  align-items: center;
  padding: 0 3rem 0 3rem;
}
.basic-menu-list,
.my-page-list {
  margin-left: 1rem;
  display: flex;
  flex-direction: column;
}

.basic-menu-list {
  margin-bottom: 4rem;
}

button.btn:hover {
  background-color: var(--p-indigo-50) !important;
  color: var(--p-indigo-700) !important;
}

.btn.active {
  background-color: var(--p-indigo-50);
  color: var(--p-indigo-700);
  font-weight: bold;
}

.btn:active {
  background-color: var(--p-indigo-50);
  color: var(--p-indigo-700);
}

.btn:focus {
  background-color: var(--p-indigo-50);
  color: var(--p-indigo-700);
}

@media (max-width: 768px) {
  .collapse {
    display: none;
  }

  .total-container {
    border: none;
  }
}
</style>
