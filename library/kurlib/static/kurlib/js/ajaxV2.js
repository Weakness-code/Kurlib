let pageCounter = 1;
let container = document.querySelector(".new-books__wrapper");
let btn = document.querySelector(".new-books__button");
console.log(btn);

window.onload = function () {
    let ourRequest = new XMLHttpRequest();
    ourRequest.open('GET', '/static/kurlib/js/bookJSON-0.json');
    ourRequest.onload = function() {
      if (ourRequest.status >= 200 && ourRequest.status < 400) {
        let ourData = JSON.parse(ourRequest.responseText);
        renderHTML(ourData);
          console.log('сработало');
      } else {
        console.log("We connected to the server, but it returned an error.");
      }
      
    };
  
    ourRequest.onerror = function() {
      console.log("Connection error");
    };
  
    ourRequest.send();
}

btn.addEventListener("click", function() {
  let ourRequest = new XMLHttpRequest();
  ourRequest.open('GET', '/static/kurlib/js/bookJSON-' + pageCounter + '.json');
  ourRequest.onload = function() {
    if (ourRequest.status >= 200 && ourRequest.status < 400) {
      let ourData = JSON.parse(ourRequest.responseText);
      renderHTML(ourData);
        // console.log(ourData[0].name);
    } else {
      console.log("We connected to the server, but it returned an error.");
    }
    
  };

  ourRequest.onerror = function() {
    console.log("Connection error");
  };

  ourRequest.send();
  pageCounter++;
  if (pageCounter > 3) {
    btn.style.display = "none";
  }
});



function renderHTML(data) {
    // отрисуй для каждого объекта свою карточку
    for (i = 0; i < data.length; i++) {
        drawCards(data[i].name, data[i].author, data[i].src);
    }
}

function drawCards (nameP, authorP, srcP) {
    // получи все параметры для отрисовки
    let name = nameP,
        author = authorP,
        src = srcP;

    
    // создай все необходимые элементы, задай им классы
    let item = document.createElement('div');
    item.classList.add("new-books__item");

    let bg = document.createElement('div');
    bg.classList.add("new-books__item-bg");

    let img = document.createElement('img');
    img.classList.add("new-books__item-img");

    let info = document.createElement('div');
    info.classList.add("new-books__info");

    let nameOfBook = document.createElement('h5');
    nameOfBook.classList.add("new-books__name");
    
    let authorOfBook = document.createElement('h6');
    authorOfBook.classList.add("new-books__author");

    // займись вложенностью
    // можно было бы короче, но так понятнее    
    container.appendChild(item);
    item.appendChild(bg);
    item.appendChild(img);
    item.appendChild(info);
    info.appendChild(nameOfBook);
    info.appendChild(authorOfBook);

    // разметка готова, стили в файлах


    // займись подстановкой небходмой инфы
    nameOfBook.innerHTML = name;
    authorOfBook.innerHTML = author;
    img.src = src;


}