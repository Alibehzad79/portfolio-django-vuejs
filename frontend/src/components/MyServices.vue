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
            <div class="servics-body m-auto d-flex gap-3 flex-column justify-content-center align-items-center">
                <div class="d-flex gap-3 flex-wrap justify-content-center">
                    <service-item v-for="service in services" :key="service" :icon="service.icon" :title="service.title"
                        :content="service.content" :slug="service.slug"></service-item>
                </div>
                <primary-button title="More" url="/services"></primary-button>
            </div>
        </div>
    </div>
</template>

<script>
import ServiceItem from '@/components/services_components/ServiceItem.vue'
import PrimaryButton from "@/components/buttons_components/PrimaryButton.vue";
export default {
    name: "MyServices",
    components: {
        "service-item": ServiceItem,
        'primary-button': PrimaryButton,
    },
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