<template>
  <div class="detail-container">
    <h2>{{ title }}</h2>
    <div class="detail-data">
      <h4>작성 일자: {{ date }}</h4>
      <h4>작성자: {{ writer }}</h4>
    </div>
    <article class="content">
      {{ content }}
    </article>
  </div>
</template>

<script setup>
import { ref } from "vue";

const title = ref("제목");
const date = ref("작성 일자");
const writer = ref("작성자");
const content = ref("작성 내용");
</script>

<style scoped>
.detail-container {
  width: 100%;
  height: 70%;
}

.detail-data {
  width: 100%;
  border-top: 0.1px solid var(--p-primary-50);
  border-bottom: 0.1px solid var(--p-primary-50);
}

.content {
  margin: 2rem;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  box-sizing: content-box;
  margin: 1rem;
  padding: 0;
}
</style>
