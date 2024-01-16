# Verbinden Anfrage und gefundte Kontext in Datenbank
import Kontexterstellung.Kontext_OR_AND as kt

def anfrage_kontext():
    anfrage = input('Bitte schreiben Sie die Anfrage: ')
    kontext = kt.db_info(anfrage) #str
    anfrage_kontext = anfrage + kontext #str
    print('erstellte Kontext: ')
    print(anfrage_kontext)
    return anfrage_kontext

#anfrage_kontext()
