<!-- GoalDetail.vue -->
<template>
  <div class="goaldetail-container">
    <div class="top">
      <h1>{{ goalData.goal_name }}</h1>
      <h3>시작이 반, 조금 더 힘내봐요!</h3>
      <div class="chart-container">
        <Chart
          type="bar"
          :data="chartData"
          :options="chartOptions"
          class="h-[30rem]"
          indexAxis="y"
          fluid
        />
      </div>
    </div>
    <div class="bottom">
      <div class="goal-products">
        <Carousel :value="goalProducts" circular="">
          <template #item="slotProps">
            <RouterCard
              class="card-item"
              :page-name="'goalproductdetail'"
              :params="{
                goalid: slotProps.data.goal,
                userid: slotProps.data.user,
                product:
                  slotProps.data.finance_product ??
                  slotProps.data.additional_product
              }"
              :is-progressbar="true"
              :is-duration-months="true"
              :start-date="slotProps.data.start_date"
              :card-title="slotProps.data.title"
              :value="
                (slotProps.data.current_amount / slotProps.data.target_amount) *
                  100
              "
              :duration-months="slotProps.data.duration_months"
            ></RouterCard>
          </template>
        </Carousel>
      </div>
      <div class="recommendation">
        <h3 class="title">금융 상품 추천</h3>
        <RouterLink
          v-for="product in productList"
          :key="product.id"
          :to="{ name: 'productdetail', params: { productid: product.id } }"
        >
          <CustomTextButton :label-name="product.title">
            {{ product.title }}
          </CustomTextButton>
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { RouterLink } from "vue-router";
import Chart from "primevue/chart";
import RouterCard from "@/components/card/RouterCard.vue";
import CustomTextButton from "@/components/button/CustomTextButton.vue";
import Carousel from "primevue/carousel";
import axiosInstance from "@/api/axiosInstance";

const route = useRoute();

const goalId = route.params.goalid;

const goalData = ref({});
const totalTargetAmount = ref(0);
onMounted(async () => {
  try {
    const response = await axiosInstance.get(
      `http://127.0.0.1:8000/api/goals/${goalId}`
    );
    goalData.value = response.data;
    totalTargetAmount.value = goalData.value.total_target_amount;
    console.log(totalTargetAmount.value);

    chartData.value = setChartData();
    chartOptions.value = setChartOptions();
  } catch (error) {
    console.log(error);
  }
});

const chartData = ref();
const chartOptions = ref();

const setChartData = () => {
  const documentStyle = getComputedStyle(document.documentElement);

  return {
    labels: ["2025-04", "2025-05", "2025-06"],
    datasets: [
      {
        type: "bar",
        label: "적금",
        backgroundColor: documentStyle.getPropertyValue("--p-indigo-700"),
        data: [50, 25, 12, 48, 90, 76, 42]
      },
      {
        type: "bar",
        label: "예금",
        backgroundColor: documentStyle.getPropertyValue("--p-indigo-500"),
        data: [21, 84, 24, 75, 37, 65, 34]
      },
      {
        type: "bar",
        label: "그 외",
        backgroundColor: documentStyle.getPropertyValue("--p-indigo-300"),
        data: [41, 52, 24, 74, 23, 21, 32]
      }
    ]
  };
};
const setChartOptions = () => {
  const documentStyle = getComputedStyle(document.documentElement);
  const textColor = documentStyle.getPropertyValue("--p-text-color");
  const textColorSecondary = documentStyle.getPropertyValue(
    "--p-text-muted-color"
  );
  const surfaceBorder = documentStyle.getPropertyValue(
    "--p-content-border-color"
  );

  return {
    indexAxis: "y",
    maintainAspectRatio: false,
    aspectRatio: 0.8,
    plugins: {
      tooltips: {
        mode: "index",
        intersect: false
      },
      legend: {
        labels: {
          color: textColor
        }
      }
    },
    scales: {
      x: {
        stacked: true,
        ticks: {
          color: textColorSecondary
        },
        grid: {
          color: surfaceBorder
        },
        max: totalTargetAmount.value
      },
      y: {
        stacked: true,
        ticks: {
          color: textColorSecondary
        },
        grid: {
          color: surfaceBorder
        }
      }
    }
  };
};

const deposit = ref([
  {
    id: 1,
    goal: 1,
    user: 1,
    title: "싸피 청년 우대 예금",
    finance_product: 1,
    additional_product: null,
    option_product: 1,
    target_amount: 500,
    current_amount: 200,
    duration_months: 12,
    start_date: "2025-05-24"
  },
  {
    id: 2,
    goal: 1,
    user: 1,
    title: "예금 2",
    finance_product: null,
    additional_product: 2,
    option_product: 1,
    target_amount: 500,
    current_amount: 200,
    duration_months: 12,
    start_date: "2025-05-24"
  },
  {
    id: 3,
    goal: 1,
    user: 1,
    title: "예금 3",
    finance_product: 3,
    additional_product: null,
    option_product: 1,
    target_amount: 500,
    current_amount: 200,
    duration_months: 12,
    start_date: "2025-05-24"
  }
]);
const saving = ref([
  {
    id: 4,
    goal: 1,
    user: 1,
    title: "적금 4",
    finance_product: 3,
    additional_product: null,
    option_product: 1,
    target_amount: 600,
    current_amount: 300,
    duration_months: 12,
    start_date: "2025-05-24"
  }
]);
const goal = ref({
  title: "유학 자금 마련하기",
  target_amount: 2000,
  current_amount: 500,
  saving: 200,
  deposit: 300,
  saving: saving,
  deposit: deposit
});

const goalProducts = goal.value.deposit.concat(goal.value.saving);

const productList = ref([
  {
    id: 1,
    goal: 1,
    user: 1,
    title: "추천 1",
    finance_product: 1,
    additional_product: null,
    option_product: 1,
    target_amount: 500,
    current_amount: 200,
    duration_months: 12,
    start_date: "2025-05-24"
  },
  {
    id: 2,
    goal: 1,
    user: 1,
    title: "추천 2",
    finance_product: null,
    additional_product: 2,
    option_product: 1,
    target_amount: 500,
    current_amount: 200,
    duration_months: 12,
    start_date: "2025-05-24"
  },
  {
    id: 3,
    goal: 1,
    user: 1,
    title: "추천 3",
    finance_product: 3,
    additional_product: null,
    option_product: 1,
    target_amount: 500,
    current_amount: 200,
    duration_months: 12,
    start_date: "2025-05-24"
  }
]);
</script>

<style scopped>
.goaldetail-container {
  width: 60%;
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: space-between;
}

.top {
  width: 100%;
}
.chart-container {
  width: 100%;
  margin: 1rem 0 1rem 0;
}
.title {
  text-align: center;
}
.card-item {
  flex: 0 0 calc(33.33% - 1rem);
}

.bottom {
  width: 100%;
  display: flex;
  gap: 1rem;
}

.goal-products {
  width: 65%;
}
.recommendation {
  width: 35%;
}
</style>
