# development notes
event and handler follow the observer design pattern
handler subscribe an event and get to the events Handler list.
Whenever a event happens it triggers all subscripted handlers.

## api updating
1. change the api files
2. check in all other changes
3. download flask server stub
4. extract to api/server/
5. check changes and commit

## testing
if I need classes from src folder in the functional testing i need to make
```bash
echo "PYTHON PATH = ./src" > .env
```

# Sources:
https://github.com/BradenM/micropy-cli
http://micropython.org/webrepl/#192.168.0.157:8266/
http://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#
https://github.com/belyalov/tinyweb
https://github.com/mcauser/awesome-micropython (list o fmicropython libraries)

https://www.codeply.com/p?starter=Bootstrap%204 (bootstrap online editor)

https://forum.micropython.org/viewtopic.php?t=4813 (maximize ram)

https://diyi0t.com/how-to-reduce-the-esp8266-power-consumption/

deep sleep experimenst:
https://randomnerdtutorials.com/esp8266-deep-sleep-with-arduino-ide/#:~:text=You%20can%20also%20wake%20up,LOW%20to%20wake%20it%20up.

# board
## esp01 (hat nur 1M speicher)
https://www.amazon.de/s?k=esp-01&i=electronics&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=
(5€, niedriger strom verbrauch)

https://german.alibaba.com/product-detail/oem-odm-esp8266-stable-wifi-to-uart-esp-01remote-wireless-module-62306647882.html?spm=a2700.md_de_DE.deiletai6.2.38f65b3a242w1J (1,19$)



## d1 mini (1,91 $)
https://german.alibaba.com/product-detail/esp8266-esp-12-esp-12f-ch340g-ch340-v2-usb-wemos-d1-mini-wifi-development-board-d1-mini-nodemcu-lua-iot-board-3-3v-with-pins-62500932624.html?spm=a2700.galleryofferlist.normal_offer.3.4e77628c8m9oql&s=p


## esp32 d1 ($3,18)
https://de.aliexpress.com/item/4000232057013.html?spm=a2g0o.productlist.0.0.4f3a745aA50heR&algo_pvid=1c627931-56aa-4e37-a8c6-0bb48323e10b&algo_expid=1c627931-56aa-4e37-a8c6-0bb48323e10b-21&btsid=0bb0623e16036088779256164e6a32&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_

# battery shield (0,785$)
https://de.aliexpress.com/item/32892162107.html?spm=a2g0o.productlist.0.0.206b6155clXwPT&algo_pvid=29c46515-054f-4ff4-8b0b-b6f023deb80d&algo_expid=29c46515-054f-4ff4-8b0b-b6f023deb80d-9&btsid=0bb0624616035763253444722e2a39&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_

mengenrabat:
https://de.aliexpress.com/item/32841796602.html?spm=a2g0o.productlist.0.0.58241b57poFv7T&algo_pvid=019ea799-349e-433b-9e85-04be5e9305d6&algo_expid=019ea799-349e-433b-9e85-04be5e9305d6-15&btsid=0b0a556216035803283496946ecd8f&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_ (0,56$)


