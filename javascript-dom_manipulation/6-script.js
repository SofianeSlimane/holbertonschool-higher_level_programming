const div = document.getElementById('character');
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(res => res.json())
  .then(data => div.textContent = data.name);
