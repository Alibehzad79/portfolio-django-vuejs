<template>
    <div class="latest-projects bg-white">
        <div class="container bg-white p-5 rounded d-flex flex-column gap-5 justify-content-center align-items-center">
            <div class="info w-50">
                <h3 class="fw-bold">Latest Project</h3>
                <p class="text-secondary mt-4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusantium
                    cumque quisquam, hic consectetur
                    laborum veniam omnis aliquam</p>
            </div>
            <div class="projects d-flex" v-if="info != 'null'">
                <project-item v-for="data in info" :key="data" :image="data.project_gallery['0'].image"
                    :title="data.title" :client="data.client" :url="data.title.replace(' ', '-')"></project-item>
            </div>

            <primary-buttom title="more projects" url="/projects"></primary-buttom>
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
            info: "null"
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/v1/projects/')
            .then(response => this.info = response.data)
            .catch(error => this.info = error)
    },
    watch: {
        $route() {
            axios.get('http://127.0.0.1:8000/api/v1/projects/')
                .then(response => this.info = response.data)
                .catch(error => this.info = error)
        }

    }
}
</script>