var url = window.location.href;


chrome.browserAction.onClicked.addListener(function() {
    alert('button clicked');

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:8088/json", true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function() {
      if(xhr.readyState == 4 && xhr.status == 200) {
        alert('got response');
      }
    }
    xhr.send(url);
    alert(url);
    // chrome.tabs.executeScript(null, {file: 'post.js'})
  });
