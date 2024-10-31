<template>
  <div class="classes-view">
    <h1>Available Classes</h1>
    <div class="class-list">
      <div v-for="classItem in classes" :key="classItem.id" class="class-card">
        <h3>{{ classItem.name }}</h3>
        <p>{{ classItem.description }}</p>
        <p><strong>Horario:</strong> {{ classItem.schedule }}</p>
      </div>
    </div>
    
    <router-link :to="{ name: 'signup' }">
      <button class="signup-button">Sign Up Now</button>
    </router-link>
  </div>
</template>

<script>
import classesData from '../data/classes.json';

export default {
  data() {
    return {
      classes: classesData,
    };
  },
};
</script>

<style scoped>
.classes-view {
  text-align: center;
  background-color: #f9f9f9;
  padding: 20px;
}
.class-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
.class-card {
  border: 1px solid #ddd;
  padding: 20px;
  margin: 10px;
  width: 250px;
  border-radius: 8px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
}
.signup-button {
  margin-top: 20px;
  padding: 12px 24px;
  background-color: #ff4500;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.signup-button:hover {
  background-color: #e03e00;
}
</style>
