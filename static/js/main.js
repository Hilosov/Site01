document.body.addEventListener("click", function(){
    var second = document.getElementsByClassName("logo");
    addMessage(second, "Event: click");
})