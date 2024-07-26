document.addEventListener('DOMContentLoaded', () => {
  const myDiv = document.getElementById('hello');
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(res => res.json())
    .then((data) => {
      myDiv.textContent = data.hello;
    });
});
