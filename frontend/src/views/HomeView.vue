<template>
  <div class="home">
    <MainSlide />
    <MyServices />
    <LatestProject />
  </div>
</template>

<script>
// @ is an alias to /src
import MainSlide from '@/components/MainSlide.vue'
import MyServices from '@/components/MyServices.vue'
import LatestProject from '@/components/LatestProject.vue'

export default {
  name: 'HomeView',
  components: {
    MainSlide,
    MyServices,
    LatestProject,
  }
}
</script>
