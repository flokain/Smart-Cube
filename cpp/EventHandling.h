#ifndef EVENTHANDLING_H_
#define EVENTHANDLING_H_

#include "Smartcube.h"
#include <WiFiClientSecureBearSSL.h>
#include <ESP8266HTTPClient.h>
#include <map>
#include <vector>

typedef std::map<String, String> Parameters;
class Handler;
class RestHandler;

class Trigger
{
protected:
    Handler *handler_;
    virtual Parameters getState() = 0;
    virtual bool triggers() = 0;

public:
    Trigger(Handler *handler) : handler_(handler){};
    virtual ~Trigger(){};
    void checkAndExecute();
};

class SmartCubeTrigger : public Trigger
{
protected:
    Smartcube *cube_;
    std::map<String, String> getState();
    bool triggers();

public:
    SmartCubeTrigger(Handler *handler)
        : Trigger(handler), cube_(){};
    SmartCubeTrigger(Handler *handler, Smartcube *cube)
        : Trigger(handler), cube_(cube){};
};

class Handler
{
public:
    virtual ~Handler(){};
    virtual void execute(std::map<String, String> input) = 0;
};

class RestHandler : public Handler
{
protected:
    /*  Need to expose write and handleHeaderResponse function of HTTPClient
        so the whole http (curl) commant can be parsed.
    */
    class RestClient : public HTTPClient
    {

    public:
        String preparedHTTPRequest;
        int makeRequest()
        {
            Serial.println("Sending request");
            Serial.println(this->_host);
            Serial.println(this->_port);
            if (!_client->connect("toggl.com", 443))
            {
                Serial.println("connection failed");
                return -1;
            }
            _client->print(preparedHTTPRequest);
            Serial.println("request sent");
            while (_client->connected())
            {
                String line = _client->readStringUntil('\n');
                if (line == "\r")
                {
                    Serial.println("headers received");
                    break;
                }
            }
            String line = _client->readStringUntil('\n');
            if (line.startsWith("{\"state\":\"success\""))
            {
                Serial.println("esp8266/Arduino CI successfull!");
            }
            else
            {
                Serial.println("esp8266/Arduino CI has failed");
            }
            Serial.println("reply was:");
            Serial.println("==========");
            Serial.println(line);
            Serial.println("==========");
            Serial.println("closing connection");

            return returnError(handleHeaderResponse());
        };
    };
    std::map<Parameters, RestClient *> restClients;

public:
    RestHandler()
        : restClients(){};

    void execute(Parameters index);
    void setRestCall(Parameters index, String url, String SHA1Fingerprint, String preparedHTTPRequest, bool insecure);
};

#endif