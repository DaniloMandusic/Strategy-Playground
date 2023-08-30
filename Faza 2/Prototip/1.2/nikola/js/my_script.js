// Nikola Đokić 2018/0128
// Converts your input data into an object:
var convert = function(input) {
    var output = {};
    // iterate through each path in the input array:
    input.forEach(function(path) {
      var folders = path.split("\\"); // convert this path into an array of folder names
      // "parent" serves as a marker in the output object pointing to the current folder
      var parent = output; // the topmost folder will be a child of the output root
      folders.forEach(function(f) {
        parent[f] = parent[f] || {}; // add a folder object if there isn't one already
        parent = parent[f]; // the next part of the path will be a child of this part
      });
    });
    return (output);
  }
  
  // Draws nested lists for the folder structure
  var drawFolders = function(input) {
    var output = "<ul class='file'>";
    Object.keys(input).forEach(function(k) { 
      if (Object.keys(input[k]).length) {
        output += "<li class='file'>" + k; // draw this folder
        output += drawFolders(input[k]); // recurse for child folders
      }
      else {
        output += "<li class='file-end'>" + k; // draw this file
      }
      output += "</li>";
    });
    output += "</ul>";
    return output;
  }
  
  var input = [
    "Koren\\folder1\\fajl1.py",
    "Koren\\folder1\\fajl2.py",
    "Koren\\fajl3.py"
  ];
  document.getElementById("files").innerHTML = drawFolders(convert(input));