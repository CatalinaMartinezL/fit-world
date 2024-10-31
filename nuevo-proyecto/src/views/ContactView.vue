<template>
    <div class="contact">
      <h1>Contact Us</h1>
      <p>If you have any questions, feel free to reach out to us!</p>
      <p>Email: info@fitworld.com</p>
      <p>Phone: +1 (555) 123-4567</p>
      
      <h2>Affiliated Gyms</h2>
      <ul class="gym-list">
        <li><strong>Peak Performance Gym</strong> - Downtown</li>
        <li><strong>Elite Fitness Center</strong> - Eastside</li>
        <li><strong>Powerhouse Fitness</strong> - Midtown</li>
        <li><strong>Iron Haven Gym</strong> - West End</li>
        <li><strong>Core Strength Studio</strong> - Uptown</li>
        <li><strong>FlexZone</strong> - Riverside</li>
        <li><strong>PulseFit Gym</strong> - Northside</li>
      </ul>
  
      <router-link to="/">Back to Home</router-link>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ContactView'
  };
  </script>
  
  <style scoped>
  .contact {
    text-align: center;
    padding: 20px;
    font-family: 'Arial', sans-serif;
  }
  
  .gym-list {
    list-style-type: none;
    padding: 0;
    margin: 20px 0;
  }
  
  .gym-list li {
    font-size: 18px;
    margin: 5px 0;
    font-weight: bold;
    color: #333;
  }
  </style>
  