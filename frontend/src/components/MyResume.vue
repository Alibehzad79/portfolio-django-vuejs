<template>
    <div class="my-reusme p-5">
        <div class="reusme-header w-50 m-auto mb-5">
            <h4 class="h1 fw-bold mb-3">My Resume</h4>
            <p class="text-secondary">Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis eligendi
                facilis consequuntur ab
                amet mollitia praesentium saepe veniam nesciunt voluptatum nihil in tempore error totam debitis
                incidunt harum, vitae corrupti!</p>
        </div>
        <div class="d-flex flex-column flex-md-row align-items-start container gap-4" v-if="data">
            <div class="nav flex-sm-row nav-pills col col-md-4 flex-md-column" id="v-pills-tab" role="tablist"
                aria-orientation="vertical">
                <button class="nav-link text-dark  text-start active" id="education-tab" data-bs-toggle="pill"
                    data-bs-target="#education" type="button" role="tab" aria-controls="education"
                    aria-selected="true">Education</button>

                <button class="nav-link text-dark  text-start" id="experiance-tab" data-bs-toggle="pill"
                    data-bs-target="#experiance" type="button" role="tab" aria-controls="experiance"
                    aria-selected="true">Experiance</button>

                <button class="nav-link text-dark  text-start" id="skills-tab" data-bs-toggle="pill"
                    data-bs-target="#skills" type="button" role="tab" aria-controls="skills"
                    aria-selected="true">Professional Skills</button>
            </div>
            <div class="tab-content col  bg-white w-100 rounded" id="v-pills-tabContent bg-white">
                <div class="tab-pane fade show active" id="education" role="tabpanel" aria-labelledby="education-tab"
                    tabindex="0">
                    <div class="d-flex flex-column flex-md-row justify-content-between align-items-start p-5 gap-2"
                        v-for="education in data.educations" :key="education">
                        <div class="d-flex flex-column gap-3 text-start col col-md-4">
                            <h6 class="fw-bold text-start">{{ education.title }}</h6>
                            <span class="badge bg-warning text-start">{{ education.start_date }} - {{
            education.end_date }}</span>
                        </div>
                        <div class="d-flex flex-column gap-2 text-start col col-md-8">
                            <h6 class="fw-bold">{{ education.certificate }}</h6>
                            <p class="text-secondary">{{ education.description }}</p>
                        </div>
                    </div>
                </div>
                <div class="tab-pane fade show" id="experiance" role="tabpanel" aria-labelledby="experiance-tab"
                    tabindex="0">
                    <div class="d-flex flex-column flex-md-row justify-content-between align-items-start p-5 gap-2"
                        v-for="experiance in data.experiances" :key="experiance">
                        <div class="d-flex flex-column gap-3 text-start col col-md-4">
                            <h6 class="fw-bold text-start">{{ experiance.title }}</h6>
                            <span class="badge bg-warning text-start">{{ experiance.start_date }} - {{
            experiance.end_date }}</span>
                        </div>
                        <div class="d-flex flex-column gap-2 text-start col col-md-8">
                            <h6 class="fw-bold">Description</h6>
                            <p class="text-secondary">{{ experiance.description }}</p>
                        </div>
                        <hr>
                    </div>
                </div>

                <div class="tab-pane fade show col p-4" id="skills" role="tabpanel" aria-labelledby="skills-tab"
                    tabindex="0">
                    <div class="flex flex-column text-start" v-for="skill in data.skills" :key="skill">
                        <h6>{{ skill.title }}</h6>
                        <div class="progress" role="progressbar" :aria-label="skill.title"
                            :aria-valuenow="skill.percentage" aria-valuemin="0" aria-valuemax="100">
                            <div class="progress-bar bg-warning progress-bar-striped progress-bar-animated"
                                :style="'width:' + skill.percentage + '%'">{{ skill.percentage }}%
                            </div>
                        </div>
                        <hr>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="loading">
            <div class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>
        <div v-if="error">
            <span><i class="ri-error-line fs-1"></i></span>
        </div>
        <div v-if="data == null" class="border p-5 border-dark rounded container m-auto">
            <span class="d-flex align-items-center gap-2 justify-content-center"><i class="ri-box-3-line fs-1"></i> Empty</span>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "MyResume",
    components: {
    },
    data() {
        return {
            data: null,
            error: false,
            loading: true
        }
    },
    methods: {

    },
    mounted() {
        axios.get("http://127.0.0.1:8000/api/v1/resume/")
            .then(response => this.data = response.data)
            .catch(() => this.error = false)
            .finally(() => this.loading = false)
    },
    watch: {
        $route() {
            axios.get("http://127.0.0.1:8000/api/v1/resume/")
                .then(response => this.data = response.data)
                .catch(() => this.error = false)
                .finally(() => this.loading = false)
        }
    },
}
</script>