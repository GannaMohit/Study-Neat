function displayMenuMobile(element) {
    menu_box = document.getElementById("menu_box");
    if (menu_box.style.display == "flex") {
        menu_box.style.display = "none";
    }
    else {
        menu_box.style.display = "flex";
    }
}