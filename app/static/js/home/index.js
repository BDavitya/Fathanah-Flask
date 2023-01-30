function currentTime() {
    let date = new Date(); 
    let hh = date.getHours();
    let mm = date.getMinutes();
    let ss = date.getSeconds();
    hh = (hh < 10) ? "0" + hh : hh;
    mm = (mm < 10) ? "0" + mm : mm;
    ss = (ss < 10) ? "0" + ss : ss;
    let time = hh + "  :  " + mm;
    document.getElementById("clock").innerText = time; 
    let t = setTimeout(function(){ currentTime() }, 1000);  
}

currentTime();

function currentDate() {
    const days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
    const months = ["January","February","March","April","May","June","July","August","September","October","November","December"];
    const d = new Date();
    let day = days[d.getDay()];
    let date = d.getDate();
    let month = months[d.getMonth()];
    let year = d.getFullYear();
    let data = day + ", " + date + " " + month + " " + year;
    document.getElementById("date").innerText = data; 
    let t = setTimeout(function(){ currentDate() }, 1000);  
}

currentDate();

let using = document.getElementById("usingMyDiary").value;
let user = document.getElementById("manyUser").value;
let notUsing = user - using;
var xValues = ["Using MyDiary", "Just Registration"];
var yValues = [using, notUsing];
var barColors = [
  "#FFD700",
  "#00692D"
];
new Chart("myChart", {
  type: "pie",
  data: {
    labels: xValues,      
    hoverOffset: 4,
    datasets: [{
      backgroundColor: barColors,
      data: yValues,
      borderColor: '000',
      color:'000',
    }]
  }
}); 