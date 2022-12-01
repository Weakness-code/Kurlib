let all = takeAllImages('/static/kurlib/images/church/church1.png', '/static/kurlib/images/flag/slider__flag-img.png', '/static/kurlib/images/bolotnov/bolotnov1.png');
let allText = takeAllText('Картинка один бла бла', 'Картинка два бла', 'Картинка три');
followEvent('.poster__arrow--left', '.poster__arrow--right', '.poster__item-img', '.poster__item-text', all, allText);