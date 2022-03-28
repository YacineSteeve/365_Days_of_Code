const displayedImage = document.getElementById("displayed");
const toDisplayImages = document.getElementsByClassName("to-display-img");

function getUrl(div) {
    return window.getComputedStyle(div).backgroundImage;
}

function display(e) {
    displayedImage.style.backgroundImage = getUrl(e.target);
}

for (let i = 0; i < toDisplayImages.length; i++) {
    toDisplayImages[i].addEventListener("click", display);
}