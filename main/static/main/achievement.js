function drop() {
    var a = document.getElementsByClassName('dropdown-content')
        a[0].style.display = 'block'
    setTimeout(drop2, 3000);
}
function drop2() {
    var a = document.getElementsByClassName('dropdown-content')
        a[0].style.display = 'none'
}