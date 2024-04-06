<template>

    <div class="contact-us">
        <div class="container p-5 rounded d-flex flex-column gap-5 justify-content-center align-items-center">
            <div class="info w-50">
                <h3 class="fw-bold">Contact Me</h3>
                <p class="text-secondary mt-4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusantium
                    cumque quisquam, hic consectetur
                    laborum veniam omnis aliquam</p>
            </div>

            <div class="d-flex flex-column flex-md-row w-100 justify-content-center align-items-start gap-5">
                <div class="contact-form col-md-6">
                    <form :submit="sendMessage" method="post" class="form text-start gap-4 d-flex flex-column">
                        <div class="d-flex flex-column flex-md-row gap-1">
                            <div class="col-md-6">
                                <label for="name">Name</label>
                                <input type="text" required v-model="name" name="name" class="form-control">
                            </div>
                            <div class="col-md-6">
                                <label for="email">Email</label>
                                <input type="email" required v-model="email" name="email" class="form-control">
                            </div>
                        </div>
                        <div class="">
                            <label for="subject">Subject</label>
                            <input type="text" required v-model="subject" name="subject" class="form-control">
                        </div>
                        <div>
                            <label for="message">Message</label>
                            <textarea name="message" required v-model="message" id="message" cols="30" rows="10"
                                class="form-control"></textarea>
                        </div>
                        <div v-if="error">
                            <p class="alert alert-danger mt-3">Send Message Field</p>
                        </div>
                        <div v-if="response == '201'">
                            <p class="alert alert-success mt-3">Message Sended.</p>
                        </div>
                        <send-button title="Send Message" class="mt-1" @click="sendMessage"
                            v-if="loading == false"></send-button>
                        <div v-else>
                            <div class="spinner-border text-center" role="status">
                                <span class="visually-hidden">Loading...</span>
                            </div>
                        </div>
                    </form>
                </div>
                <div class="col-md-4 d-flex flex-column gap-3" v-if="data">
                    <div class="address d-flex flex-column gap-1">
                        <span class="mb-4"><i class="ri-map-line text-warning p-2 bg-dark rounded-circle"></i></span>
                        <div class="d-flex justify-content-between">
                            <span>Country:</span>
                            <span>{{ data.country }}</span>
                        </div>
                        <div class="d-flex justify-content-between">
                            <span>City:</span>
                            <span>{{ data.city }}</span>
                        </div>
                    </div>
                    <hr>
                    <div class="social d-flex flex-column gap-1">
                        <span class="mb-4"><i class="ri-mail-line text-warning p-2 bg-dark rounded-circle"></i></span>
                        <div class="d-flex justify-content-between">
                            <span>Email:</span>
                            <span>{{ data.email }}</span>
                        </div>
                    </div>
                    <hr>
                    <div class="phones d-flex flex-column gap-1">
                        <span class="mb-4"><i class="ri-phone-line text-warning p-2 bg-dark rounded-circle"></i></span>
                        <div class="d-flex justify-content-between" v-for="(phone, index) in data.phones" :key="phone">
                            <span>Phone{{ index + 1 }}:</span>
                            <span>{{ phone.phone_number }}</span>
                        </div>
                    </div>
                </div>
                <div v-if="loading && data != null">
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
            </div>
        </div>

    </div>

</template>

<script>
import SendButton from '@/components/buttons_components/SendButton.vue'
import axios from 'axios'
export default {
    name: "ContactUs",
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
            error: false
        }
    },
    methods: {
        async sendMessage() {
            this.loading = true
            this.error = false
            this.response = 0
            const message = { "name": this.name, "email": this.email, "subject": this.subject, "message": this.message }
            await axios.post("http://127.0.0.1:8000/api/v1/contacts/", message)
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
        axios.get("http://127.0.0.1:8000/api/v1/contacts/")
            .then(response => this.data = response.data)
            .catch(() => this.dataError = true)
            .finally(() => this.dataLoading = false)

    },
    watch: {
        $route() {
            axios.get("http://127.0.0.1:8000/api/v1/contacts/")
                .then(response => this.data = response.data)
                .catch(() => this.dataError = true)
                .finally(() => this.dataLoading = false)
        }
    }
}
</script>