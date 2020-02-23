#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <ESP8266HTTPUpdateServer.h> // Step #1
#include <ESP8266mDNS.h>             // Step #1
#include <WiFiClient.h>              // Step #1
#include "Smartcube.h"
#include "EventHandling.h"
#include <AutoConnect.h>

// #define AC_DEBUG

static const char HELLO_PAGE[] PROGMEM = R"(
{ "title": "Hello world", "uri": "/", "menu": true, "element": [
    { "name": "caption", "type": "ACText", "value": "<h2>Hello, world</h2>",  "style": "text-align:center;color:#2f4f4f;padding:10px;" },
    { "name": "content", "type": "ACText", "value": "In this page, place the custom web page handled by the sketch application." } ]
}
)";

// swagger ui example
const char *swaggerJSON = "{\"swagger\":\"2.0\",\"info\":{\"description\":\"This is a sample server Petstore server.\",\"version\":\"1.0.0\",\"title\":\"IoT application\"},\"host\":\"192.168.0.120\",\"tags\":[{\"name\":\"Temperature\",\"description\":\"Getting temperature measurements\"}],\"paths\":{\"/temperature\":{\"get\":{\"tags\":[\"Temperature\"],\"summary\":\"Endpoint for getting temperature measurements\",\"description\":\"\",\"operationId\":\"getTemperature\",\"responses\":{\"200\":{\"description\":\"A list of temperature measurements\",\"schema\":{\"$ref\":\"#/definitions/temperatureMeasurement\"}}}}}},\"definitions\":{\"temperatureMeasurement\":{\"type\":\"object\",\"properties\":{\"value\":{\"type\":\"string\"},\"timestamp\":{\"type\":\"string\"}}}}}";
const char *swaggerUI = "!DOCTYPE html><html><head> <meta charset=\"UTF-8\"> <meta http-equiv=\"x-ua-compatible\" content=\"IE=edge\"> <title>Swagger UI</title> <link href='https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css' media='screen' rel='stylesheet' type='text/css'/> <link href='https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/2.2.10/css/screen.css' media='screen' rel='stylesheet' type='text/css'/> <script>if (typeof Object.assign !='function'){(function (){Object.assign=function (target){'use strict'; if (target===undefined || target===null){throw new TypeError('Cannot convert undefined or null to object');}var output=Object(target); for (var index=1; index < arguments.length; index++){var source=arguments[index]; if (source !==undefined && source !==null){for (var nextKey in source){if (Object.prototype.hasOwnProperty.call(source, nextKey)){output[nextKey]=source[nextKey];}}}}return output;};})();}</script> <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.0/jquery-1.8.0.min.js' type='text/javascript'></script> <script>(function(b){b.fn.slideto=function(a){a=b.extend({slide_duration:\"slow\",highlight_duration:3E3,highlight:true,highlight_color:\"#FFFF99\"},a);return this.each(function(){obj=b(this);b(\"body\").animate({scrollTop:obj.offset().top},a.slide_duration,function(){a.highlight&&b.ui.version&&obj.effect(\"highlight\",{color:a.highlight_color},a.highlight_duration)})})}})(jQuery); </script> <script>jQuery.fn.wiggle=function(o){var d={speed:50,wiggles:3,travel:5,callback:null};var o=jQuery.extend(d,o);return this.each(function(){var cache=this;var wrap=jQuery(this).wrap('<div class=\"wiggle-wrap\"></div>').css(\"position\",\"relative\");var calls=0;for(i=1;i<=o.wiggles;i++){jQuery(this).animate({left:\"-=\"+o.travel},o.speed).animate({left:\"+=\"+o.travel*2},o.speed*2).animate({left:\"-=\"+o.travel},o.speed,function(){calls++;if(jQuery(cache).parent().hasClass('wiggle-wrap')){jQuery(cache).parent().replaceWith(cache);}if(calls==o.wiggles&&jQuery.isFunction(o.callback)){o.callback();}});}});}; </script> <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery.ba-bbq/1.2.1/jquery.ba-bbq.min.js' type='text/javascript'></script> <script src='https://cdnjs.cloudflare.com/ajax/libs/handlebars.js/4.0.5/handlebars.min.js' type='text/javascript'></script> <script src='https://cdnjs.cloudflare.com/ajax/libs/lodash-compat/3.10.1/lodash.min.js' type='text/javascript'></script> <script src='https://cdnjs.cloudflare.com/ajax/libs/backbone.js/1.1.2/backbone-min.js' type='text/javascript'></script> <script>Backbone.View=(function(View){return View.extend({constructor: function(options){this.options=options ||{}; View.apply(this, arguments);}});})(Backbone.View); </script> <script src='https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/2.2.10/swagger-ui.min.js' type='text/javascript'></script> <script src='https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.10.0/highlight.min.js' type='text/javascript'></script> <script src='https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.10.0/languages/json.min.js' type='text/javascript'></script> <script src='https://cdnjs.cloudflare.com/ajax/libs/json-editor/0.7.28/jsoneditor.min.js' type='text/javascript'></script> <script src='https://cdnjs.cloudflare.com/ajax/libs/marked/0.3.6/marked.min.js' type='text/javascript'></script> <script type=\"text/javascript\">$(function (){url=\"http://192.168.0.120/swagger.json\"; hljs.configure({highlightSizeThreshold: 5000}); window.swaggerUi=new SwaggerUi({url: url, dom_id: \"swagger-ui-container\", supportedSubmitMethods: ['get', 'post', 'put', 'delete', 'patch'],validatorUrl: null, onComplete: function(swaggerApi, swaggerUi){}, onFailure: function(data){log(\"Unable to Load SwaggerUI\");}, docExpansion: \"none\", jsonEditor: false, defaultModelRendering: 'schema', showRequestHeaders: false, showOperationIds: false}); window.swaggerUi.load(); function log(){if ('console' in window){console.log.apply(console, arguments);}}}); </script></head><body class=\"swagger-section\"><div id='header'> <div class=\"swagger-ui-wrap\"> <a id=\"logo\" href=\"http://swagger.io\"><img class=\"logo__img\" alt=\"swagger\" height=\"30\" width=\"30\" src=\"https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/2.2.10/images/logo_small.png\"/><span class=\"logo__title\">swagger</span></a> <form id='api_selector'> </form> </div></div><div id=\"message-bar\" class=\"swagger-ui-wrap\" data-sw-translate>&nbsp;</div><div id=\"swagger-ui-container\" class=\"swagger-ui-wrap\"></div></body></html>";
const char *answer = "[{\"value\":\"10.5\",\"timestamp\":\"22/10/2017 10:10\"},{\"value\":\"11.0\",\"timestamp\":\"22/10/2017 10:20\"}]";

