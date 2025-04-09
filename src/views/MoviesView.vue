<template>
  <div class="movies-container">
    <div v-for="movie in movies" :key="movie.id" class="movie-card">
      <img :src="movie.poster" alt="Movie Poster" class="movie-poster" />
      <h3>{{ movie.title }}</h3>
      <p>{{ movie.description }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

let movies = ref([]);

function fetchMovies() {
  fetch('/api/v1/movies')
    .then((response) => response.json())
    .then((data) => {
      movies.value = data.movies;
    });
}

onMounted(() => {
  fetchMovies();
});
</script>

<style scoped>
.movies-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.movie-card {
  width: 300px;
  margin: 20px;
  padding: 10px;
  border: 1px solid #ddd;
  text-align: center;
}

.movie-poster {
  max-width: 100%;
  height: auto;
}
</style>