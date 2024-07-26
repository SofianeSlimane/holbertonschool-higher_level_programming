const myId = document.getElementById('red_header');
const myHeader = document.querySelector('header');
myId.addEventListener('click', () => {
  myHeader.classList.add('red');
});
