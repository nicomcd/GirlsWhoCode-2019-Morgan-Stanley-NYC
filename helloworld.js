console.log("Hello World!");
var names = ['NICOLE', 'NIKI', 'NIK', 'NIKKI', 'NICO'];
var pos = 0;
var loc = document.getElementById('specialfont');

function changeNames(){
  loc.innerHTML = names[pos];
  pos ++;
  if (pos >= names.length){
    pos = 0;
  }
}


var colors = ["black", "red", "green", "blue", "yellow", "purple", "orange"];
var coz = 0;

function changeColor(){
  loc.style.color = colors[coz];
  coz ++;
  if (coz >= colors.length){
    coz = 0;
  }
}


var fonts = ["'Darker Grotesque', sans-serif, 'Bonbon', cursive, 'Hanalei', cursive"];
var poz = 0;

function changeFont(){
  loc.style.fontFamily = fonts[poz];
  //foz.setAttribute("style", 'font-family: ${fonts[poz]}');
  //like f"{}" in python
  poz ++;
  if (poz >= fonts.length){
    poz = 0;
  }
}


document.getElementById("specialfont").addEventListener("click",
  function(){
    alert("You've downloaded a virus!");
      document.getElementById("specialfont").style.color = "pink";
      changeNames();
      changeFont();
  }
)
