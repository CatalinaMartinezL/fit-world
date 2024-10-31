<template>
  <div class="signup-view">
    <h1>Sign Up for a Class</h1>
    <form @submit.prevent="submitForm">
      <label for="name">Name:</label>
      <input type="text" v-model="name" required />

      <label for="surname">Surname:</label>
      <input type="text" v-model="surname" required />

      <label for="dni">DNI:</label>
      <input type="text" v-model="dni" required />

      <label for="class">Class:</label>
      <select v-model="selectedClass" required>
        <option v-for="classItem in classes" :key="classItem.id" :value="classItem.name">
          {{ classItem.name }}
        </option>
      </select>

      <label for="gym">Select Gym:</label>
      <select v-model="selectedGym" required>
        <option v-for="gym in gyms" :key="gym" :value="gym">{{ gym }}</option>
      </select>

      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import classesData from '../data/classes.json';

export default {
  data() {
    return {
      name: '',
      surname: '',
      dni: '',
      selectedClass: '',
      selectedGym: '',
      classes: classesData,
      gyms: ['FitZone', 'PowerUp', 'Strength Hub', 'FlexFit', 'GymNation', 'The Arena', 'Peak Performance'],
    };
  },
  methods: {
    submitForm() {
      console.log(`Name: ${this.name}, Surname: ${this.surname}, DNI: ${this.dni}, Class: ${this.selectedClass}, Gym: ${this.selectedGym}`);
    },
  },
};
</script>

<style scoped>
.signup-view {
  text-align: center;
  padding: 20px;
}
</style>
