#include <ESP8266WebServer.h>

class CubeRequestHandler : public RequestHandler
{
    bool canHandle(HTTPMethod method, String uri)
    {
        return uri != null && uri.startsWith("/cube/face/");
    }

    bool handle(ESP8266WebServer &server, HTTPMethod requestMethod, String requestUri)
    {
        if (server.hasArg("plain") == false)
        { //Check if body received

            server.send(200, "text/plain", "Body not received");
            return;
        }

        String message = "Body received:\n";
        message += server.arg("plain");
        message += "\n";

        server.send(200, "text/plain", message);
        Serial.println(message);
    }
} myHandler;

void setup()
{
    server.addHandler(&myHandler);
}