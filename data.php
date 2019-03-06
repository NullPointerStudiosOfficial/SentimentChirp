
<!DOCTYPE HTML> 
<html>
<head>
<script>
window.onload = function () {
var chart = new CanvasJS.Chart("chartContainer", {
   title: {
        text: "Popularity"
    },
    axisX: {	  
       valueFormatString: "DDDD"
    },
    axisY2: {
        title: "Tweets",
        suffix: " Tweets"
    },
    toolTip: {
        shared: true
    },
    legend: {
        cursor: "pointer",
        verticalAlign: "top",
        horizontalAlign: "center",
        dockInsidePlotArea: true,
        itemclick: toogleDataSeries
    },
    data: [{
        type: "line",
        axisYType: "secondary",
        name: "None",
        showInLegend: true,
        markerSize: 0,
        yValueFormatString: "# Sentiments,",
        dataPoints: [
        {x: new Date(2019, 02, 24), y: 0.06650384199134199},
        {x: new Date(2019, 02, 25), y: 0.050742334054834075},
        {x: new Date(2019, 02, 26), y: 0.1294559365981241},
        {x: new Date(2019, 02, 27), y: 0.021237689393939392},
        {x: new Date(2019, 02, 28), y: 0.07731527326839827},
        {x: new Date(2019, 03, 01), y: 0.015951298701298695},
        {x: new Date(2019, 03, 02), y: 0.09849242424242427},
        {x: new Date(2019, 03, 03), y: 0.07939118867243869},
       ]
    }]
});
chart.render();
function toogleDataSeries(e){
 if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible    ) {
     e.dataSeries.visible = false;
 } else{
     e.dataSeries.visible = true;
 }
 chart.render();
}
}
 </script>
</head>
 <?php if (isset($_GET['hello'])) { exec('c:\WINDOWS\system32\cmd.exe /c START C:\MAMP\htdocs\RunFile.py'); } ?>
<body>
<form name="search" method="get">
      <input type="text" data_test="twitter_handle" style="height: 50px; width: 50%; margin-left: 25%; margin-top: 5%;">
</form>
<a href = "?hello=true">.</a>
  <div id="chartContainer" style="height: 370px; width: 80%; margin-top: 10%; margin-left: 10%;"></div>
	<script src="graph.js"></script>
<a href = "?hello=true">.</a>
</body>
<style>
   input {
      font-size: 2em;
      text-align: center;
      border: 0;
      outline: 0;
      background: transparent;
      border-bottom: 1px solid black;
  }
</style>
</html>