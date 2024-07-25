const myDivId = document.getElementById('add_item');
const myList = document.querySelector('.my_list');

myDivId.addEventListener('click', () => {
  const item = document.createElement('li');
  item.textContent = 'Item';
  myList.appendChild(item);
});
