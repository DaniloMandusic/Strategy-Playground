// Nikola Đokić 2018/0128

var file1_code = "def respond_to_change(change)\n\
    process(change)\n\
    if(should_buy)\n\
        buy()";

document.getElementById("editor").innerHTML = file1_code;