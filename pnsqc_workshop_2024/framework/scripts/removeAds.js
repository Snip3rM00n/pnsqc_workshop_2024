var all = document.getElementsByTagName("*");

for (var i = 0; i < all.length; i++){
    element = all[i];
    for (var j = 0; j < element.attributes.length; j++){
        if (element.attributes[j].value.includes("Ad.")){
            element.remove();
        }
    }
}