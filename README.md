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
<p align="center">
<div class="svg-container" align="center">

<meta charset="utf-8">
<body>
<script src="https://d3js.org/d3.v4.min.js"></script>
<script src="https://d3js.org/d3-timer.v1.min.js"></script>

<script>

// Set dimensions of SVG containers.

var width = 250,
    height = 200;

// Build SVG grid for visualization.

var svg1 = d3.select("body").append("svg")
    .attr("width", width / 5)
    .attr("height", height / 5)
    .style("background", "#ffffff")
    .append("g")
    .attr("transform", "translate(" + [width / 2, height / 2] + ")");

var svg2 = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)
    .style("background", "#000000")
    .append("g")
    .attr("transform", "translate(" + [width / 2, height / 2] + ")");

var svg3 = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)
    .style("background", "#b3e8c2")
    .append("g")
    .attr("transform", "translate(" + [width / 2, height / 2] + ")");

var svg4 = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)
    .style("background", "#baa600")
    .append("g")
    .attr("transform", "translate(" + [width / 2, height / 2] + ")");

var svg5 = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)
    .style("background", "#ffb852")
    .append("g")
    .attr("transform", "translate(" + [width / 2, height / 2] + ")");

// Append paths for Lissajous curves.

var lissajousTitle = svg2.append("path")
    .attr("fill", "none")
    .attr("stroke", "#c0b490")
    .attr("stroke-opacity", 1)
    .attr("stroke-width", 0.5)
    .attr("x", 50)
    .attr("y", 250);

var lissajous1 = svg3.append("path")
    .attr("fill", "none")
    .attr("stroke", "#ffff00")
    .attr("stroke-opacity", 1)
    .attr("stroke-width", 0.5)
    .attr("x", 50)
    .attr("y", 250);

var lissajous2 = svg4.append("path")
    .attr("fill", "none")
    .attr("stroke", "#e62e73")
    .attr("stroke-opacity", 1)
    .attr("stroke-width", 0.5)
    .attr("x", 50)
    .attr("y", 250);

var lissajous3 = svg5.append("path")
    .attr("fill", "none")
    .attr("stroke", "#ebd999")
    .attr("stroke-opacity", 1)
    .attr("stroke-width", 0.5)
    .attr("x", 50)
    .attr("y", 250);

// Append rectangles to house text.

var textBoxTitle = svg2.append("rect")
    .attr("width", 150)
    .attr("height", 100)
    .attr("x", -10)
    .attr("y", -50)
    .style("fill", "#06004f")
    .style("opacity", 0.8);

var textBox1 = svg3.append("rect")
    .attr("width", 150)
    .attr("height", 100)
    .attr("x", -10)
    .attr("y", -50)
    .style("fill", "#ffcfc4")
    .style("opacity", 0.8);

var textBox2 = svg4.append("rect")
    .attr("width", 150)
    .attr("height", 100)
    .attr("x", -10)
    .attr("y", -50)
    .style("fill", "#2dbc94")
    .style("opacity", 0.9);

var textBox3 = svg5.append("rect")
    .attr("width", 150)
    .attr("height", 100)
    .attr("x", -10)
    .attr("y", -50)
    .style("fill", "#a93400")
    .style("opacity", 0.6);


// Append text of title.

var text1_title = svg2.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "-1em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#c0b490")
    .text("ALL WATCHED");

var text2_title = svg2.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "0em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#c0b490")
    .text("OVER BY");

var text3_title = svg2.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "1em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#c0b490")
    .text("MACHINES OF");

var text4_title = svg2.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "2em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#c0b490")
    .text("LOVING GRACE");

var text5_title = svg2.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "4em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#c0b490")
    .text("");

var text6_title = svg2.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "5em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#c0b490")
    .text("Richard Brautigan | 1967");

// Append text of first stanza.

    /*
    I like to think (and
    the sooner the better!)
    of a cybernetic meadow
    where mammals and computers
    live together in mutually
    programming harmony
    like pure water
    touching clear sky.
    */

var text1_3 = svg3.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "-1em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#ffff00")
    .text("I like to think (and");

var text2_3 = svg3.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "0em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#ffff00")
    .text("the sooner the better!)");

var text3_3 = svg3.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "1em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#ffff00")
    .text("of a cybernetic meadow");

var text4_3 = svg3.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "2em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#ffff00")
    .text("where mammals and computers");

var text5_3 = svg3.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "3em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#ffff00")
    .text("live together in mutually");

