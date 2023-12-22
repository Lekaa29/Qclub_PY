
let image = document.querySelector("#parImage");
let svg = image.querySelector("svg");

let CTM = svg.getScreenCTM();

let clickedTableIndex = null;

let x = 0;
let y = 0;
let z = 0;
let w = 0;

function startDrag(event) {
  if (event.buttons !== 1) {
    // Check if the left mouse button is pressed
    return;
  }

  image.addEventListener('mousemove', drag);

  var popup = document.getElementById('popupid');

  popup.style.left = 0 + 'px';
  popup.style.top = 0 + 'px';

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



function drag() {
  event.preventDefault();


  let X = (-((event.clientX - CTM.e) / CTM.a)) + 40;
  let Y = (-((event.clientY - CTM.f) / CTM.d)) + 30;

  svg.viewBox.baseVal.x = (X - x);
  svg.viewBox.baseVal.y = (Y - y);
 
}



window.onload = function() {
  image.addEventListener('mousedown', startDrag);
  //image.addEventListener('mouseup', endDrag);
  //image.addEventListener('mouseleave', endDrag);
  // Get all elements with the class "table"
  document.addEventListener('mouseup', endDrag);
  var tables = document.querySelectorAll('.table');


  document.addEventListener('mouseup', function () {
    var popup = document.getElementById('popupid');
    popup.classList.remove('show');
  });
  
  // Add click event listener to each table element
  tables.forEach(function(table) {
    table.addEventListener('click', function(event) {
      // Get the bounding box of the clicked table
      var tableRect = table.getBoundingClientRect();

      // Get the popup element
      var popup = document.getElementById('popupid');

      // Toggle the "show" class on the popup to display or hide it
     // popup.classList.toggle('show');

      clickedTableIndex = index;

      // Set the popup position above the clicked table
      var popupX = tableRect.left + window.scrollX + tableRect.width / 2 - popup.offsetWidth / 2;
      var popupY = tableRect.top + window.scrollY;

      // Set the popup position
      popup.style.left = popupX + 'px';
      popup.style.top = popupY + 'px';

      // Prevent the click event from propagating to the document click listener
      event.stopPropagation();
      
    });

    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
      // Access the clickedTableIndex here and include it in the form data
      if (clickedTableIndex !== null) {
        // Include clickedTableIndex in the form data
        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'clickedTableIndex';
        input.value = clickedTableIndex;
        form.appendChild(input);
      }
    });

  });

  // Add a click event listener to the document to hide the popup when clicked outside
  document.addEventListener('click', function(event) {
    var popup = document.getElementById('popupid');
    if (!popup.contains(event.target)) {
      // Clicked outside the popup, hide it
      popup.style.left = 0 + 'px';
      popup.style.top = 0 + 'px';
      clickedTableIndex = null;
    }
    });
  };

