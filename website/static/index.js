let image = document.querySelector("#parImage");
let svg = image.querySelector("svg");

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


  let X = (-((event.clientX - CTM.e) / CTM.a)) + 40;
  let Y = (-((event.clientY - CTM.f) / CTM.d)) + 30;

  svg.viewBox.baseVal.x = (X - x);
  svg.viewBox.baseVal.y = (Y - y);
 
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




var path = document.getElementById('myPath');
var popup = document.getElementById('popupid');

// Add a click event listener to the path
path.addEventListener('click', function (event) {
    // Get the bounding box of the path
    var pathRect = path.getBoundingClientRect();

    var popup2 = document.getElementById("myPopup");
    popup2.classList.toggle("show");

    // Set the popup position above the path
    // Calculate the position of the popup
    

    var popupX = pathRect.left + window.scrollX;
    var popupY = pathRect.top + window.scrollY;

    // Set the popup position
    popup.style.left = popupX + 'px';
    popup.style.top = popupY + 'px';

    // Set the popup position
    var x = event.clientX;
    var y = event.clientY;
   
    popup.style.display = 'inline-block';


});

// Add a click event listener to the document to hide the popup when clicked outside
document.addEventListener('click', function (event) {
    if (!path.contains(event.target) && !popup.contains(event.target)) {
        // Clicked outside the path and popup, hide the popup
        popup.style.display = 'none';

        var popup2 = document.getElementById("myPopup");
        popup2.classList.remove("show");
    }
});