var text6_3 = svg3.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "4em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#ffff00")
    .text("programming harmony");

var text7_3 = svg3.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "5em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#ffff00")
    .text("like pure water");

var text8_3 = svg3.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "6em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#ffff00")
    .text("touching clear sky.");

// Append text of second stanza.

        /*
        I like to think
        (right now, please!)
        of a cybernetic forest
        filled with pines and electronics
        where deer stroll peacefully
        past computers
        as if they were flowers
        with spinning blossoms.
        */

var text1_4 = svg4.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "-1em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#e62e73")
    .text("I like to think");

var text2_4 = svg4.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "0em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#e62e73")
    .text("(right now, please!)");

var text3_4 = svg4.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "1em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#e62e73")
    .text("of a cybernetic forest");

var text4_4 = svg4.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "2em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#e62e73")
    .text("filled with pines and electronics");

var text5_4 = svg4.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "3em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#e62e73")
    .text("where deer stroll peacefully");

var text6_4 = svg4.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "4em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#e62e73")
    .text("past computers");

var text7_4 = svg4.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "5em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#e62e73")
    .text("as if they were flowers");

var text8_4 = svg4.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "6em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#e62e73")
    .text("with spinning blossoms.");

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

var text1_5 = svg5.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "-1em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#ebd999")
    .text("I like to think");

var text2_5 = svg5.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "0em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#ebd999")
    .text("(it has to be!)");

var text3_5 = svg5.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "1em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#ebd999")
    .text("of a cybernetic ecology");

var text4_5 = svg5.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "2em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#ebd999")
    .text("where we are free of our labors");

var text5_5 = svg5.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "3em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#ebd999")
    .text("and joined back to nature,");

var text6_5 = svg5.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "4em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#ebd999")
    .text("returned to our mammal");

var text7_5 = svg5.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "5em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#ebd999")
    .text("brothers and sisters,");

var text8_5 = svg5.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "6em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#ebd999")
    .text("and all watched over");

var text9_5 = svg5.append("text")
    .attr("x", 0)
    .attr("y", -20)
    .attr("dy", "7em")
    .attr("font-family", "sans-serif")
    .attr("font-size", "8px")
    .attr("fill", "#ebd999")
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

var range2 = d3.range(-60 * Math.PI, 40 * Math.PI, 0.02);

d3.timer(function(t) {

    var dTitle = "M";

    for (var i = 0; i < range.length; i++) {
        var p = range2[i];
        dTitle += 0.22 * width * (Math.sin(3 * p + t / 2000) + Math.sin(2.01 * p + t / 3000));
        dTitle += ",";
        dTitle += 0.22 * height * (Math.sin(2.5 * p + t / 4000) + Math.sin(3.01 * p + t / 3000));
        if (i != range.length - 1) dTitle += "L";
    }

    dTitle.length--;
    lissajousTitle.attr("d", dTitle);

    var d1 = "M";

    for (var i = 0; i < range.length; i++) {
        var p = range[i];
        d1 += 0.22 * width * (Math.sin(3 * p + t / 2000) + Math.sin(2.01 * p + t / 3000));
        d1 += ",";
        d1 += 0.22 * height * (Math.sin(2 * p + t / 4000) + Math.sin(3.01 * p + t / 3000));
        if (i != range.length - 1) d1 += "L";
    }

    d1.length--;
    lissajous1.attr("d", d1);

    var d2 = "M";

    for (var i = 0; i < range.length; i++) {
        var p = range2[i];
        d2 += 0.22 * width * (Math.sin(4 * p + t / 2000) + Math.sin(2.01 * p + t / 3000));
        d2 += ",";
        d2 += 0.22 * height * (Math.sin(2 * p + t / 4000) + Math.sin(3.01 * p + t / 3000));
        if (i != range.length - 1) d2 += "L";
    }

    d2.length--;
    lissajous2.attr("d", d2);

    var d3 = "M";

    for (var i = 0; i < range.length; i++) {
        var p = range[i];
        d3 += 0.22 * width * (Math.sin(4 * p + t / 2000) + Math.sin(2.01 * p + t / 3000));
        d3 += ",";
        d3 += 0.22 * height * (Math.sin(4 * p + t / 4000) + Math.sin(3.01 * p + t / 3000));
        if (i != range.length - 1) d3 += "L";
    }

    d3.length--;
    lissajous3.attr("d", d3);

})

</script>
</p>
</div>
