const header = document.querySelector('header');
const div = document.getElementById('update_header');

div.addEventListener('click', () => {
  header.textContent = 'New Header!!!';
});
