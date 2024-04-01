<template>
    <div class="priamry-button">
        <div class="lets-talk d-flex gap-2 bg-warning justify-content-between align-items-center p-2 rounded-5"
            @click="getUrl">
            <span class="ms-3">{{ title }}</span>
            <a :href="getUrl" class="text-decoration-none bg-dark px-2 py-1 rounded-5 text-warning"><i
                    class="ri-arrow-right-line"></i></a>
        </div>
    </div>
</template>

<script>
export default {
    name: "PrimaryButton",
    props: ["title", "url"],
    methods: {
        getUrl(){
            this.$router.push(this.url)
        }
    }
}
</script>