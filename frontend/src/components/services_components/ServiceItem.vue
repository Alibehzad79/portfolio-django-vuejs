<template>
    <div class="service-item">
        <div class="service-card card border-0 mb-3" style="max-width: 18rem;" @click="getUrl">
            <div class="card-header bg-transparent border-0 text-start p-4"><i
                    class="bg-warning p-3 text-white rounded fs-2" :class="'ri-' + icon + '-line'"></i>
            </div>
            <div class="card-body d-flex flex-column gap-2">
                <h5 class="card-title text-start">{{ title }}</h5>
                <p class="card-text text-start text-secondary">{{ content }}</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "ServiceItem",
    props: [
        'icon',
        'title',
        'content',
        'slug'
    ],
    data() {
        return {

        }
    },
    methods: {
        getUrl(){
            this.$router.push('/services/'+this.slug)
        }
    }
}

</script>