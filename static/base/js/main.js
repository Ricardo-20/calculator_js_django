function insertTextInInputValue(buttonValueIs){
    if (buttonValueIs == "AC")
    {
      $('#ques').text('Ans : 0');
      $('#result').val(0);
    }
    else {
      var inputElementIs = document.getElementById("result");
      inputElementIs.value =  inputElementIs.value + buttonValueIs;
      $('#result').val(inputElementIs.value);
    }
}
