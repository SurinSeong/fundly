<template>
  <div v-if="data && data.length > 0" class="checkgoal-container">
    <RouterCard
      class="card-item"
      :pagename="'goaldetail'"
      :params="{ goalid: goalId }"
      :cardtitle="title"
      :isprogressbar="true"
      :isdurationmonths="true"
      :value="value"
      :durationmonths="durationmonths"
    ></RouterCard>
    <RouterCard
      class="card-item"
      :pagename="'setgoal'"
      :cardtitle="'목표 추가하기'"
      :isicon="true"
      :isprogressbar="false"
      :iconclass="'pi pi-plus'"
      :isdurationmonths="false"
      :backgroundcolor="'backgroundcolor'"
    ></RouterCard>
  </div>
  <div v-else class="checkgoal-container-none">
    <h2 class="title">
      현재 설정되어 있는 목표가 없습니다.
      <br />
      함께 목표를 설정해볼까요?
    </h2>
    <RouterLink :to="{ name: 'setgoal' }"
      ><CustomButton :label-name="'목표 설정 하기'"
    /></RouterLink>
  </div>
</template>

<script setup>
import CustomButton from "@/components/button/CustomButton.vue";
import RouterCard from "@/components/card/RouterCard.vue";
import { RouterLink } from "vue-router";
import { onMounted, ref } from "vue";
import axiosInstance from "@/api/axiosInstance";

const data = ref(null);

onMounted(async () => {
  try {
    const reponse = await axiosInstance.get("http://127.0.0.1:8000/api/goals/");
    data.value = reponse.data;
    console.log(data);
  } catch (err) {
    console.log(err);
  }
});
</script>

<style scoped>
.checkgoal-container {
  text-align: center;
  width: 100%;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  align-items: center;
}

.checkgoal-container-none {
  text-align: center;
  width: 100%;
  gap: 1rem;
  align-items: center;
}

.title {
  margin-bottom: 3rem;
}

.card-item {
  flex: 0 0 calc(20% - 1rem);
  aspect-ratio: 3/2;
  box-sizing: border-box;
}
</style>
