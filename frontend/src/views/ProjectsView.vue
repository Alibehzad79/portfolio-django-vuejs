<template>
    <div class="project-view container p-5">
        <div class="mt-5 d-flex flex-column m-auto gap-2">
            <h6 class="fw-bold h1 mb-5">Projects</h6>
            <div class="projects d-flex flex-column flex-md-row gap-4 flex-wrap" v-if="data">
                <project-item v-for="project in data" :key="project" :image="project.image" :title="project.title"
                    :client="project.client" :url="project.website"
                    class="col-md-6 col-lg-4 bg-white p-0 rounded"></project-item>
            </div>
            <div v-if="loading">
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

import axios from 'axios';
import ProjectItem from '@/components/projects_components/ProjectItem.vue'

export default {
    name: "ProjectView",
    components: {
        'project-item': ProjectItem,
    },
    data() {
        return {
            data: null,
            loading: true,
            error: false
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/v1/projects/')
            .then(response => this.data = response.data)
            .catch(() => this.error = true)
            .finally(() => this.loading = false)
    },
    watch: {
        $route() {
            axios.get('http://127.0.0.1:8000/api/v1/projects/')
                .then(response => this.data = response.data)
                .catch(() => this.error = true)
                .finally(() => this.loading = false)
        }
    }
}
</script>