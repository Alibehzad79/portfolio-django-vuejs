<template>
    <div class="blog-item d-flex flex-column gap-2 p-3 text-start rounded-3 col-md-5 col-lg-3 m-auto" @click="getUrl">
        <img :src="domain + image" alt="Article Title" class="img-fluid blog-item-img">
        <h6 class="fw-bold blog-title">{{ title }}</h6>
        <p class="text-secondary blog-content" v-html="content"></p>
        <a class="nav-link">Read More <i class="ms-1 ri-arrow-right-line"></i></a>
    </div>

</template>

<script>
export default {
    name: "BlogItem",
    props: ['title', 'content', 'image', 'slug'],
    data() {
        return {
            domain: this.$store.state.domain
        }
    },
    methods: {
        getUrl() {
            this.$router.push('/blog/articles/' + this.slug)
        }
    }
}
</script>