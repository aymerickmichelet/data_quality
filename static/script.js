const SPINNER_DURATION_MS = 1000;

document.querySelector('#upload')
    .addEventListener('change', event => {
        showSpinner();
        setTimeout(function() {
            document.querySelector('#formUpload').submit();
        }, SPINNER_DURATION_MS);
    })


const showSpinner = () => {
    const inner_square = document.getElementById("inner_square")
    const loader = document.getElementById("loader")
    const xlsx_icon = document.getElementById("xlsx_icon")
    const label = document.getElementById("label")

    inner_square.classList.remove("pointer")
    loader.classList.remove("hide")
    xlsx_icon.classList.add("hide")
    label.classList.add("hide")
}