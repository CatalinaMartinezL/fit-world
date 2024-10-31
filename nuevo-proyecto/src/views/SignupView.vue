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
    async submitForm() {
      const signupData = {
        name: this.name,
        class_name: this.selectedClass,
        gym_name: this.selectedGym
      };

      try {
        const response = await fetch('http://127.0.0.1:5000/api/signup', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(signupData)
        });

        if (!response.ok) throw new Error('Failed to sign up');

        const result = await response.json();
        console.log('Signup successful:', result);
        // Optionally redirect or show a success message
        this.resetForm();
      } catch (error) {
        console.error(error);
      }
    },
    resetForm() {
      this.name = '';
      this.surname = '';
      this.dni = '';
      this.selectedClass = '';
      this.selectedGym = '';
    }
  },
};
</script>

<style scoped>
.signup-view {
  text-align: center;
  padding: 20px;
}
</style>
