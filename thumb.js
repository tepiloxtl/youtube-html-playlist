function forOthers(e)
{
 if (document.getElementById('thumb').style.visibility == "visible")
 {
  hor = window.scrollX + window.innerWidth - 240 - 20;
  //console.log("hor: " + hor);
  //console.log(window.scrollX)
  //console.log(window.innerWidth)
  //console.log(document.getElementById('thumb').offsetWidth)
  ver = window.scrollY + window.innerHeight - 180 - 20;
  //console.log("ver: " + ver);
  posHor = window.scrollX + e.clientX + 10;
  //console.log("posHor: " + posHor);
  posVer = window.scrollY + e.clientY + 10;
  //console.log("posVer: " + posVer);
  posHor2 = window.scrollX + e.clientX - 240 - 5;
  //console.log("posHor2: " + posHor2);
  posVer2 = window.scrollY + e.clientY - 180 - 5;
  //console.log("posVer2: " + posVer2);
  if (posVer<ver)
   document.getElementById('thumb').style.top = posVer + "px";
  else
   document.getElementById('thumb').style.top = posVer2 + "px";

  if (posHor<hor)
   document.getElementById('thumb').style.left = posHor + "px";
  else
   document.getElementById('thumb').style.left = posHor2 + "px";
 }
}
function showthumb(x,z)
{
 if (x == '')
  temp = ''
 else
  temp = "<table class='thumb' border=0 width=270 cellspacing=1 cellpadding=0><tr><td width=1 valign=bottom><img border=1 src=thumbs/" + x + ".jpg width=240 height=180></td></tr></table>";
  document.onmouseover = forOthers;
  document.onmousemove = forOthers;
  document.getElementById('thumb').innerHTML = temp;
  document.getElementById('thumb').style.width = 240;
  if (z == 1)
   document.getElementById('thumb').style.visibility = "visible";
  else
   document.getElementById('thumb').style.visibility = "hidden";
}