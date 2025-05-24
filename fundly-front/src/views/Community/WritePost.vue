<template>
  <div class="writepost-container">
    <h2>게시글 작성</h2>
    <div class="selet-category">
      <Select
        v-model="category"
        placeholder="말머리 선택"
        :options="categories"
      ></Select>
    </div>
    <div class="post-title">
      <CustomInputText v-model="title" input-placeholder="게시글 제목">
      </CustomInputText>
    </div>
    <div class="post-content">
      <Textarea
        placeholder="게시글 내용"
        fluid=""
        v-model="content"
        style="height: 100%;"
      >
      </Textarea>
    </div>

    <CustomButton label-name="작성하기" :justify="'end'" @click="writePost" />
  </div>
</template>

<script setup>
import { ref } from "vue";
import Textarea from "primevue/textarea";
import Select from "primevue/select";
import CustomInputText from "@/components/input/CustomInputText.vue";
import CustomButton from "@/components/button/CustomButton.vue";
import axiosInstance from "@/api/axiosInstance";
import { useRouter } from "vue-router";

const title = ref("");
const content = ref("");
const category = ref("");
const categories = ref(["금융 상품 문의", "자유"]);
const router = useRouter();

const writePost = async () => {
  try {
    const response = await axiosInstance.post(
      "http://127.0.0.1:8000/api/community/",
      {
        title: title.value,
        content: content.value,
        category: category.value
      }
    );
    router.push("/community");
  } catch (error) {}
};
</script>

<style scopped>
.writepost-container {
  width: 60%;
  height: 70%;
}
.post-title,
.post-content {
  margin-bottom: 1rem;
}

.post-content {
  width: 100%;
  height: 50%;
}
</style>
