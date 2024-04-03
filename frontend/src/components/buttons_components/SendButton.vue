<template>
    <div class="priamry-button">
        <div class="lets-talk d-flex gap-2 bg-warning justify-content-between align-items-center p-2 rounded-5">
            <span class="ms-3">{{ title }}</span>
            <span class="text-decoration-none bg-dark px-2 py-1 rounded-5 text-warning"><i
                    class="ri-arrow-right-line"></i></span>
        </div>
    </div>
</template>

<script>
export default {
    name: "PrimaryButton",
    props: ["title"],
}
</script>