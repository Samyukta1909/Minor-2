function techStackpopup() {
    document.querySelector(".tech-stack-card").style.visibility = 'visible';
    document.querySelector("header").style.filter = "blur(2px)";
}

function techStackpopout() {
    document.querySelector(".tech-stack-card").style.visibility = 'hidden';
    document.querySelector("header").style.filter = "blur(0px)";
}