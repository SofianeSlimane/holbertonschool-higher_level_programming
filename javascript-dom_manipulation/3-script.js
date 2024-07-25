const myToggleHeaderId = document.getElementById('toggle_header');
const myHeader = document.querySelector('header');
myToggleHeaderId.addEventListener('click', () => {
  if (myHeader.className === 'green') {
    myHeader.classList.toggle('green');
    myHeader.classList.toggle('red');
  } else if (myHeader.className === 'red') {
    myHeader.classList.toggle('red');
    myHeader.classList.toggle('green');
  }
});
