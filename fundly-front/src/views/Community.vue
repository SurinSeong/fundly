<template>
  <div class="community-container">
    <h2>자유롭게 의견과 정보를 공유할 수 있어요.</h2>
    <DataTable
      v-model:filters="filters"
      :value="posts"
      paginator
      :rows="5"
      :rowsPerPageOptions="[5, 10, 20, 50]"
      tableStyle="width: 100%;"
      :globalFilterFields="['user', 'title']"
    >
      <template #header>
        <div class="flex">
          <IconField>
            <InputIcon>
              <i class="pi pi-search" />
            </InputIcon>
            <InputText v-model="filters['global'].value" placeholder="작성자 / 제목 검색" />
          </IconField>
        </div>
      </template>
      <Column field="user" header="작성자"> </Column>
      <Column field="title" header="제목">
        <template #body="slotProps">
          <RouterLink :to="{ name: 'detail', params: { id: slotProps.data.id } }">
            <Button :label="slotProps.data.title" text />
          </RouterLink>
        </template>
      </Column>
      <Column field="date" header="작성 날짜"></Column>
      <Column field="likes" header="좋아요"></Column>
    </DataTable>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import InputText from 'primevue/inputtext'
import IconField from 'primevue/iconfield'
import InputIcon from 'primevue/inputicon'
import { FilterMatchMode } from '@primevue/core/api'
import ColumnGroup from 'primevue/columngroup' // optional
import Row from 'primevue/row'
import { ref } from 'vue'

const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
  title: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
  user: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
})
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
</script>

<style scoped>
.community-container {
  width: 100%;
}
.flex {
  display: flex;
  justify-content: flex-end;
}
</style>
