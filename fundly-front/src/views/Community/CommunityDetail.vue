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
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import axiosInstance from "@/api/axiosInstance";

const route = useRoute();
const id = route.params.id;

const title = ref("제목");
const date = ref("작성 일자");
const writer = ref("작성자");
const content = ref("작성 내용");
onMounted(async () => {
  try {
    const response = await axiosInstance.get(
      `http://127.0.0.1:8000/api/community/${id}`
    );
    const post = response.data;
    title.value = post.title;
    date.value = post.created_at.split("T")[0]; // 날짜만 추출
    writer.value = post.user; // user가 username 문자열이라면
    content.value = post.content;
  } catch (err) {
    console.log(err);
  }
});
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
