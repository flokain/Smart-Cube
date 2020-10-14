#include "EventHandling.h"

void Trigger::checkAndExecute()
{
    if (triggers())
    {
        handler_->execute(getState());
    }
}

bool SmartCubeTrigger::triggers()
{
    return cube_->detectChange();
}

std::map<String, String> SmartCubeTrigger::getState()
{
    return std::map<String, String>{{"face", String(cube_->getSideUp())}};
}

void RestHandler::setRestCall(Parameters index, String url, String SHA1Fingerprint, String preparedHTTPRequest, bool insecure)

// Fingerprint for demo URL, expires on June 2, 2019, needs to be updated well before this date
{
    std::unique_ptr<BearSSL::WiFiClientSecure> client(new BearSSL::WiFiClientSecure);

    // convert sha1 fingerprint to har array for client
    char charBuf[20];
    SHA1Fingerprint.toCharArray(charBuf, 20);
    client->setFingerprint(charBuf);
    if (insecure)
    {
        client->setInsecure();
    }

    // Use Http client for reading responses
    RestClient restClient;
    Serial.println("[RestHandler][setRestCall] prepare client");
    restClient.begin(*client, url);
    Serial.print("RestHandler][setRestCall] trying GET");
    Serial.println(restClient.GET());
    Serial.println("[RestHandler][setRestCall] prepare preparedHTTPRequest");
    restClient.preparedHTTPRequest = preparedHTTPRequest;
    //restClient.makeRequest();
    Serial.println("[RestHandler][setRestCall] add to restclients list");
    restClients[index] = &restClient;
    Serial.println("[RestHandler][setRestCall] preparation finished");
    Serial.println("[RestHandler] Executing Request");
}

void RestHandler::execute(std::map<String, String> index)
{
    Serial.println("[RestHandler] Executing Request");
    Serial.print("[RestHandler::execute] face is ");
    Serial.println(index["face"]);
    Serial.print("RestHandler::check if index");
    Serial.println(restClients.count(index));
    Serial.println(restClients[index]->makeRequest());
}