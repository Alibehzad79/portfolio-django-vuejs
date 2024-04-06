<template>
    <div class="main-slide">
        <div class="d-flex flex-column flex-md-row container justify-content-around align-items-center mt-5"
            v-if="profile">
            <div class="d-flex flex-row justify-content-between align-items-center gap-1 col col-md-6">
                <div class="col-6">
                    <h1 class="text-start fw-bold">{{ profile.profile.full_name }}</h1>
                    <hr class="text-warning">
                    <div>
                        <p class="text-start">Social account</p>
                        <ul class="social nav d-flex flex-wrap bg-white rounded justify-content-center">
                            <li v-for="(social, index) in profile.socials.social_item" :key="index" class="nav-item"><a
                                    :href="social.url" class="nav-link text-secondary"><i
                                        :class="'ri-' + social.name + '-fill'"></i></a>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="col-6">
                    <img :src="domain + profile.profile.img" :alt="profile.profile.full_name"
                        :title="profile.profile.full_name" class="img-fluid my-logo">
                </div>
            </div>
            <div class="d-flex flex-column text-start gap-3 col col-md-3">
                <h2 class="fw-bold">
                    {{ profile.profile.whate_am_i }}
                </h2>
                <p class="text-secondary">{{ profile.profile.my_description }}</p>
                <div class="lets-talk d-flex gap-2 bg-warning justify-content-between align-items-center p-2 rounded-5">
                    <a :href="'tel:'+profile.profile.phone" class="ms-3 nav-link text-dark">Let's to Talk!</a>
                    <a :href="'tel:'+profile.profile.phone" class="text-decoration-none bg-dark px-2 py-1 rounded-5 text-warning"><i
                            class="ri-arrow-right-line"></i></a>
                </div>
            </div>
            <div v-if="loading && profile != null">
                <div class="spinner-border" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
            </div>
            <div v-if="error">
                <span><i class="ri-error-line fs-1"></i></span>
            </div>
            <div v-if="profile == null" class="border p-5 border-dark rounded col-6 m-auto">
                <span class="d-flex align-items-center gap-2"><i class="ri-box-3-line fs-1"></i> Empty</span>
            </div>
        </div>

    </div>
</template>

<script>
import axios from "axios";
export default {
    name: "MainSlide",
    components: {
    },
    data() {
        return {
            profile: null,
            error: false,
            loading: true,
            domain: this.$store.state.domain
        }
    },
    mounted() {
        axios.get(`${this.domain}/api/v1/profile/`)
            .then(response => this.profile = response.data)
            .catch(() => this.error = true)
            .finally(() => this.loading = false)
    },
    watch: {
        $route() {
            axios.get(`${this.domain}/api/v1/profile/`)
                .then(response => this.profile = response.data)
                .catch(() => this.error = true)
                .finally(() => this.loading = false)
        }
    }
}
</script>