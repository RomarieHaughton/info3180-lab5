<template>
  <form id="movieForm" @submit.prevent="saveMovie">
    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input type="text" name="title" class="form-control" v-model="movie.title" />
    </div>
    <div class="form-group mb-3">
      <label for="description" class="form-label">Description</label>
      <textarea name="description" class="form-control" v-model="movie.description"></textarea>
    </div>
    <div class="form-group mb-3">
      <label for="poster" class="form-label">Poster</label>
      <input type="file" name="poster" class="form-control" @change="handleFileUpload" />
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
</template>

<script setup>
import { ref, onMounted } from "vue";

let movie = ref({
  title: "",
  description: "",
  poster: null,
});

let csrf_token = ref("");

function handleFileUpload(event) {
  movie.value.poster = event.target.files[0];
}

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token;
    });
}

function saveMovie() {
  let movieForm = document.getElementById('movieForm');
  let form_data = new FormData(movieForm);
  fetch("/api/v1/movies", {
    method: 'POST',
    body: form_data,
    headers: {
      'X-CSRFToken': csrf_token.value,
    },
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      console.log(data);
      // Display a success message
    })
    .catch(function (error) {
      console.log(error);
    });
}

onMounted(() => {
  getCsrfToken();
});
</script>