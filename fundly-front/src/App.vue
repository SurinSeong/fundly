<template>
  <div class="container">
    <div class="side-bar">
      <div class="basic-menu">
        <h3>기본 메뉴</h3>
        <div class="basic-menu-list">
          <RouterLink to="/"><Button label="목표 확인" text /></RouterLink>
          <RouterLink to="/setgoal"><Button label="목표 추가하기" text /></RouterLink>
          <RouterLink to="/checkproducts"><Button label="금융 상품 확인" text /></RouterLink>
          <RouterLink to="/recommendproducts"><Button label="금융 상품 추천" text /></RouterLink>
          <RouterLink to="/searchbank"
            ><Button label="주변 은행 / ATM 찾기" text
          /></RouterLink>
          <RouterLink to="/community"><Button label="커뮤니티" text /></RouterLink>
          <RouterLink to="/exchangerate"><Button label="환율 계산" text /></RouterLink>
        </div>
      </div>
      <div class="my-page">
        <h3>마이 페이지</h3>
        <div class="my-page-list">
          <RouterLink to="/edit/personalinfo"
            ><Button label="개인 정보 수정" text
          /></RouterLink>
          <RouterLink to="/likeproducts"
            ><Button label="찜한 상품 확인" text
          /></RouterLink>
          <RouterLink to="/qna"><Button label="자주 묻는 질문" text /></RouterLink>
        </div>
      </div>
    </div>

    <div class="main"><RouterView /></div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
button {
  
}
.container {
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

.basic-menu-list,
.my-page-list {
  margin-left: 1rem;
  display: flex;
  flex-direction: column;
}

.basic-menu-list {
  margin-bottom: 4rem;
}
</style>
