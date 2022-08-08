import kfzdaten 
while True:
    kennzeichen = input("Eingabe KFZ-Kennzeichen\n");
    for i in kfzdaten.kfz:
        if i["kennzeichen"].find(kennzeichen.upper())==0:
           print(i["kennzeichen"],i["gebiet"],sep=":")
    if input("Weitere Kennzeichen abfragen (Y/N)?\n").upper()=="N":
        print("Danke, dass Sie unseren Service genutzt haben!")
        break
