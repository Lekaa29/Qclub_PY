
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

  var rectElements = document.querySelectorAll('rect');


  document.addEventListener('mouseup', function () {
    var popup = document.getElementById('popupid');
    popup.classList.remove('show');
  });
  
  rectElements.forEach(function(rect) {
    rect.addEventListener('click', function(event) {
      // Get the id of the clicked rect element
      var clickedRectId = event.target.id;

      var clickedTableIndex = event.target.getAttribute('data-table-index');
  
      // Do something with the id
      console.log('Clicked rect element id:', clickedRectId);
      console.log('Clicked clickedTableIndex:', clickedTableIndex);

      //clickedTableIndex = clickedRectId;
      
      var hiddenInput = document.getElementById('clickedTableIndex');
      hiddenInput.value = clickedTableIndex;

  })});

  // Add click event listener to each table element
  tables.forEach(function(table, index) {
    table.addEventListener('click', function(event) {
      console.log('clickedTableIndex:', clickedTableIndex);

      // Get the bounding box of the clicked table
      var tableRect = table.getBoundingClientRect();

      // Get the popup element
      var popup = document.getElementById('popupid');

      var tables = tablesData; 
      
    
      var tableOwner = tables[index];
      console.log('Clicked table owner:', tables[index]);

      var popupContent = document.getElementById('popupContent');

      popupContent.innerHTML = '';

      

      if (table.classList.contains('taken')) {
        // If taken, display a message instead of the button
        var messageDiv = document.createElement('div');
        messageDiv.classList.add('popuptext'); // Apply the same class as the button
        messageDiv.innerText = tableOwner;
        popupContent.appendChild(messageDiv);
      } else {
        // If free, display the button as usual
        var reserveButton = document.createElement('button');
        reserveButton.classList.add('popuptext');
        reserveButton.id = 'myPopup';
        reserveButton.innerText = 'Reserve';
        popupContent.appendChild(reserveButton);

        var hiddenInput = document.getElementById('clickedTableIndex');
        hiddenInput.value = table.getAttribute('data-table-index');
      }
      // Toggle the "show" class on the popup to display or hide it
      popup.classList.toggle('show');
      
      // Set the popup position above the clicked table
      var popupX = tableRect.left + window.scrollX + tableRect.width / 2 - popup.offsetWidth / 2;
      var popupY = tableRect.top + window.scrollY;
      
      // Set the popup position
      popup.style.left = popupX + 'px';
      popup.style.top = popupY + 'px';
      
      // Prevent the click event from propagating to the document click listener
      event.stopPropagation();
    
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

