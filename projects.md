<div class="topnav">
  <a href="about.html" style="color: rgb(0,0,0)"><font color="000000">ABOUT</font></a>&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="pubs.html" style="color: rgb(0,0,0)"><font color="000000">PUBLICATIONS + PRESENTATIONS</font></a>&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="projects.html" style="color: rgb(0,0,0)"><font color="000000">PROJECTS</font></a>&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="cv.html" style="color: rgb(0,0,0)"><font color="000000">CURRICULUM VITAE</font></a> 
</div>

# PROJECTS

## R packages

### ```sanzo``` R Color Palettes Based on the Works of Sanzo Wada.

Inspired by the art and color research of Sanzo Wada (1883-1967), his <a href="http://seigensha.com/en/2016/11/01/978-4-86152-247-5/" style="color: rgb(167,55,75)" target="_blank"><font color="A7374B">Dictionary Of Color Combinations</font></a>, and the incredible <a href="https://github.com/dblodorn/sanzo-wada" style="color: rgb(167,55,75)" target="_blank"><font color="A7374B">interactive site</font></a> by Dain M. Blodorn Kim, this package brings Wada's color combinations to R for easy use in data visualizations. This package honors 60 of Wada's color combinations: 20 duos, 20 trios, and 20 quads.

<a href="https://github.com/jmaasch/sanzo/" style="color: rgb(167,55,75)" target="_blank"><font color="A7374B">github.com/jmaasch/sanzo/</font></a>

<img src="https://user-images.githubusercontent.com/50045763/71492000-268c5c80-2802-11ea-8ceb-fd8f12784bed.png" align="middle"/>

<html>
<head>
  <meta charset="utf-8">
  <style type="text/css">
    svg {
      background-color: #b3e8c2;
      width: 400px;
      height: 400px;
    }
    circle {
      fill: #ff5200;
    }
  </style>
</head>
<body>
<svg></svg>
</body>
<script src="https://d3js.org/d3.v4.min.js"></script>
<script src="https://d3js.org/d3-timer.v1.min.js"></script>
<script type="text/javascript">
// Adapted from https://bl.ocks.org/pvernier/2ba5a32840c7d5125afe071c6b68e5ac
// Colors from sanzo R package.
  var circle = d3.select("svg")
                 .append("circle")
                 .attr("cx", 370)
                 .attr("cy", 200)
                 .attr("r", 30)
  d3.interval(function(elapsed) {
    circle.transition()
          .attr("cx", 200)
          .attr("cy", 370)
          .style("fill", "#FF616B")
          .transition()
          .attr("cx", 30)
          .attr("cy", 200)
          .style("fill", "C9303E")
          .transition()
          .attr("cx", 200)
          .attr("cy", 30)
          .style("fill", "681916")
          .transition()
          .attr("cx", 370)
          .attr("cy", 200)
          .style("fill", "C74300")
    }, 1000);
</script>
</html>
