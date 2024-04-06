<template>

    <div class="project-item container">
        <div @click="getUrl" class="d-flex flex-column gap-3 p-4 rounded-3">
            <img :src="domain + image" :alt="title" class="img-fluid project-image">
            <div class="info d-flex flex-column gap-2">
                <span class="text-start">{{ client }}</span>
                <h6 class="text-start fw-bold project-title">{{ title }}</h6>
                <a class="text-start p-2 text-dark">more detail</a>
            </div>
        </div>
    </div>

</template>

<script>
export default {
    name: "ProjectItem",
    props: ["image", "title", "client", "url"],
    data() {
        return {
            domain: this.$store.state.domain
        }
    },
    methods: {
        getUrl() {
            window.location.href = this.url
        }
    }
}
</script>