## selbstgebastelt
1000uF capacitor (0,093 \$)  https://de.aliexpress.com/item/32948189325.html?spm=a2g0o.productlist.0.0.5ece70cdTogVNq&algo_pvid=70ae1869-17d9-4b79-9741-83ec89f9cb81&algo_expid=70ae1869-17d9-4b79-9741-83ec89f9cb81-1&btsid=0bb0624016035756034341727e0add&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603
100nF capcitor (0,0056$)(https://de.aliexpress.com/item/32971478818.html?spm=a2g0o.productlist.0.0.70d44aa1LX5K3U&algo_pvid=32b73561-80c0-4d60-a0aa-bac72994e341&algo_expid=32b73561-80c0-4d60-a0aa-bac72994e341-8&btsid=0bb0624016035754533918546e0add&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_)
LDO regulator (0,068) MCP1700-3302E or HT7333-A


micro usb ladeadapter.
https://de.aliexpress.com/item/32608706630.html?spm=a2g0o.detail.0.0.6c6f3458KiRa4H&gps-id=pcDetailBottomMoreThisSeller&scm=1007.13339.169870.0&scm_id=1007.13339.169870.0&scm-url=1007.13339.169870.0&pvid=1ffcfafe-22e5-4653-ac39-d0afe321973b&_t=gps-id:pcDetailBottomMoreThisSeller,scm-url:1007.13339.169870.0,pvid:1ffcfafe-22e5-4653-ac39-d0afe321973b,tpp_buckets:668%230%23131923%2330_668%23808%233772%23660_668%23888%233325%2320_668%234328%2319934%23630_668%232846%238107%236_668%232717%237558%23113_668%231000022185%231000066059%230_668%233468%2315616%23797
 (0,12 $)


JST connector cables
https://de.aliexpress.com/item/33027366342.html?spm=a2g0o.productlist.0.0.41d47a17CSTvmy&algo_pvid=2253a7ed-d687-4693-8f2a-71938e5b7fa8&algo_expid=2253a7ed-d687-4693-8f2a-71938e5b7fa8-2&btsid=0bb0623416035778476055362e8252&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_(0,58)


Batterie (5€)
https://www.amazon.de/MakerHawk-Schutz-Brett-Isolierkautschuk-Band-Entwicklungs-Brett-WIFI-Ausr%C3%BCstung/dp/B07CYMYMS9/ref=pd_sbs_23_1/261-5993676-0577205?_encoding=UTF8&pd_rd_i=B07CYMYMS9&pd_rd_r=11717156-ae33-467f-9900-fdd4d67c12e0&pd_rd_w=MWZ8W&pd_rd_wg=v1qVh&pf_rd_p=a03ac387-6e4d-4f6b-96b6-1853da0bb37b&pf_rd_r=C3VNBXD6SZ98XMA17K08&psc=1&refRID=C3VNBXD6SZ98XMA17K08

## battery
https://de.aliexpress.com/item/4001130974185.html?spm=a2g0o.productlist.0.0.22c135bfsuwya7&algo_pvid=67045af6-f6d9-4e5c-9264-5caec1689f99&algo_expid=67045af6-f6d9-4e5c-9264-5caec1689f99-26&btsid=0b0a556716035704295852165e55cc&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_ (2,4$ kein versand gebühren)

# reset board from comandline
```
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 ~/Arduino/smartcube/micropython/bin/esp8266-20200911-v1.13.bin 
```

pymakr.json needs to accept gz file on upload

build and deploy firmware with this:
```bash
cd ~/Arduino/smartcube/misc/micropython/ports/esp8266/ &&  docker run --rm -v $HOME:$HOME -u 1000 -w $PWD larsks/esp-open-sdk make clean  &&  docker run --rm -v $HOME:$HOME -u 1000 -w $PWD larsks/esp-open-sdk make && esptool.py --port /dev/ttyUSB0 erase_flash && esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 ~/Arduino/smartcube/misc/micropython/ports/esp8266/build-GENERIC/firmware-combined.bin
```


# Power consumption

| action             | notes                           | mA    |
| ------------------ | ------------------------------- | ----- |
| deepsleep          |                                 | 0,244 |
| init process       | 15-18 s                         | 71-75 |
| idle (modem-sleep) | spikes every 3 sec for 1s 7o 75 | 22-25 |
| idle (light-sleep) | spikes every 3 sec for 1s 7o 75 | 8-10  |
| webcall            | 7-20s                           | 74    |
| servercall         | 2 sec                           | 74    |

laut diesen daten: deepsleep zahlt sich aus ab einem intervall von 67 sekunden = 75*18/20. sicher ist es ab 168.5 (2.8 min)

- [ ] test bei annähernd konstanten 73mA wurden 1000mAh in 13:40 h verbraucht. ich muss noch testen welches programm da tatsächlich drauf lief.

### version fe685d1fc

- [ ] eine stunde in idle mode mit version fe685d1f auf seite 3 verbrauchte 20mah
- [ ] mit 
- [ ] Auf seite 4,5,6 habe ich gar keinen strom gemessen, oder so zu schwach fuer da messgerät. wenn ich in einem dieses zustande gestartet habe. dabei waren alle pins auf pin IN ohne resistor im idle mode
  - [ ] auf seite 1 sind es 9 mA ( alle kontakte geschlossen)
  - [ ] auf seite 3 sind es 7 mA ( d2/gpio4 offen d1 d3 geschlossen)
  - [ ] auf seite 6 sind es 0 mA  alle offen 0 mA
  - [ ] auf seite 5 sind es 0 mA  d1/gpio5 geshlossen 0mA
  - [ ] auf seite 4 sind es 0 mA  ( d2/gpio4 geschlossen)
  - [ ] auf seite 2 sind es 7 mA ( d1 ist offen  d2 d3 geschlossen)

wenn d3 geschlossen ist fließt am meisten strom (ca 7mAh)

### version 488d11c9d045

pins sind im idle mode auf out und value 0 gestellt.

stromverbrauch wurde hier mi 3mAh gemessen

langzeit test idle:  9mA  (3,25h 31mAh) (geschätzte laufzeit 83h )

todo static ip for faster connection see: https://www.instructables.com/ESP8266-Pro-Tips/

