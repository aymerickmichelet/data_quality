const Step = ["BEFORE", "LOADING", "RESULT"]
let index = 0;

function switchStep(){
    index < 2 ? index++ : index=0
    displayStep()
}


function displayStep(){
    let inner_square = document.getElementById("inner_square")
    let loader = document.getElementById("loader")
    let upload = document.getElementById("upload")
    let csv_icon = document.getElementById("csv_icon")
    let label = document.getElementById("label")

    if (index === 0){
        inner_square.classList.add("pointer")
        loader.classList.add("hide")
        upload.removeAttribute("disabled")
        csv_icon.classList.remove("hide")
        label.classList.remove("hide")
    }else if (index === 1) {
        inner_square.classList.remove("pointer")
        loader.classList.remove("hide")
        upload.setAttribute("disabled", "")
        csv_icon.classList.add("hide")
        label.classList.add("hide")
    }
}

displayStep()
