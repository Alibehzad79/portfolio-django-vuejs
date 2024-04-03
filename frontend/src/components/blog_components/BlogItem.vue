<template>
    <div class="blog-item d-flex flex-column gap-2 p-3 bg-mute text-start rounded-3 col-md-3" @click="getUrl">
        <img :src="domain + image" alt="Article Title" class="img-fluid blog-item-img">
        <h6 class="fw-bold blog-title">{{ title }}</h6>
        <p class="text-secondary blog-content" v-html="content"></p>
        <a href="#" class="nav-link">Read More <i class="ms-1 ri-arrow-right-line"></i></a>
    </div>

</template>

<script>
export default {
    name: "BlogItem",
    props: ['title', 'content', 'image', 'slug'],
    data() {
        return {
            domain: "http://127.0.0.1:8000"
        }
    },
    methods: {
        getUrl(){
            this.$router.push(this.slug)
        }
    }
}
</script>