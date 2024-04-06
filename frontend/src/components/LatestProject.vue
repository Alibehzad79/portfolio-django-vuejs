<template>
    <div class="latest-projects bg-white">
        <div class="container bg-white p-5 rounded d-flex flex-column gap-5 justify-content-center align-items-center">
            <div class="info w-50">
                <h3 class="fw-bold">Latest Project</h3>
                <p class="text-secondary mt-4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusantium
                    cumque quisquam, hic consectetur
                    laborum veniam omnis aliquam</p>
            </div>
            <div class="projects d-flex flex-column flex-md-row gap-3" v-if="info">
                <project-item v-for="data in info" :key="data" :image="data.image" :title="data.title"
                    :client="data.client" :url="data.website" class="bg-mute p-0 rounded"></project-item>
            </div>
            <div v-if="loading && info != null">
                <div class="spinner-border" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
            </div>
            <div v-if="error">
                <span><i class="ri-error-line fs-1"></i></span>
            </div>
            <div v-if="info == null" class="border p-5 border-dark rounded">
                <span class="d-flex align-items-center gap-2"><i class="ri-box-3-line fs-1"></i> Empty</span>
            </div>
            <primary-buttom title="more projects" url="/projects" v-if="info"></primary-buttom>
        </div>
    </div>
</template>

<script>
import PrimaryButton from '@/components/buttons_components/PrimaryButton.vue';
import ProjectItem from '@/components/projects_components/ProjectItem.vue'
import axios from 'axios'
export default {
    name: "LatestPorojects",
    components: {
        "project-item": ProjectItem,
        'primary-buttom': PrimaryButton
    },
    data() {
        return {
            loading: true,
            error: false,
            info: null,
            domain: this.$store.state.domain
        }
    },
    mounted() {
        axios.get(`${this.domain}/api/v1/projects/?limit=3`)
            .then(response => this.info = response.data)
            .catch(() => this.error = true)
            .finally(() => this.loading = false)
    },
    watch: {
        $route() {
            axios.get(`${this.domain}/api/v1/projects/?limit=3`)
                .then(response => this.info = response.data)
                .catch(() => this.error = true)
                .finally(() => this.loading = false)
        }

    }
}
</script>
