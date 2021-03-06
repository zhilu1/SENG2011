export default [
  {
    path: "/profile",
    name: "ProfileDetail",
    component: () => import("@/views/profile/Detail.vue"),
    props: { default: true }
  },
  {
    path: "/profile/edit",
    name: "ProfileEdit",
    component: () => import("@/views/auth/Register.vue")
  }
];
