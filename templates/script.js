// Steps: BEFORE=0/LOADING=1/RESULT=2
let index = 0;

const displayStep = () => {
    const inner_square = document.getElementById("inner_square")
    const loader = document.getElementById("loader")
    const upload = document.getElementById("upload")
    const csv_icon = document.getElementById("csv_icon")
    const label = document.getElementById("label")

    if (!index){ // index === 0
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

const switchStep = () => {
    index < 2 ? index++ : index = 0
    displayStep()
}

displayStep()
