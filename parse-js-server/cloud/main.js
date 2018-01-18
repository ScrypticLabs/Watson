// Use Parse.Cloud.define to define as many cloud functions as you want.
// For example:
// Parse.Cloud.define("hello", function(request, response) {
//   response.success("Hello world!");
// });

var twilio = require("twilio");
twilio.initialize("AC0bec7092250cd3794b159a91b9dd1074","1569df3a5048cdcdbb2779b8b45924f1");

Parse.Cloud.define("inviteWithTwilio", function(request, response) {
  twilio.sendSMS({
    From: request.params.WatsonNumber,
    To: request.params.number,
    Body: request.params.message
  }, {
    success: function(httpResponse) {
      console.log(httpResponse);
      response.success("SMS sent!",request.params.number);
    },
    error: function(httpResponse) {
      console.error(httpResponse);
      response.error("Uh oh, something went wrong");
    }
  });
});


Parse.Cloud.define("receiveSMS", function(request, response) {
  console.log("New text: " + request.params.Body);
  var message = "";
  var text = request.params.Body;
  text = text.split(' ').join('+');
  var city = request.params.FromCity;
  var state = request.params.FromState;
  var country = request.params.FromCountry;
  var zipCode = request.params.FromZip;

  var url = 'https://radiant-forest-3193.herokuapp.com/?action=singleService&text='+text+"&city="+city+"&state="+state+"&country="+country+"&zipCode="+zipCode;
  console.log(url);
  var promise = Parse.Cloud.httpRequest({
      url: url,
  });
  promise.then(function(httpResponse) {
    console.log(httpResponse.headers);
    console.log(httpResponse.text);

    message = httpResponse.text;

    Parse.Cloud.run('inviteWithTwilio', { "plan": "paid", "WatsonNumber": "5067990324", "number": request.params.From, "message": message}, {
      success: function(result) {
      response.success('Succeeded');
      },
      error: function(error) {
      response.error('Failed');
      }
    });

    response.success(httpResponse.text);
  }, function(httpResponse) {
    response.error("Error: "+httpResponse.text);
    console.error(httpResponse);
  });
});

Parse.Cloud.define("receiveSMSwithParty", function(request, response) {
  console.log("New text: " + request.params.Body);
  var message = "";
  var text = request.params.Body;
  text = text.split(' ').join('+');
  var from = request.params.From
  var city = request.params.FromCity;
  var state = request.params.FromState;
  var country = request.params.FromCountry;
  var zipCode = request.params.FromZip;

  var replyBackto = "5198175265";

  if (from == "5198175265") {   // Sender's cell number
    replyBackto = "2262463034"; // Recipients's cell number
  } 


  var url = 'https://radiant-forest-3193.herokuapp.com/?action=multiService&text='+text+"&sender="+from+"&city="+city+"&state="+state+"&country="+country+"&zipCode="+zipCode;
  console.log(url);
  var promise = Parse.Cloud.httpRequest({
      url: url,
  });
  promise.then(function(httpResponse) {
    console.log(httpResponse.headers);
    console.log(httpResponse.text);

    message = httpResponse.text;

    Parse.Cloud.run('inviteWithTwilio', { "plan": "paid", "WatsonNumber": "2892747953", "number": replyBackto, "message": message}, {
      success: function(result) {
      response.success('Succeeded');
      },
      error: function(error) {
      response.error('Failed');
      }
    });
    replyBackto="";
    response.success(httpResponse.text);
  }, function(httpResponse) {
    response.error("Error: "+httpResponse.text);
    console.error(httpResponse);
  });
});