function submit() {
    const myObj = {
        name : document.getElementById("name").value,
        title : document.getElementById("title").value,
        body : document.getElementById("body").value,
        creator : document.getElementById("creator").value,
    };
    const myJSON = JSON.stringify(myObj);
    
    console.log(myJSON);

    window.location = "http://localhost:8080/create_sneeze?x=" + myJSON;
}
