<template>
    <div class="myServices scrollspy-example bg-body-tertiary p-3 rounded-2" data-bs-spy="scroll"
        data-bs-target="#myNav" data-bs-root-margin="0px 0px -40%" data-bs-smooth-scroll="true" tabindex="0">
        <div id="services" class="container my-5 d-flex flex-column gap-5">
            <div class="service-headee w-50 m-auto">
                <h4 class="h1 fw-bold">My Sercices</h4>
                <p class="text-secondary">Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis eligendi
                    facilis consequuntur ab
                    amet mollitia praesentium saepe veniam nesciunt voluptatum nihil in tempore error totam debitis
                    incidunt harum, vitae corrupti!</p>
            </div>
            <div class="servics-body m-auto d-flex gap-3 flex-wrap justify-content-center">
                <div v-for="(service, index) in services" :key="index" @click="getServiceDetail(service.slug)"
                    class="service-card card border-0 mb-3" style="max-width: 18rem;">
                    <div class="card-header bg-transparent border-0 text-start p-4"><i
                            class="bg-warning p-3 text-white rounded fs-2" :class="'ri-' + service.icon + '-line'"></i>
                    </div>
                    <div class="card-body d-flex flex-column gap-2">
                        <h5 class="card-title text-start">{{ service.title }}</h5>
                        <p class="card-text text-start text-secondary">{{ service.content }}</p>
                    </div>
                </div>
                <router-link to="/services"
                    class="service-more card border-0 px-5 mb-3 justify-content-center nav-link"><span>more <i
                            class="ri-arrow-right-line"></i></span></router-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "MyServices",
    data() {
        return {
            services: [
                { "title": "Web Developmet", "slug": "web-developmet", "content": "Some quick example text to build on the card title and make up the bulk of the card's content.", "icon": "code-box" },
                { "title": "App Development", "slug": "app-development", "content": "Some quick example text to build on the card title and make up the bulk of the card's content.", "icon": "android" },
                { "title": "UI / UX Designer", "slug": "uiux-designer", "content": "Some quick example text to build on the card title and make up the bulk of the card's content.", "icon": "android" },
            ]
        }
    },
    methods: {
        getServiceDetail(slug) {
            this.$router.push({ name: 'servic-detail', params: { slug: slug } })
        }
    }
}
</script>