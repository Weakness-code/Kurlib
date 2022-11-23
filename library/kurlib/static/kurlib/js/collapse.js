let coll = document.getElementsByClassName("about__list-item--for-open");

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
      this.classList.toggle("active");
      let content = this.nextElementSibling;
    //   let img = this.firstChild;
    //   console.log(img);
    let img = this.firstChild.nextElementSibling;
      if (content.style.display === "block") {
        content.style.display = "none";
        img.src = "/static/kurlib/images/about/about__item-img2.png";
      } else {
        content.style.display = "block";
        img.src = "/static/kurlib/images/about/about__item-img4.png";
      }
    });
}