<template>
    <div class="latestBlog p-3 rounded-2 bg-white">
        <div id="services" class="container my-5 d-flex flex-column gap-5">
            <div class="service-headee w-50 m-auto">
                <h4 class="h1 fw-bold">Latest Blog</h4>
            </div>
            <div class="latest-body m-auto d-flex gap-3 flex-column justify-content-center align-items-center">
                <div class="d-flex gap-3 flex-wrap justify-content-center">
                    <blog-item v-for="article in articles" :key="article" :title="article.title"
                        :content="article.content" :slug="article.slug" :image="article.image"
                        class="bg-mute"></blog-item>
                </div>
                <div v-if="loading && articles != null">
                    <div class="spinner-border" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                </div>
                <div v-if="error">
                    <span><i class="ri-error-line fs-1"></i></span>
                </div>
                <div v-if="articles == null" class="border p-5 border-dark roundeds">
                    <span class="d-flex align-items-center gap-2"><i class="ri-box-3-line fs-1"></i> Empty</span>
                </div>
                <div v-if="articles == ''" class="border p-5 border-dark roundeds">
                    <span class="d-flex align-items-center gap-2"><i class="ri-box-3-line fs-1"></i> Empty</span>
                </div>
                <primary-button class="mt-5" title="Explore More" url="/blog/articles" v-if="articles"></primary-button>
            </div>
        </div>
    </div>
</template>

<script>
import BlogItem from './blog_components/BlogItem.vue';
import axios from 'axios';
import PrimaryButton from './buttons_components/PrimaryButton.vue';
export default {
    name: "LatestBlug",
    components: {
        'blog-item': BlogItem,
        'primary-button': PrimaryButton,
    },
    data() {
        return {
            articles: null,
            error: false,
            loading: true,
            domain: this.$store.state.domain
        }
    },
    mounted() {
        axios.get(`${this.domain}/api/v1/blog/articles/?limit=3`)
            .then(response => this.articles = response.data)
            .catch(() => this.error = true)
            .finally(() => this.loading = false)
    },
    watch: {
        $route() {
            axios.get(`${this.domain}/api/v1/blog/articles/?limit=3`)
                .then(response => this.articles = response.data)
                .catch(() => this.error = true)
                .finally(() => this.loading = false)
        }
    },
}
</script>