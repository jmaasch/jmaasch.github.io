<div class="name">
  <p align="center" style="font-size:40px">
    <b>JACQUELINE R.M.A. MAASCH</b>
  </p>
</div>

<div class="topnav">
  <p align="center">
  <a href="home.html" style="color: rgb(0,0,0)"><font color="000000">HOME</font></a>&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="about.html" style="color: rgb(0,0,0)"><font color="000000">ABOUT</font></a>&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="pubs.html" style="color: rgb(0,0,0)"><font color="000000">PUBLICATIONS + PRESENTATIONS</font></a>&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="projects.html" style="color: rgb(0,0,0)"><font color="000000">PROJECTS</font></a>&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="resume_05_2020.pdf" style="color: rgb(0,0,0)" target="_blank"><font color="000000">CURRICULUM VITAE</font></a> 
</p>
</div>

---------------------------------------

<meta charset="utf-8">
<body>
<script src="https://d3js.org/d3.v4.min.js"></script>
<script src="https://d3js.org/d3-timer.v1.min.js"></script>

<script>
var width = 7000,
    height = 500;

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)
    .style("background", "#111")
    .append("g")
    .attr("transform", "translate(" + [width / 2, height / 2] + ")");

var spiral = svg.append("path")
    .attr("fill", "none")
    .attr("stroke", "#d1d1d1")
    .attr("stroke-opacity", 1)
    .attr("stroke-width", 0.5);

// Equation adapted from http://goatlink.deviantart.com/art/lissajous-curves-338721857

var range = d3.range(-60 * Math.PI, 15 * Math.PI, 0.05);

d3.timer(function(t) {
    var d = "M";

    for (var i = 0; i < range.length; i++) {
        var p = range[i];
        d += 0.1 * width * (Math.sin(3 * p + t / 2000) + Math.sin(3 * p + t / 1000));
        d += ",";
        d += 0.1 * height * (Math.sin(6 * p + t / 4000) + Math.sin(1.01 * p + t / 1000));
        if (i != range.length - 1) d += "L";
    }

    d.length--;
    spiral.attr("d", d);

    svg.attr("transform", "translate(250,250)rotate(" + 360 * (t % 100000 / 100000) + ")")})

</script>
