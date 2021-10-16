// submenu script 

let submenu = document.querySelectorAll(".menu li");
let submenu1 = document.querySelector(".submenu");

submenu.forEach(item => item.addEventListener("click", (event) => {

    item.classList.toggle("show");

}));

let continer = document.querySelector(".content")
continer.onclick = function(e) {

    if (e.target.id !== 'side-bar' && e.target.id !== "slideing") {
        document.querySelector(".side-bar").classList.remove("slideing");
    }

}

document.querySelector(".close-btn").addEventListener("click", () => {

    document.querySelector(".side-bar").classList.remove("slideing");

});
document.querySelector(".open-menu").addEventListener("click", () => {

    document.querySelector(".side-bar").classList.toggle("slideing");

});


let loginform = document.querySelector("form.login");
let signupform = document.querySelector("form.signup");
let loginBtn = document.querySelector("label.login");
let signupBtn = document.querySelector("label.signup");
let signupLink = document.querySelector(".signup-link");
let loginText = document.querySelector(".title-text .login");
let signupText = document.querySelector(".title-text .signup");


signupBtn.addEventListener("click", () => {

    loginform.style.marginLeft = "-50%";
    loginText.style.marginLeft = "-50%";

});

loginBtn.addEventListener("click", () => {

    loginform.style.marginLeft = "0%";
    loginText.style.marginLeft = "0%";
});


signupLink.addEventListener("click", (event) => {
    event.preventDefault();
    signupBtn.click();
});