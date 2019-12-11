console.log('background running');

chrome.browserAction.onClicked.addListener(function() {
    alert('button clicked');

    var currentURL = window.location.href;

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:8088/json", true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function() {
      if(xhr.readyState == 4 && xhr.status == 200) {
        alert('got response');
      }
    }
    // var jsonObject = { "parsedText": currentURL};
    var jsonObject = { "parsedText": "TEST"};
    var data = JSON.stringify(jsonObject);
    alert(currentURL);
    xhr.send(data);
    // chrome.tabs.executeScript(null, {file: 'post.js'})
  });



