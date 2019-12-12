var hyperPartisan = false;
var parsedText = "Trump 2020 baby wohoo. I hate libtards";

function sendText()
{
    $.ajax
    (
        {
            type: "POST",
            url: "http://flask-env.z8fvk4ursf.us-east-2.elasticbeanstalk.com/json",
            dataType:"json",
            data: 
            {               
               parsedText,
            },
            success: function(backEndModelJSONOutput)
            {
               output = backEndModelJSONOutput.hyperPartisan;
               alert(output);
            },
            error: function() {
                alert('error sending parsed text');
            }     
        }
    );//End ajax 

}//end function

//SAMPLE POST request to url.com
/*
{
    "parsedText": "trump is the worst president ever"
}
*/

//SAMPLE RESPONSE
/*
{
"hyperPartisan": true
}
*/
//sendText = function(){};
sendText();

