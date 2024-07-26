const myList = document.getElementById('list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(res => res.json())
  .then(data => {
    for (const obj of data.results) {
      const item = document.createElement('li');
      item.textContent = obj.title;
      myList.appendChild(item);
    }
  }
  );
