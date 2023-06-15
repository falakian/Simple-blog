const url = "http://127.0.0.1:5000/api/fetch";

async function getcount(url) {
    let x = await fetch(url);
    let y = await x.text();
    document.getElementById("count2").innerHTML = `Number of users :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ${y} `;  }
getcount(url);