ESP8266WebServer httpServer;                // Step #2
ESP8266HTTPUpdateServer httpUpdate;         // Step #3
AutoConnect portal(httpServer);             // Step #4
AutoConnectAux update("/update", "UPDATE"); // Step #5, #6, #7
AutoConnectAux hello;                       // Step #8

Smartcube *cube = new Smartcube(D1, D2, D3, 2000);
RestHandler *handler = new RestHandler();
SmartCubeTrigger trigger = SmartCubeTrigger(handler, cube);

String host = "https://www.toggl.com";
// String http_reuqest =
String http_request = "POST /api/v8/time_entries/start HTTP/1.1\n"
                      "Host: www.toggl.com\n"
                      "Content-Type: application/json\n"
                      "Authorization: Basic NzQwYzIzZjhjYTEwMzQwMDY3Mjk5NTllMzNjYTg5ODY6YXBpX3Rva2Vu\n"
                      "Accept: */*\n"
                      "Cache-Control: no-cache\n"
                      "Postman-Token: 04d96165-2bee-4730-b4d1-55680fe65300,c4df8b60-e0f9-4e20-ae41-08efc2705d15\n"
                      "Host: www.toggl.com\n"
                      "Accept-Encoding: gzip, deflate\n"
                      "Content-Length: 100\n"
                      "Cookie: GCLB=CO_a5oLDpqmj-QE\n"
                      "Connection: keep-alive\n"
                      "cache-control: no-cache\n"
                      "\n"
                      "{\"time_entry\":{\"description\":\"Meeting with possible clients\",\"pid\":151476843,\"created_with\":\"curl\"}}\n";

String fingerprint = "51 24 0A C6 62 CB 06 31 9C A7 7B 13 3A 9D E7 3F 6B A7 89 BF";

void setup()
{
  Serial.begin(115200);
  // test handler
  Parameters par = Parameters({{"face", "1"}});

  Serial.println("[setup] handler->setRestCall");
  bool insecure = true;
  //handler->setRestCall(par, host, fingerprint, http_request, insecure);
  Serial.println("[setup] handler->execute(par)");
  //handler->execute(par);

  // setup autconnect server
  httpUpdate.setup(&httpServer, "USERNAME", "PASSWORD"); // Step #9.a
  hello.load(HELLO_PAGE);                                // Step #9.b
  portal.join({hello, update});                          // Step #9.c

  // swagger ui example
  httpServer.on("/temperature", handleTemperature);
  httpServer.on("/swagger.json", handleSwaggerJson);
  httpServer.on("/swaggerUI", handleSwaggerUI);
  httpServer.on("/cube/face", HTTP_POST, handleCubeFacePostRequest);
  if (portal.begin())
  {                                       // Step #9.d
    if (MDNS.begin("esp-webupdate"))      // Step #9.e
      MDNS.addService("http", "tcp", 80); // Step #9.e
  }
}

void loop()
{
  MDNS.update();         // Step #10.a
  portal.handleClient(); // Step #10.b
  trigger.checkAndExecute();
}

void handleTemperature()
{
  httpServer.send(200, "application/json", answer);
}

void handleSwaggerJson()
{

  httpServer.send(200, "application/json", swaggerJSON);
}

void handleSwaggerUI()
{

  httpServer.send(200, "text/html", swaggerUI);
}

void handleCubeFacePostRequest()
{
  if (httpServer.hasArg("plain") == false)
  { //Check if body received

    httpServer.send(200, "text/plain", "Body not received");
    return;
  }

  String message = "Body received:\n";
  message += httpServer.arg("plain");
  message += "\n";

  httpServer.send(200, "text/plain", message);
  Serial.println(message);
}