<template>
  <div class="community-container">
    <h1>커뮤니티</h1>
    <DataTable :value="posts" tableStyle="min-width: 50rem">
      <Column field="user" header="작성자"></Column>
      <Column field="title" header="제목"></Column>
      <Column field="date" header="작성 날짜"></Column>
      <Column field="likes" header="좋아요"></Column>
    </DataTable>
  </div>
</template>

<script setup>
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import ColumnGroup from 'primevue/columngroup' // optional
import Row from 'primevue/row'
import { ref } from 'vue'

const posts = ref([
  {
    user: '첫 번째 유저',
    title: '첫 번째 글',
    date: '2025-05-20',
    likeUsers: 2,
  },
  {
    user: '두 번째 유저',
    title: '두 번째 글',
    date: '2025-05-20',
    likeUsers: 2,
  },
  {
    user: '세 번째 유저',
    title: '세 번째 글',
    date: '2025-05-20',
    likeUsers: 2,
  },
])
</script>

<style scoped></style>
