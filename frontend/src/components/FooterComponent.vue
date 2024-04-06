<template>
    <div class="footer bg-white">
        <!-- Footer -->
        <footer class="text-center container text-lg-start text-muted" v-if="data">
            <!-- Section: Social media -->
            <section class="d-flex justify-content-center justify-content-lg-between p-4 border-bottom">

                <!-- Right -->
                <div>
                    <a :href="social.url" class="me-4 text-reset" v-for="social in data.socials.social_item"
                        :key="social">
                        <i :class="'ri-' + social.name + '-line'"></i>
                    </a>
                </div>
                <!-- Right -->
            </section>
            <!-- Section: Social media -->

            <!-- Section: Links  -->
            <section class="">
                <div class="container text-center text-md-start mt-5">
                    <!-- Grid row -->
                    <div class="row mt-3">
                        <!-- Grid column -->
                        <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
                            <!-- Content -->
                            <h6 class="text-uppercase fw-bold mb-4">
                                <i class="fas fa-gem me-3"></i>{{ data.site_settings.site_name }}
                            </h6>
                            <p>
                                {{ data.site_settings.site_about }}
                            </p>
                        </div>
                        <!-- Grid column -->

                        <!-- Grid column -->
                        <div class="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4">
                            <!-- Links -->
                            <h6 class="text-uppercase fw-bold mb-4">
                                Navigations
                            </h6>
                            <ul class="nav flex-column">
                                <li class="nav-item">
                                    <router-link class="nav-link text-dark" to="/">Home</router-link>
                                </li>
                                <li class="nav-item">
                                    <!-- <a class="nav-link" href="/about">About</a> -->
                                    <router-link to="/about" class="nav-link text-dark">About</router-link>
                                </li>
                                <li class="nav-item">
                                    <router-link to="/services" class="nav-link text-dark">Services</router-link>
                                </li>
                                <li class="nav-item">
                                    <router-link class="nav-link text-dark" to="/projects">Projects</router-link>
                                </li>
                                <li class="nav-item">
                                    <router-link class="nav-link text-dark" to="/blog/articles">Blog</router-link>
                                </li>
                                <li class="nav-item">
                                    <router-link class="nav-link text-dark" to="/contact">Contact</router-link>
                                </li>
                            </ul>
                        </div>
                        <!-- Grid column -->

                        <!-- Grid column -->
                        <div class="col-md-3 col-lg-2 col-xl-2 mx-auto mb-4">
                            <!-- Links -->
                            <h6 class="text-uppercase fw-bold mb-4">
                                Contact
                            </h6>
                            <p>
                                <a :href="'mailto:' + data.contacts_info.email" class="text-reset">{{
            data.contacts_info.email }}</a>
                            </p>
                            <p v-for="phone in data.contacts_info.phones" :key="phone">
                                <a :href="'tel:' + phone.phone_number" class="text-reset">{{ phone.phone_number }}</a>
                            </p>
                        </div>
                        <!-- Grid column -->

                        <!-- Grid column -->
                        <div class="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4">
                            <!-- Links -->
                            <h6 class="text-uppercase fw-bold mb-4">Address</h6>
                            <p><i class="fas fa-home me-3"></i> {{ data.contacts_info.country }} /
                                {{ data.contacts_info.city }}</p>
                        </div>
                        <!-- Grid column -->
                    </div>
                    <!-- Grid row -->
                </div>
            </section>
            <!-- Section: Links  -->

            <!-- Copyright -->
            <div class="text-center p-4" style="background-color: rgba(0, 0, 0, 0.05);">
                © {{ date }} Copyright:
                <a class="text-reset fw-bold" href="/">{{ data.site_settings.site_name }}</a>
            </div>
            <!-- Copyright -->
        </footer>
        <!-- Footer -->
        <div v-if="error">
            <span><i class="ri-error-line fs-1"></i></span>
        </div>
        <div v-if="data == null" class="border p-5 border-dark rounded container m-auto">
            <span class="d-flex align-items-center gap-2 justify-content-center"><i class="ri-box-3-line fs-1"></i>
                Empty</span>
        </div>
        <div v-if="loading && data != null">
            <div class="spinner-border text-center" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
var date = new Date()
export default {
    name: "FooterComponent",
    data() {
        return {
            data: null,
            loading: true,
            error: false,
            date: date.getFullYear()
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/v1/site-settings/')
            .then(response => this.data = response.data)
            .catch(() => this.error = true)
            .finally(() => this.loading = false)
    },
    watch: {
        $route() {
            axios.get('http://127.0.0.1:8000/api/v1/site-settings/')
                .then(response => this.data = response.data)
                .catch(() => this.error = true)
                .finally(() => this.loading = false)
        }
    }
}
</script>