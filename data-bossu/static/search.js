const searchBar = document.getElementById('search');
let button = document.getElementById('button');

function search() {
    window.location = link + '/sneeze?search=' + searchBar.value;
}
