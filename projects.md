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

# PROJECTS

## R packages

### ```sanzo``` Color Palettes Based on the Works of Sanzo Wada.

Inspired by the art and color research of Sanzo Wada (1883-1967), his <a href="http://seigensha.com/en/2016/11/01/978-4-86152-247-5/" style="color: rgb(167,55,75)" target="_blank"><font color="A7374B">Dictionary Of Color Combinations</font></a>, and the incredible <a href="https://github.com/dblodorn/sanzo-wada" style="color: rgb(167,55,75)" target="_blank"><font color="A7374B">interactive site</font></a> by Dain M. Blodorn Kim, this package brings Wada's color combinations to R for easy use in data visualizations. This package honors 60 of Wada's color combinations: 20 duos, 20 trios, and 20 quads.

View the <a href="https://github.com/jmaasch/sanzo/" style="color: rgb(167,55,75)" target="_blank"><font color="A7374B">GitHub repository</font></a> for <a href="https://CRAN.R-project.org/package=sanzo" style="color: rgb(167,55,75)" target="_blank"><font color="A7374B">CRAN</font></a> install instructions, usage recommendations, and demo gallery.

<img src="https://user-images.githubusercontent.com/50045763/71599641-b5a6b680-2b19-11ea-8262-bdc7c26505b0.png" align="middle"/>

## Visualizing algorithms

### All watched over by machines of loving grace

<script>

// Set dimensions of SVG container.

var width = 550,
    height = 550;

// Build SVG container for visualization.

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)
    .style("background", "#baa600")
    .append("g")
    .attr("transform", "translate(" + [width / 2, height / 2] + ")");

// Append path for Lissajous curve.

var lissajous = svg.append("path")
    .attr("fill", "none")
    .attr("stroke", "#e62e73")
    .attr("stroke-opacity", 1)
    .attr("stroke-width", 0.5)
    .attr("x", 50)
    .attr("y", 250);

// Append rectangle to house text.

var textBox = svg.append("rect")
    .attr("width", 250)
    .attr("height", 400)
    .attr("x", 20)
    .attr("y", -200)
    .style("fill", "#2dbc94")
    .style("opacity", 0.8);

// Append text of third stanza.

    /*
    I like to think
    (it has to be!)
    of a cybernetic ecology
    where we are free of our labors
    and joined back to nature,
    returned to our mammal
    brothers and sisters,
    and all watched over
    by machines of loving grace.
    */

var text1 = svg.append("text")
    .attr("x", 35)
    .attr("y", -50)
    .attr("dy", "-2em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "15px")
    .attr("fill", "#e62e73")
    .text("I like to think");

var text2 = svg.append("text")
    .attr("x", 35)
    .attr("y", -50)
    .attr("dy", "-1em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "15px")
    .attr("fill", "#e62e73")
    .text("(it has to be!)");

var text3 = svg.append("text")
    .attr("x", 35)
    .attr("y", -50)
    .attr("dy", "0em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "15px")
    .attr("fill", "#e62e73")
    .text("of a cybernetic ecology");

var text4 = svg.append("text")
    .attr("x", 35)
    .attr("y", -50)
    .attr("dy", "1em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "15px")
    .attr("fill", "#e62e73")
    .text("where we are free of our labors");

var text5 = svg.append("text")
    .attr("x", 35)
    .attr("y", -50)
    .attr("dy", "2em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "15px")
    .attr("fill", "#e62e73")
    .text("and joined back to nature,");

var text6 = svg.append("text")
    .attr("x", 35)
    .attr("y", -50)
    .attr("dy", "3em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "15px")
    .attr("fill", "#e62e73")
    .text("returned to our mammal");

var text7 = svg.append("text")
    .attr("x", 35)
    .attr("y", -50)
    .attr("dy", "4em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "15px")
    .attr("fill", "#e62e73")
    .text("brothers and sisters,");

var text8 = svg.append("text")
    .attr("x", 35)
    .attr("y", -50)
    .attr("dy", "5em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "15px")
    .attr("fill", "#e62e73")
    .text("and all watched over");

var text8 = svg.append("text")
    .attr("x", 35)
    .attr("y", -50)
    .attr("dy", "6em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "15px")
    .attr("fill", "#e62e73")
    .text("by machines of loving grace.");


/*
SVG Path Mini-Language

T (t) = Shorthand/smooth quadratic Bézier curveto:
Draw a quadratic Bézier curve from the current point
to (x,y). The control point is assumed to be the
reflection of the control point on the previous command
relative to the current point.

L (l) = lineto: Draw a line from the current point to
the point (x,y).

M (m) = moveto: Move the pen to a new location. No line
is drawn. All path data must begin with a 'moveto' command.
*/

/* Equations for Lissajous curves adapted from:
http://goatlink.deviantart.com/art/lissajous-curves-338721857
*/

var range = d3.range(-70 * Math.PI, 50 * Math.PI, 0.02);

d3.timer(function(t) {
    var d = "M";

    for (var i = 0; i < range.length; i++) {
        var p = range[i];
        d += 0.25 * width * (Math.sin(4 * p + t / 2000) + Math.sin(2.01 * p + t / 1000));
        d += ",";
        d += 0.25 * height * (Math.sin(2 * p + t / 4000) + Math.sin(3.01 * p + t / 1000));
        if (i != range.length - 1) d += "L";
    }

    d.length--;
    lissajous.attr("d", d);

})

</script>


An homage to the 1967 poem by Richard Brautigan and Lissajous curves played out in JavaScript D3. <a href="machines_of_loving_grace1.html" style="color: rgb(167,55,75)" target="_blank"><font color="A7374B">Click to view version 1</font></a>.


