console.log('background running');

var currentURL;

chrome.browserAction.onClicked.addListener(function(activeTab){
  currentURL = activeTab.url;
});

chrome.browserAction.onClicked.addListener(function() {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://flask-env.z8fvk4ursf.us-east-2.elasticbeanstalk.com/json", true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = (function() {
      if(xhr.readyState == 4 && xhr.status == 200) {
        alert(xhr.responseText);
      }
    })
    var jsonObject = {"parsedText": currentURL };
    var data = JSON.stringify(jsonObject);
    xhr.send(data);
    // chrome.tabs.executeScript(null, {file: 'post.js'})
  });


  console.log('background running');

