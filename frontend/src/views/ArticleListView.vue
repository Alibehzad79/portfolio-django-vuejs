<template>
    <div class="project-view container p-5">
        <div class="mt-5 d-flex flex-column m-auto gap-2">
            <h6 class="fw-bold h1 mb-5">Blog</h6>
            <div class="projects d-flex flex-column flex-md-row flex-wrap gap-4" v-if="data">
                <blog-item v-for="article in data" :key="article" :title="article.title" :content="article.content"
                    :slug="article.slug" :image="article.image" class="bg-white"></blog-item>
            </div>
            <div v-if="loading && data != null">
                <div class="spinner-border" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
            </div>
            <div v-if="error">
                <span><i class="ri-error-line fs-1"></i></span>
            </div>
            <div v-if="data == null" class="border p-5 border-dark rounded">
                <span class="d-flex align-items-center gap-2"><i class="ri-box-3-line fs-1"></i> Empty</span>
            </div>
        </div>
    </div>
</template>

<script>
import BlogItem from '@/components/blog_components/BlogItem.vue';
import axios from 'axios';

export default {
    name: "ArticleList",
    components: {
        "blog-item": BlogItem,
    },
    data() {
        return {
            data: null,
            loading: true,
            error: false,
            domain: this.$store.state.domain
        }
    },
    mounted() {
        axios.get(`${this.domain}/api/v1/blog/articles/`)
            .then(response => this.data = response.data)
            .catch(() => this.error = true)
            .finally(() => this.loading = false)
    },
    watch: {
        $route() {
            axios.get(`${this.domain}/api/v1/blog/articles/`)
                .then(response => this.data = response.data)
                .catch(() => this.error = true)
                .finally(() => this.loading = false)
        }
    }
}
</script>