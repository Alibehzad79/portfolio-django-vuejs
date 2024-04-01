<template>
    <div class="main-slide">
        <div class="d-flex flex-column flex-md-row container justify-content-around align-items-center mt-5">
            <div class="d-flex flex-row justify-content-between align-items-center gap-1 col col-md-6">
                <div class="col-6">
                    <h1 class="text-start fw-bold">Ali <br> behzad</h1>
                    <hr class="text-warning">
                    <div>
                        <p class="text-start">Social account</p>
                        <ul class="social nav d-flex flex-wrap bg-white rounded justify-content-center">
                            <li v-for="(social, index) in socials" :key="index" class="nav-item"><a :href="social.url"
                                    class="nav-link text-secondary"><i :class="'ri-' + social.name + '-fill'"></i></a>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="col-6">
                    <img src="../assets/myLogo.svg" alt="myLogo" class="img-fluid my-logo">
                </div>
            </div>
            <div class="d-flex flex-column text-start gap-3 col col-md-3">
                <h2 class="fw-bold">
                    I'm a Professional Product Designer in New York
                </h2>
                <p class="text-secondary">Lorem ipsum dolor sit amet consectetur adipisicing elit. Dicta dolores tenetur
                    modi, nihil sunt vel
                    blanditiis nobis cumque earum illum facilis laborum libero, neque fuga aliquid, culpa error
                    necessitatibus animi!</p>
                <primary-button title="Let's To Talk!" url="#"></primary-button>
            </div>
        </div>
    </div>
</template>

<script>
import PrimaryButton from "@/components/buttons_components/PrimaryButton.vue";
export default {
    name: "MainSlide",
    components: {
        "primary-button": PrimaryButton,
    },
    data() {
        return {
            socials: [
                { "name": "instagram", "url": "https://instagram.com/username/" },
                { "name": "telegram", "url": "https://telegram.com/username/" },
                { "name": "github", "url": "https://github.com/username/" },
                { "name": "facebook", "url": "https://facebook.com/username/" },
                { "name": "twitter", "url": "https://twitter.com/username/" },
            ]
        }
    }
}
</script>