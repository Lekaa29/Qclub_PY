let image = document.querySelector("#parImage");
let svg = image.querySelector("svg");
//let vbVals = svg.getAttribute("viewBox").split(" ");

let CTM = svg.getScreenCTM();

let x = 0;
let y = 0;
let z = 0;
let w = 0;

window.onload = function() {
  image.addEventListener('mousedown', startDrag);
  image.addEventListener('mouseup', endDrag);
  image.addEventListener('mouseleave', endDrag);
}

function drag() {
  event.preventDefault();

  //x += 0.1;

  let X = (-((event.clientX - CTM.e) / CTM.a)) + 40;
  let Y = (-((event.clientY - CTM.f) / CTM.d)) + 30;

  svg.viewBox.baseVal.x = (X - x);
  svg.viewBox.baseVal.y = (Y - y);
  /*svg.setAttribute("viewBox",
    (X - x) + " " +
    (Y - y) + " " +
    vbVals[2] + " " +
    vbVals[3]);*/
}


function startDrag() {
  image.addEventListener('mousemove', drag);

  x = (-((event.clientX - CTM.e) / CTM.a)) + 40;
  y = (-((event.clientY - CTM.f) / CTM.d)) + 30;

  //vbVals = svg.getAttribute("viewBox").split(" "); /* added this */
  x -= /*parseFloat(vbVals[0])*/ svg.viewBox.baseVal.x;
  y -= /*parseFloat(vbVals[1])*/ svg.viewBox.baseVal.y;

  z = /*parseFloat(vbVals[2])*/ svg.viewBox.baseVal.width;
  w = /*parseFloat(vbVals[3])*/ svg.viewBox.baseVal.height;
}

function endDrag() {
  image.removeEventListener("mousemove", drag);
}