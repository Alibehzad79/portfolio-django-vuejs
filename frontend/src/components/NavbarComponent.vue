<template>
    <div class="my-nav sticky-top" id="myNav">
        <nav class="navbar navbar-expand-lg bg-white mt-4 container rounded-5 p-2">
            <div class="container">
                <div class="d-flex gap-3 justify-content-center align-items-center">
                    <a v-if="data" class="navbar-brand" href="/"><img :src="domain + data.site_settings.site_logo"
                            alt="Logo" class="img-fluid rounded-5 logo"></a>
                    <i class="ri-search-line fs-4 d-lg-none search" @click="showSearch"
                        :class="{ 'text-primary rounded-5': search }"></i>
                </div>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                    aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <router-link class="nav-link" to="/">Home</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link to="/services" class="nav-link">Services</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" to="/projects">Projects</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" to="/blog/articles">Blog</router-link>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/#contact">Contact</a>
                        </li>
                        <li class="nav-item">
                            <a href="/#resume" class="nav-link">About</a>
                        </li>
                    </ul>
                    <div class="d-none d-lg-flex search" @click="showSearch"
                        :class="{ 'text-warning rounded-5': search }">
                        <i class="ri-search-line fs-4"></i>
                    </div>
                </div>
            </div>
        </nav>
        <div class="search-box container mt-2 d-flex" v-if="search">
            <input type="search" class="form-control rounded-5 rounded-end-0 py-2" v-model="searchInput"
                placeholder="Search in blog..." @keyup.enter="getSearch()">
            <button class="btn btn-warning rounded-start-0 rounded-5 px-3" @click="getSearch"><i
                    class="ri-search-line"></i></button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "NavbarComponent",
    data() {
        return {
            search: false,
            searchInput: "",
            data: null,
            domain: this.$store.state.domain
        }
    },
    methods: {
        showSearch() {
            this.search = !this.search
        },
        getSearch() {
            this.$router.push('/blog/articles/search/' + this.searchInput)
        }
    },
    mounted() {
        axios.get(`${this.domain}/api/v1/site-settings/`)
            .then(response => this.data = response.data)
            .catch(() => this.error = true)
            .finally(() => this.loading = false)
    },
    watch: {
        $route() {
            axios.get(`${this.domain}/api/v1/site-settings/`)
                .then(response => this.data = response.data)
                .catch(() => this.error = true)
                .finally(() => this.loading = false)
        }
    }
}
</script>