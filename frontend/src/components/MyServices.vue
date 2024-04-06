<template>
    <div class="myServices rounded-2">
        <div id="services" class="container my-5 d-flex flex-column gap-5">
            <div class="service-headee w-50 m-auto">
                <h4 class="h1 fw-bold">My Sercices</h4>
                <p class="text-secondary">Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis eligendi
                    facilis consequuntur ab
                    amet mollitia praesentium saepe veniam nesciunt voluptatum nihil in tempore error totam debitis
                    incidunt harum, vitae corrupti!</p>
            </div>
            <div class="servics-body m-auto d-flex gap-3 flex-column justify-content-center align-items-center">
                <div class="d-flex gap-3 flex-wrap justify-content-center">
                    <service-item v-for="service in services" :key="service" :icon="service.icon" :title="service.title"
                        :content="service.content" :slug="service.slug"></service-item>
                </div>
                <div v-if="loading && services != null">
                    <div class="spinner-border" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                </div>
                <div v-if="error">
                    <span><i class="ri-error-line fs-1"></i></span>
                </div>
                <div v-if="services == null" class="border p-5 border-dark rounded">
                    <span class="d-flex align-items-center gap-2"><i class="ri-box-3-line fs-1"></i> Empty</span>
                </div>
                <div v-if="services == ''" class="border p-5 border-dark roundeds">
                    <span class="d-flex align-items-center gap-2"><i class="ri-box-3-line fs-1"></i> Empty</span>
                </div>
                <primary-button title="More" url="/services" v-if="services"></primary-button>
            </div>
        </div>
    </div>
</template>

<script>
import ServiceItem from '@/components/services_components/ServiceItem.vue'
import PrimaryButton from "@/components/buttons_components/PrimaryButton.vue";
import axios from 'axios';
export default {
    name: "MyServices",
    components: {
        "service-item": ServiceItem,
        'primary-button': PrimaryButton,
    },
    data() {
        return {
            services: null,
            error: false,
            loading: true,
            domain: this.$store.state.domain
        }
    },
    methods: {
        getServiceDetail(slug) {
            this.$router.push({ name: 'servic-detail', params: { slug: slug } })
        }
    },
    mounted() {
        axios.get(`${this.domain}/api/v1/services/?limit=3`)
            .then(response => this.services = response.data)
            .catch(() => this.error = true)
            .finally(this.loading = false)
    },
    watch: {
        $route() {
            axios.get(`${this.domain}/api/v1/services/?limit=3`)
                .then(response => this.services = response.data)
                .catch(() => this.error = true)
                .finally(this.loading = false)
        }
    }
}
</script>