import android
import time
import geo_distance

droid = android.Android()

from math import sqrt

#!adb forward tcp:9999 tcp:49762
#droid = android.Android()

droid.dialogCreateAlert("Posicion Principal","Estas en tu trabajo?")
droid.dialogSetPositiveButtonText("Yes")
droid.dialogSetNegativeButtonText("No")
droid.dialogShow()
response = droid.dialogGetResponse().result
droid.dialogDismiss()

if response.has_key("which"):
    result=response["which"]
    if result=="positive":
        droid.startLocating()
        time.sleep(16)
        resultado = droid.readLocation().result
        #print(resultado)
        droid.ttsSpeak("posicion guardada")
        longitud = resultado['network']['longitude']
        latitud = resultado['network']['latitude']
        droid.stopLocating()
        print (longitud, latitud)
    elif result=="negative":
        print "ponte a trabajar"

time.sleep(120)

droid.startLocating()
time.sleep(16)
resultado2 = droid.readLocation().result
droid.ttsSpeak("segunda posicion guardada")
longitud2 = resultado2['network']['longitude']
latitud2 = resultado2['network']['latitude']
droid.stopLocating()

distancia = (geo_distance.distance(latitud,longitud,latitud2,longitud2)*1000)

if distancia < 10:
    droid.ttsSpeak("no te has movido")
else:
    droid.ttsSpeak("no te alejes de tu trabajo")