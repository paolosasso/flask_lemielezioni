var cps = 0
var maxcps = 0
var clicksthissecond = 0
var clicks = 0
if (localStorage.getItem('cps') != undefined) {
  clicksthissecond = localStorage.getItem('clicksthissecond')
  document.getElementById('t').innerHTML = maxcps + ' Cps'
  document.getElementById('n').innerHTML = cps + " Max Cps"
  document.getElementById('m').innerHTML = 'Clicks: ' + clicks
  document.getElementById('s').innerHTML = 'Secondi: ' + timeleft
}
setInterval(function () {
  cps = clicksthissecond;
  if (cps > maxcps) {
    maxcps = cps;
    document.getElementById('n').innerHTML = maxcps + ' Max Cps'
  }
  document.getElementById('t').innerHTML = cps + " Cps"
  clicksthissecond = 0;
}, 1000)

var timeleft = 10;

  var Timer = setInterval(function(){
    if(timeleft <= 0){
      clearInterval(Timer);
      document.getElementById("s").innerHTML = "Fine";
    } else {
      document.getElementById("s").innerHTML = timeleft + " Secondi";
    }
    timeleft -= 1;
  }, 1000);

function press() {
  clicksthissecond++;
  clicks++;
  document.getElementById('m').innerHTML = 'Clicks: ' + clicks;
}
