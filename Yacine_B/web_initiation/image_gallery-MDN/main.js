let displayedImage = document.getElementById("displayed");
let toDisplayImages = document.getElementsByClassName("to-display-img");
let lumButton = document.getElementById("luminosity-btn");
let veilDiv = document.getElementById("veil");


function getUrl(div) {
    // Return the background image url for a given element.
    return window.getComputedStyle(div).backgroundImage;
}

function display(evt) {
    // Set a new displayed image url with the one from the clicked element.
    displayedImage.style.backgroundImage = getUrl(evt.target);
}

function toggleLuminosity(evt) {
    if (evt.target.textContent === "Darken") {
        veil.style.backgroundColor = "rgba(0, 0, 0, 0.5)";
        evt.target.textContent = "Lighten";
    }
    else {
        veil.style.backgroundColor = "rgba(0, 0, 0, 0.0)";
        evt.target.textContent = "Darken";
    }
}

lumButton.addEventListener("click", toggleLuminosity);

for (let i = 0; i < toDisplayImages.length; i++) {
    toDisplayImages[i].addEventListener("click", display);
}
