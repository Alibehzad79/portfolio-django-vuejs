<template>
    <div class="article-detail container m-auto">
        <div class="text-start p-2 mt-5" v-if="data">
            <span class="text-warning text-dark mb-2 rounded-5 badge p-2">{{ data.date_created }}</span>
            <div class="d-flex text-start flex-column gap-3">
                <h1 class="fw-bold">{{ data.title }}</h1>
                <img :src="domain + data.image" alt="title" class="img-fluid article-img rounded-5">
                <div class="content" v-html="data.content">
                </div>
            </div>
        </div>
        <div v-if="loading && data != null">
            <div class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>
        <div v-if="error">
            <span><i class="ri-error-line fs-1"></i></span>
        </div>
        <div v-if="data == null" class="border p-5 border-dark rounded my-5">
            <span class="d-flex align-items-center gap-2"><i class="ri-box-3-line fs-1"></i> Empty</span>
        </div>
        <div v-if="data == ''" class="border p-5 border-dark roundeds">
                    <span class="d-flex align-items-center gap-2"><i class="ri-box-3-line fs-1"></i> Empty</span>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "ArticleDetail",

    data() {
        return {
            data: null,
            loading: true,
            error: false,
            domain: this.$store.state.domain
        }
    },
    mounted() {
        var slug = this.$route.params.slug
        axios.get(`${this.domain}/api/v1/blog/articles/${slug}/`)
            .then(response => this.data = response.data)
            .catch(() => this.error = true)
            .finally(() => this.loading = false)
    },
    watch: {
        $route() {
            var slug = this.$route.params.slug
            axios.get(`${this.domain}/api/v1/blog/articles/${slug}/`)
                .then(response => this.data = response.data)
                .catch(() => this.error = true)
                .finally(() => this.loading = false)
        }
    }
}
</script>