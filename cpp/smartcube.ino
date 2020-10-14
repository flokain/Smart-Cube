#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <ESP8266HTTPUpdateServer.h> // Step #1
#include <ESP8266mDNS.h>             // Step #1
#include <WiFiClient.h>              // Step #1
#include "Smartcube.h"
#include "EventHandling.h"
#include <AutoConnect.h>

// #define AC_DEBUG

ESP8266WebServer httpServer;    // Step #2
AutoConnect portal(httpServer); // Step #4

Smartcube *cube = new Smartcube(D1, D2, D3, 2000);
RestHandler *handler = new RestHandler();
SmartCubeTrigger trigger = SmartCubeTrigger(handler, cube);

String host = "https://www.google.com/";

// String http_request = "POST /api/v8/time_entries/start HTTP/1.1\r\n"
//                       "Host: www.toggl.com\r\n"
//                       "Content-Type: application/json\n"
//                       "Authorization: Basic NzQwYzIzZjhjYTEwMzQwMDY3Mjk5NTllMzNjYTg5ODY6YXBpX3Rva2Vu\r\n"
//                       "Accept: */*\r\n"
//                       "Cache-Control: no-cache\r\n"
//                       "Accept-Encoding: gzip, deflate\\rn"
//                       "Content-Length: 100\r\n"
//                       "Connection: close\r\n"
//                       "cache-control: no-cache\r\n"
//                       "\r\n"
//                       "{\"time_entry\":{\"description\":\"Meeting with possible clients\",\"pid\":151476843,\"created_with\":\"curl\"}}\r\n";

String http_request = "GET / HTTP/1.1\r\n"
                      "Host: www.toggl.com\r\n"
                      "Connection: close\r\n\r\n";

String fingerprint = "51 24 0A C6 62 CB 06 31 9C A7 7B 13 3A 9D E7 3F 6B A7 89 BF";

void setup()
{
  Serial.begin(115200);
  // test handler
  portal.begin();
  Parameters par = Parameters({{"face", "3"}});
  bool insecure = true;
  handler->setRestCall(par, host, fingerprint, http_request, insecure);
  // handler->execute(par);
}

void loop()
{
  portal.handleClient(); // Step #10.b
  trigger.checkAndExecute();
}