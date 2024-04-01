<template>

    <div class="project-item container col-4">
        <div @click="getUrl" class="d-flex flex-column gap-3">
            <img :src="'http://127.0.0.1:8000'+image" :alt="title" class="img-fluid project-image">
            <div class="info d-flex flex-column gap-2">
                <span class="text-start">{{ client }}</span>
                <h3 class="text-start fw-bold">{{ title }}</h3>
                <router-link :to="url" class="text-start p-2 text-dark">more detail</router-link>
            </div>
        </div>
    </div>

</template>

<script>
export default {
    name: "ProjectItem",
    props: ["image", "title", "client", "url"],
    data() {
        return {}
    },
    methods: {
        getUrl() {
            this.$router.push(this.url)
        }
    }
}
</script>