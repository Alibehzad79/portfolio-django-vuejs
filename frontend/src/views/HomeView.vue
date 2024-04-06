<template>
  <div class="home">
    <MainSlide />
    <MyServices />
    <LatestProject />
    <MyResume id="resume" />
    <LatestBlog />
    <ContactUsComponent id="contact" />
  </div>
</template>

<script>
// @ is an alias to /src
import MainSlide from '@/components/MainSlide.vue'
import MyServices from '@/components/MyServices.vue'
import LatestProject from '@/components/LatestProject.vue'
import LatestBlog from '@/components/LatestBlog.vue'
import MyResume from '@/components/MyResume.vue'
import ContactUsComponent from '@/components/ContactUsComponent.vue'
export default {
  name: 'HomeView',
  components: {
    MainSlide,
    MyServices,
    LatestProject,
    LatestBlog,
    MyResume,
    ContactUsComponent,
  }
}
</script>
