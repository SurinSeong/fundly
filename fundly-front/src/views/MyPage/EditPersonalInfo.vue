<template>
  <div class="editpersonalinfo-container">
    <h1>개인 정보 수정</h1>
    <CustomButton
      label-name="비밀번호 변경하기"
      :justify="'home'"
      @click="handleEditPassword"
    />
    <Form style="width: 100%;">
      <CustomInputText
        v-model="username"
        :input-id="'user-id'"
        :label-name="'수정하실 닉네임을 입력해주세요.'"
        :is-icon="true"
        :icon-class="'pi pi-star'"
      />
      <div class="birth-date">
        <h3>생년월일을 입력해주세요</h3>
        <div class="date-picker">
          <DatePicker
            placeholder="ex) 2025/05/28"
            date-format="yy/mm/dd"
            v-model="birthDate"
            showButtonBar
          />
        </div>
      </div>
      <div class="job mb-2">
        <h3>재직 여부를 선택해주세요.</h3>
        <Select
          v-model="selectedJob"
          :options="job"
          placeholder="재직 여부"
          fluid=""
        ></Select>
      </div>
      <CustomInputNumber
        v-model="assets"
        :input-id="'assets'"
        :label-name="'현재 자산현황을 입력해주세요.'"
        input-placeholder="단위 : 만원"
        :is-icon="true"
        :icon-class="'pi pi-star'"
      />
      <CustomInputNumber
        v-model="salary"
        :input-id="'salary'"
        :label-name="'현재 급여를 입력해주세요.'"
        input-placeholder="단위 : 만원"
        :is-icon="true"
        :icon-class="'pi pi-star'"
      />
      <br />
      <CustomButton
        label-name="수정하기"
        :justify="'end'"
        @click="handleEditPersonalInfo"
      />
    </Form>
  </div>
</template>

<script setup>
  import { Form } from '@primevue/forms';
  import CustomInputText from '@/components/input/CustomInputText.vue';
  import CustomInputNumber from "@/components/input/CustomInputNumber.vue";
  import CustomButton from '@/components/button/CustomButton.vue';
  import axiosInstance from '@/api/axiosInstance';
  import DatePicker from "primevue/datepicker";
  import Select from "primevue/select";
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';

  const router = useRouter()

  const username = ref("")
  const birthDate = ref(null)
  const assets = ref(0)
  const salary = ref(0)
  const job = ref(['학생', '직장인', '']);
  const selectedJob = ref("");

  onMounted(async () => {
    const response = await axiosInstance.get(
        "http://127.0.0.1:8000/api/user/profile/",
    )
    console.log(response)

    username.value = response.data.username
    birthDate.value = response.data.birth_date
    selectedJob.value = response.data.work_type
    assets.value = response.data.assets
    salary.value = response.data.salary

  })
  const handleEditPersonalInfo = async () => {
    try {
        const response = await axiosInstance.put(
            "http://127.0.0.1:8000/api/user/profile/",
            {
                username: username.value,
                birth_date: birthDate.value.toISOString().split('T')[0],
                work_type: workType.value,
                assets: assets.value,
                salary: salary.value,
            }
        )
        alert('수정 완료')
        router.push('/')
    }
    catch (err) {
        console.error(err)
        alert('수정 실패')
        router.push('/edit/personalinfo')
    }
  }

  const handleEditPassword = () => {
    router.replace('/edit/password')
  }

</script>

<style scoped>
.date-picker {
  display: flex;
  gap: 1rem;
}
</style>