<template>
    <div class="service-detail container mt-5">
        <div class="d-flex flex-column flex-md-row gap-3 justify-content-between align-items-start">
            <div class="col-md-8 text-start p-3 d-flex flex-column gap-4 m-auto" v-if="data">
                <h6 class="fw-bold h3">About {{ data.title }} Service</h6>
                <p class="text-secondary">{{ data.content }}</p>
                <div class="options d-flex flex-column gap-3">
                    <div class="option d-flex gap-2" v-for="option in data.service_option" :key="option">
                        <span><i class="bg-warning ri-check-line rounded-circle p-1"></i></span>
                        <span>{{ option.title }}</span>
                    </div>
                </div>
                <div class="plans d-flex flex-column gap-3 mt-5">
                    <h6 class="fw-bold h4">We Have Exclusive Plan In Our Pricing</h6>
                    <div class="plan border d-flex flex-column gap-3">
                        <div class="head d-flex justify-content-between p-3">
                            <span>Service</span>
                            <span>Price</span>
                        </div>
                        <div class="plans-item bg-white p-3 d-flex flex-column gap-3">
                            <div class="d-flex justify-content-between" v-for="plan in data.service_plan" :key="plan">
                                <span class="fw-bold text-secondary">{{ plan.title }}</span>
                                <span class="text-secondary">${{ plan.plan }}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div v-if="dataLoading">
                <div class="spinner-border" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
            </div>
            <div v-if="dataError">
                <span><i class="ri-error-line fs-1"></i></span>
            </div>
            <div v-if="data == null" class="border p-5 border-dark rounded">
                <span class="d-flex align-items-center gap-2"><i class="ri-box-3-line fs-1"></i> Empty</span>
            </div>
            <div v-if="data == ''" class="border p-5 border-dark roundeds">
                    <span class="d-flex align-items-center gap-2"><i class="ri-box-3-line fs-1"></i> Empty</span>
                </div>
            <div class="col-md-4 bg-primary bg-white p-3 d-flex flex-column gap-3 rounded m-auto mb-5" v-if="data">
                <h6 class="fw-bold mt-3">Request an Appointment</h6>
                <form method="post" class="form d-flex flex-column gap-3" @submit.prevent="sendRequestToWork">
                    <div class="col text-start">
                        <label for="name">Name</label>
                        <input type="text" v-model="name" name="name" class="form-control">
                    </div>
                    <div class="col text-start">
                        <label for="email">Email</label>
                        <input type="email" v-model="email" name="email" class="form-control">
                    </div>
                    <div class="col text-start">
                        <label for="subject">Subject</label>
                        <input type="text" v-model="subject" name="subject" class="form-control">
                    </div>
                    <div class="col text-start">
                        <label for="message">Message</label>
                        <textarea name="message" v-model="message" id="message" cols="30" rows="10"
                            class="form-control"></textarea>
                    </div>
                    <div v-if="error">
                        <p class="alert alert-danger mt-3">Send Message Field</p>
                    </div>
                    <div v-if="response == '201'">
                        <p class="alert alert-success mt-3">Message Sended.</p>
                    </div>
                    <send-button title="Send Message" class="mt-1" @click="sendRequestToWork"
                        v-if="loading == false"></send-button>
                    <div v-else>
                        <div class="spinner-border text-center" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import SendButton from '@/components/buttons_components/SendButton.vue';
import axios from 'axios';

export default {
    name: "ServiceDetail",
    components: {
        'send-button': SendButton,
    },
    data() {
        return {
            data: null,
            dataLoading: true,
            dataError: false,
            name: "",
            email: "",
            subject: "",
            message: "",
            response: 0,
            loading: false,
            error: false,
            domain: this.$store.state.domain
        }
    },
    methods: {
        sendRequestToWork() {
            this.loading = true
            this.error = false
            this.response = 0
            var data = { "service": this.data.id, "name": this.name, "email": this.email, "subject": this.subject, "message": this.message }
            axios.post(`${this.domain}/api/v1/request-to-work/`, data)
                .then(response => this.response = response.status)
                .catch(() => this.error = true)
                .finally(() => this.loading = false)
            this.name = ""
            this.email = ""
            this.subject = ""
            this.message = ""
        }
    },
    mounted() {
        var slug = this.$route.params.slug
        axios.get(`${this.domain}/api/v1/services/${slug}`)
            .then(response => this.data = response.data)
            .catch(() => this.dataError = true)
            .finally(() => this.dataLoading = false)
    },
    watch: {
        $route() {
            var slug = this.$route.params.slug
            axios.get(`${this.domain}/api/v1/services/${slug}`)
                .then(response => this.data = response.data)
                .catch(() => this.dataError = true)
                .finally(() => this.dataLoading = false)
        }
    }
}
</script>