<template>
  <div class="social-btn-container" :class="socialname">
    <a href="" class="social">
      <img :src="srcpath" alt="" />
    </a>
  </div>
</template>

<script setup>
defineProps({
  socialname: String,
  srcpath: String
});
</script>

<style scopped>
.social-btn-container {
  background-color: var(--p-primary-50);
  padding: 0.7rem 0.7rem 0.5rem 0.7rem;
  border-radius: 100%;
}

.kakao {
  background-color: #fee500;
}
img {
  height: 2rem;
  width: 2rem;
}
</style>
