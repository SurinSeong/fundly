import CheckGoal from '@/views/CheckGoal.vue'
import CheckProducts from '@/views/CheckProducts.vue'
import Community from '@/views/Community.vue'
import CommunityDetail from '@/views/CommunityDetail.vue'
import EditPersonalInfo from '@/views/EditPersonalInfo.vue'
import ExchangeRate from '@/views/ExchangeRate.vue'
import GoalDetail from '@/views/GoalDetail.vue'
import GoalProductDetail from '@/views/GoalProductDetail.vue'
import LikeProducts from '@/views/LikeProducts.vue'
import Login from '@/views/Login.vue'
import ProductDetail from '@/views/ProductDetail.vue'
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
      path: '/checkgoal/:goalid',
      name: 'goaldetail',
      component: GoalDetail,
    },
    {
      path: '/checkgoal/:goalid/:userid/:product',
      name: 'goalproductdetail',
      component: GoalProductDetail,
    },
    {
      path: '/checkproducts',
      name: 'checkproducts',
      component: CheckProducts,
    },
    {
      path: '/checkproducts/:productid',
      name: 'productdetail',
      component: ProductDetail,
    },
    {
      path: '/community',
      name: 'community',
      component: Community,
    },
    {
      path: '/community/detail/:id',
      name: 'detail',
      component: CommunityDetail,
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

// router.beforeEach((to, from, next) => {
//   const isLoggedIn = !!localStorage.getItem('accessToken')
//   const publicPages = ['/login', '/signup']

//   if (!isLoggedIn && !publicPages.includes(to.path)) {
//     next('/login')
//   } else {
//     next()
//   }
// })

export default router
