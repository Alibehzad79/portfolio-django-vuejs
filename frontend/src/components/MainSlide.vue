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
                <div
                    class="lets-talk d-flex gap-2 bg-warning justify-content-between align-items-center p-2 rounded-5">
                    <span class="ms-3">Let's Talk</span>
                    <a href="#" class="text-decoration-none bg-dark px-2 py-1 rounded-5 text-warning"><i
                            class="ri-arrow-right-line"></i></a>
                </div>
            </div>
        </div>
    </div>
    <div class="bg-warning p-3 mt-5 d-flex flex-wrap gap-5 justify-content-center align-items-center d-none d-md-flex">
        <a v-for="(compony, index) in componies" :key="index" :href="compony.url"><img :src="compony.img"
                :alt="compony.name" class="img-fluid compony"></a>
    </div>
</template>

<script>
export default {
    name: "MainSlide",
    data() {
        return {
            socials: [
                { "name": "instagram", "url": "https://instagram.com/username/" },
                { "name": "telegram", "url": "https://telegram.com/username/" },
                { "name": "github", "url": "https://github.com/username/" },
                { "name": "facebook", "url": "https://facebook.com/username/" },
                { "name": "twitter", "url": "https://twitter.com/username/" },
            ],
            componies: [
                { "name": "microsoft", "img": "https://logos-world.net/wp-content/uploads/2020/09/Microsoft-Emblem.jpg", "url": "https://microsoft.com/" },
                { "name": "google", "img": "https://s3.amazonaws.com/freebiesupply/large/2x/google-logo-transparent.png", "url": "https://google.com/" },
                { "name": "dropbox", "img": "http://logos-download.com/wp-content/uploads/2016/07/Dropbox_logo.png", "url": "https://dropbox.com/" },
                { "name": "amazon", "img": "http://www.freelargeimages.com/wp-content/uploads/2014/11/Amazon_logo-4.jpg", "url": "https://amazon.com/" },
                { "name": "facebook", "img": "https://logos-world.net/wp-content/uploads/2020/04/Facebook-Logo.png", "url": "https://facebook.com/" },
            ]
        }
    }
}
</script>