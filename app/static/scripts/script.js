function input(e) {
    /** get the input box and add the clicked number button to the box
     *
     * @type {HTMLElement}
     */
    var tbInput = document.getElementById("tbInput");
    tbInput.value = tbInput.value + e.value;
}

function del() {
    /** get the input box and remove the last char
     *
     * @type {HTMLElement}
     */
    var tbInput = document.getElementById("tbInput");
    tbInput.value = tbInput.value.substr(0, tbInput.value.length - 1);
}

function space(){
    /** get the input box and add a char
     *
     * @type {HTMLElement}
     */
    var tbInput = document.getElementById("tbInput");
    tbInput.value = tbInput.value + " ";
}

function clearAll(){
    /** clear the input box
     *
     * @type {HTMLElement}
     */
    var tbInput = document.getElementById("tbInput");
    tbInput.value = "";
}

function load() {
    /** get the input buttons and add a number to each of them from 0-9
     *
     * @type {HTMLElement}
     */

    for (let i = 0; i < 10; i++) {
        var btn = document.getElementById("btn" + i);
        btn.value = i;
        console.log()
    }
}