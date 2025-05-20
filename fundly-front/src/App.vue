<template>
  <div class="container">
    <div class="side-bar">
      <div class="basic-menu">
        <h4>기본 메뉴</h4>
        <div class="basic-menu-list">
          <RouterLink to="/"><Button label="목표 확인" variant="text" /></RouterLink>
          <RouterLink to="/setgoal"><Button label="목표 추가하기" variant="text" /></RouterLink>
          <RouterLink to="/checkproducts"><Button label="금융 상품 확인" variant="text" /></RouterLink>
          <RouterLink to="/recommendproducts"><Button label="금융 상품 추천" variant="text" /></RouterLink>
          <RouterLink to="/searchbank"
            ><Button label="주변 은행 / ATM 찾기" variant="text"
          /></RouterLink>
          <RouterLink to="/community"><Button label="커뮤니티" variant="text" /></RouterLink>
          <RouterLink to="/exchangerate"><Button label="환율 계산" variant="text" /></RouterLink>
        </div>
      </div>
      <div class="my-page">
        <h4>마이 페이지</h4>
        <div class="my-page-list">
          <RouterLink to="/edit/personalinfo"
            ><Button label="개인 정보 수정" variant="text"
          /></RouterLink>
          <RouterLink to="/likeproducts"
            ><Button label="찜한 상품 확인" variant="text"
          /></RouterLink>
          <RouterLink to="/qna"><Button label="자주 묻는 질문" variant="text" /></RouterLink>
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
.container {
  height: 100%;
  display: flex;
  border: 0.3px solid;
  border-radius: 30px;
}

.side-bar {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 2rem;
  border-right: 0.3px solid;
  padding-right: 2rem;
}

.basic-menu-list,
.my-page-list {
  margin-left: 1rem;
  display: flex;
  flex-direction: column;
}

.basic-menu-list {
}
</style>
