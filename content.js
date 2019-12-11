

var elements = document.getElementsByTagName('*');
for (var i = 0; i < elements.length; i++) {
    var element = elements[i];

    for (var j = 0; j < element.childNodes.length; j++) {
        var node = element.childNodes[j];

        if (node.nodeType === 3) {
            var text = node.nodeValue;

            var replacedText = text.replace(/daisy/gi, 'type of flower');
        //    replacedText.fontColor("red");


            if (replacedText !== text) {
                element.replaceChild(document.createTextNode(replacedText), node);
            }
        }
    }
}
//function printURL() {
//  console.log(window.location.href);
//}

//var allArticleText = "Joe Biden is running for president. Good for him.";
//console.log('parsed text:', allArticleText);


//var request = require('requests');
// give it the URL and the data
//request.post('http://localhost:8000', allArticleText);

// get brew
// brew install python
// pip install flask
