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
            _client->print(preparedHTTPRequest);
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