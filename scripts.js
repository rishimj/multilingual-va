function time_update() {
    const dat = new Date();   
    let curHr = dat.getHours();
    if (curHr < 12) {
        var greet = document.getElementsByClassName("greeting");
        for (var i = 0; i < greet.length; i++) {
            greet[i].innerHTML = "Good Morning";
        }
    } else if (curHr < 18) {
        var greet = document.getElementsByClassName("greeting");
        for (var i = 0; i < greet.length; i++) {
            greet[i].innerHTML = "Good Afternoon";
        }
    } else {
        var greet = document.getElementsByClassName("greeting");
        for (var i = 0; i < greet.length; i++) {
            greet[i].innerHTML = "Good Evening";
        }
    }
}

async function loaderclose() {
  var loadIcon = document.getElementsByClassName("gooey");

  await sleep(4000);
  loadIcon[0].style.display = "none";
  notification("Welcome to Mercury");
}

async function loaderDisplay() {
  var loadIcon = document.getElementsByClassName("gooey");
  loadIcon[0].style.display = "block";
  var funnyText = document.getElementById("introText");
  funnyText.style.display = "none";
  await sleep(750);
  loadIcon[0].style.display = "none";
}


function replaceVidImg(response) {
  var src = "data:image/png;base64,"
  src += String(response.message);
  var vidImgContainer = document.getElementById("videoImg");
  vidImgContainer.src = src;
}

function sleep(milliseconds) {
  return new Promise(resolve => setTimeout(resolve, milliseconds));
}

function notification(content) {
  var x = document.getElementById("snackbar");
  x.innerHTML = content;
  x.className = "show";
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}

