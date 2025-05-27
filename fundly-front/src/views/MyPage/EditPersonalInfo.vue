<template>
  <div class="editpersonalinfo-container">
    <h1>개인 정보 수정</h1>
    <CustomButton label-name="비밀번호 변경하기" :justify="'home'" @click="handleEditPassword" />
    <Form style="width: 100%">
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
      <h3>재직 여부를 선택해주세요.</h3>

      <div class="job mb-2">
        <Select v-model="selectedJob" :options="job" placeholder="재직 여부" fluid=""></Select>
        <CustomInputNumber
          v-model="assets"
          :input-id="'assets'"
          :label-name="'현재 자산현황을 입력해주세요.'"
          input-placeholder="단위 : 만원"
          :is-icon="true"
          :icon-class="'pi pi-wallet'"
        />
        <CustomInputNumber
          v-model="salary"
          :input-id="'salary'"
          :label-name="'현재 급여를 입력해주세요.'"
          input-placeholder="단위 : 만원"
          :is-icon="true"
          :icon-class="'pi pi-money-bill'"
        />
      </div>
      <div class="finanacial-status mb-2">
        <h3>현재 자산 현황을 선택해주세요.</h3>
        <Select
          v-model="selectedFinancialStatus"
          :options="assetRange"
          placeholder="자산 현황"
          fluid=""
        ></Select>
      </div>
      <div class="salary mb-2">
        <h3>현재 급여를 선택해주세요.</h3>
        <Select
          v-model="selectedSalary"
          :options="moneyRange"
          placeholder="급여"
          fluid=""
        ></Select>
      </div>
      <br />
      <CustomButton label-name="수정하기" :justify="'end'" @click="handleEditPersonalInfo" />
    </Form>
  </div>
</template>

<script setup>
import { Form } from '@primevue/forms'
import CustomInputText from '@/components/input/CustomInputText.vue'
import CustomInputNumber from '@/components/input/CustomInputNumber.vue'
import CustomButton from '@/components/button/CustomButton.vue'
import axiosInstance from '@/api/axiosInstance'
import DatePicker from 'primevue/datepicker'
import Select from 'primevue/select'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()


  const username = ref("")
  const birthDate = ref(null)
  const assetRange = ref(['1,000만원 미만', '1,000만원 이상 3,000만원 미만', '3,000만원 이상 5,000만원 미만', '5,000만원 이상 1억 미만', '1억 이상'])
  const moneyRange = ref(["100만원 미만", "100만원 이상 200만원 미만", "200만원 이상 300만원 미만", "300만원 이상 400만원 미만", "400만원 이상 500만원 미만", "500만원 이상"]);
  const job = ref([
    '직장인',
    '공무원',
    '군인',
    '전문직',
    '학생',
    '취업준비생',
    '자영업자',
    '프리랜서',
    '예술가/창작자',
    '주부',
    '은퇴자',
    '무직'
  ]
  );
  
  const selectedJob = ref("");
  const selectedFinancialStatus = ref("");
  const selectedSalary = ref("");

onMounted(async () => {
  const response = await axiosInstance.get('http://127.0.0.1:8000/api/user/profile/')
  console.log(response)


    username.value = response.data.username
    birthDate.value = response.data.birth_date
    selectedJob.value = response.data.work_type
    selectedFinancialStatus.value = response.data.assets
    selectedSalary.value = response.data.salary

  })

  const handleEditPersonalInfo = async () => {
    try {
        const response = await axiosInstance.put(
            "http://127.0.0.1:8000/api/user/profile/",
            {
                username: username.value,
                birth_date: new Date(birthDate.value).toISOString().split('T')[0],
                work_type: selectedJob.value,
                assets: selectedFinancialStatus.value,
                salary: selectedSalary.value,
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

})


const handleEditPersonalInfo = async () => {
  try {
    const response = await axiosInstance.put('http://127.0.0.1:8000/api/user/profile/', {
      username: username.value,
      birth_date: new Date(birthDate.value).toISOString().split('T')[0],
      work_type: selectedJob.value,
      assets: assets.value,
      salary: salary.value,
    })
    alert('수정 완료')
    router.push('/')
  } catch (err) {
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
.editpersonalinfo-container {
  width: 100%;
}

.date-picker {
  display: flex;
  gap: 1rem;
}

.job {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  justify-content: center;
}
</style>
