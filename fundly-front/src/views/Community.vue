<template>
  <div class="community-container">
    <h2>자유롭게 의견과 정보를 공유할 수 있어요.</h2>
    <CustomDataTable
      :columnInfos="columnInfos"
      :data="posts"
      :searchplaceholder="'작성자 / 제목 검색'"
      :type="'products'"
      :pageName="'detail'"
    >
    </CustomDataTable>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import CustomDataTable from '@/components/table/CustomDataTable.vue'

const posts = ref([
  {
    id: 1,
    user: '첫 번째 유저',
    title: '첫 번째 글',
    date: '2025-05-20',
    likes: 2,
  },
  {
    id: 2,
    user: '두 번째 유저',
    title: '두 번째 글',
    date: '2025-05-20',
    likes: 2,
  },
  {
    id: 3,
    user: '세 번째 유저',
    title: '세 번째 글',
    date: '2025-05-20',
    likes: 2,
  },
])

const columnNames = Object.keys(posts.value[0]).slice(1)
const columnHeader = ['작성자', '제목', '날짜', '좋아요']
let columnInfos = []

for (const idx in columnNames) {
  const columnInfo = {
    field: columnNames[idx],
    header: columnHeader[idx],
  }
  columnInfos.push(columnInfo)
}
</script>

<style scoped>
.community-container {
  width: 60%;
}
.flex {
  display: flex;
  justify-content: flex-end;
}
</style>
