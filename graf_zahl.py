
##############################################################
# Definitionen der Funtionen:
##############################################################

#Überprüft ob die Zahl durch 2 Teilbar ist, ansonsten wird sie um 1 erhöht
def check_divisibility(num):
    if num % 2 != 0:
        num += 1
    return num

#Überprüfung der Inkludierten und Exkludierten Zahlen
def check_inclusions(str_num):

    #Exkludiert
    def check_exclusions():
        for exc in not_included:
            if str(exc) in str_num:
                return False
        return True
    
    #Inkludiert
    def check_inclusions():
        for inc in is_included:
            if str(inc) not in str_num:
                return False
        return True

    def check_couple_inclusions():
        is_couple_included = False
        for couple in couple_included:
            for inc in couple_included[couple]:
                if str(inc) in str_num:
                    is_couple_included = True
        return is_couple_included

    #Ausführung der beiden sup Funktionen
    return check_exclusions()  and check_inclusions() and check_couple_inclusions()

#Überprüfung der Teilbarkeit
def check_divisivility(num):

    #Darf Definitiv nicht Teilbar sein
    def check_undevisible():
        for div in not_divisible:
            if num % div == 0:
                return False
        return True
    
    #Muss Definitiv Teilbar sein
    def check_devisible():
        for div in is_divisible:
            if num % div != 0:
                return False
        return True
    
    #Ausführung der beiden sub funktionen
    return check_undevisible() and check_devisible()

#Main Loop Generiert durch 2 Teilbare Zahlen und Checkt die Bedingungen
def num_loop(min,max):
    for cur_num in range(min,max,2):
        if check_inclusions(str(cur_num)) and check_divisivility(cur_num):
            num_arr.append(cur_num)
            print(cur_num)

##############################################################
# Definition der Variablen:
##############################################################

not_included  = [1,4] #Exkludierte Zahlen
is_included   = []    #Inkludierte Zahlen
couple_included = {1:[2,5]} #Inkludierte Couple Zahlen (Eine der beiden zahlen muss existieren)

not_divisible = [20] #Definitiv nicht Teilbar durch
is_divisible  = [2] #Muss Teilbar sein durch

num_arr      = []    #Speichert die richtigen Zahlen. NICHT MANUEL ÄNDERN!!!!!!!!

max = 999                     #Nicht 4 Stellig
min = check_divisibility(400) #Min 400€ wegen Bild

##############################################################
# Programmablauf:
##############################################################


num_loop(min,max)
print("Anzahl Möglicher Zahlen: " , len(num_arr))
