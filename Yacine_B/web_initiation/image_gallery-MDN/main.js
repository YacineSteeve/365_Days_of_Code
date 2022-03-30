const displayedImage = document.getElementById("displayed");
const toDisplayImages = document.getElementsByClassName("to-display-img");
const lumButton = document.getElementById("luminosity-btn");


function getUrl(div) {
    // Return the background image url for a given element.
    return window.getComputedStyle(div).backgroundImage;
}

function display(evt) {
    // Set a new displayed image url with the one from the clicked element.
    displayedImage.style.backgroundImage = getUrl(evt.target);
}

for (let i = 0; i < toDisplayImages.length; i++) {
    toDisplayImages[i].addEventListener("click", display);
}
