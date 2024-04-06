<template>

    <div class="services-view container p-5">
        <div class="mt-5 d-flex flex-column m-auto gap-2">
            <h6 class="fw-bold h1">Our Services</h6>
            <p class="text-secondary w-50 m-auto">Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto, dicta
                id aliquam
                animi doloribus deserunt mollitia inventore culpa </p>
            <div class="servics-body m-auto d-flex gap-3 flex-column justify-content-center align-items-center mt-5">
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
            </div>
        </div>
    </div>

</template>

<script>
import ServiceItem from '@/components/services_components/ServiceItem.vue';
import axios from 'axios';

export default {
    name: "ServicesView",
    components: {
        'service-item': ServiceItem,
    },
    data() {
        return {
            services: null,
            loading: true,
            error: false,
            domain: this.$store.state.domain
        }
    },
    mounted() {
        axios.get(`${this.domain}/api/v1/services/`)
            .then(response => this.services = response.data)
            .catch(() => this.error = true)
            .finally(this.loading = false)
    },
    watch: {
        $route() {
            axios.get(`${this.domain}/api/v1/services/`)
                .then(response => this.services = response.data)
                .catch(() => this.error = true)
                .finally(this.loading = false)
        }
    }
}
</script>