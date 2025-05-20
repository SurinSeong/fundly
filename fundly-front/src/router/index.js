import CheckGoal from '@/views/CheckGoal.vue'
import CheckProducts from '@/views/CheckProducts.vue'
import Community from '@/views/Community.vue'
import EditPersonalInfo from '@/views/EditPersonalInfo.vue'
import ExchangeRate from '@/views/ExchangeRate.vue'
import LikeProducts from '@/views/LikeProducts.vue'
import Login from '@/views/Login.vue'
import QnA from '@/views/QnA.vue'
import RecommendProducts from '@/views/RecommendProducts.vue'
import SearchBank from '@/views/SearchBank.vue'
import SetGoal from '@/views/SetGoal.vue'
import Signup from '@/views/Signup.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'checkgoal',
      component: CheckGoal,
    },
    {
      path: '/checkproducts',
      name: 'checkproducts',
      component: CheckProducts,
    },
    {
      path: '/community',
      name: 'community',
      component: Community,
    },
    {
      path: '/edit/personalinfo',
      name: 'editpersonalInfo',
      component: EditPersonalInfo,
    },
    {
      path: '/exchangerate',
      name: 'exchangerate',
      component: ExchangeRate,
    },
    {
      path: '/likeproducts',
      name: 'likeproducts',
      component: LikeProducts,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/qna',
      name: 'qna',
      component: QnA,
    },
    {
      path: '/recommendproducts',
      name: 'recommendproducts',
      component: RecommendProducts,
    },
    {
      path: '/searchbank',
      name: 'searchbank',
      component: SearchBank,
    },
    {
      path: '/setgoal',
      name: 'setgoal',
      component: SetGoal,
    },
    {
      path: '/signup',
      name: 'signup',
      component: Signup,
    },
  ],
})

export default router
