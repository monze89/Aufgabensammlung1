#!/usr/bin/env python
# coding: utf-8

# ---
# Stellen Sie bitte sicher, dass alles wie vorhergesehen läuft, bevor Sie dieses Übungsblatt abgeben. **Starten Sie den Kernel neu** (in der Menüleiste die Option Kernel$\rightarrow$Restart auswählen) und **validieren** Sie anschließend das Übungsblatt (in der Menüleiste auf Validate klicken) um Rückmeldung zu eventuellen fehlenden oder fehlerhaften Eingaben zu erhalten. 
# 
# Füllen Sie alle Stellen im Übungsblatt aus, welche entweder `DEIN CODE HIER` oder "DEINE ANTWORT HIER" enthalten. Geben Sie unterhalb Ihren vollständigen Namen an.
# 
# Wenn Sie Code-Bestandteile aus anderen Quellen (wie z.B. Stackoverflow) kopieren, dann machen sie den kopierten Code in ihrer Quellcodedatei kenntlich und fügen eine Referenz auf die Quelle als Kommentar hinzu.
# 
# Wenn Sie die Aufgaben in einer Gruppe erledigen, dann fügen Sie die Namen aller Gruppenmitglieder in der nachfolgende Zelle zu `Name` und zusätzlich als Kommentar am Anfang Ihrer Quellcodedatei hinzu.

# ---

# In[ ]:


NAME = "Manuel Brunner"


# ---

# <table style="width: 100%">
#     <tr style="background: #ffffff">
#         <td style="width: 240px"><img src="https://mci.edu/templates/mci/images/logo.svg" alt="Logo"></td>
#         <td style="width: 100%">
#             <div style="text-align:right; width: 100%; text-align:right"><font size="7"><b>Programmiertechnik</b></font></div>
#             <div style="padding-top:20px; width: 100%; text-align:right"><font size="5"><b>WS 2024/25</b></font></div>
#         </td>
#     </tr>
# </table>

# ---
# # Übungsblatt 4

# ---
# Abgabe bis <b>Sonntag, 10. November 2024, 23:55 Uhr</b>

# In[ ]:


import jagl
import os
import re
import types
import sys

def check_format_bin(varname, number, result):
    symbols = "01"
    errmsg = varname + " has wrong format. Should be a binary number."
    okmsg = varname + " has correct format."
    if len(number) == 0:
        result.setFailed(varname + " is an empty string")
    elif number[:2].upper() == "0B":
        if not all(c in symbols for c in number[2:]):
            result.setFailed(errmsg)
        else:
            result.setSucceeded(okmsg)
    else:
        if not all(c in symbols for c in number):
            result.setFailed(errmsg)
        else:
            result.setSucceeded(okmsg)

            
def check_format_bin_comma(varname, number, result):
    symbols = "01."
    errmsg = varname + " has wrong format. Should be a binary number."
    okmsg = varname + " has correct format."
    if len(number) == 0:
        result.setFailed(varname + " is an empty string")
    elif number[:2].upper() == "0B":
        if not all(c in symbols for c in number[2:]):
            result.setFailed(errmsg)
        else:
            result.setSucceeded(okmsg)
    else:
        if not all(c in symbols for c in number):
            result.setFailed(errmsg)
        else:
            result.setSucceeded(okmsg)



def check_format_oct(varname, number, result):
    symbols = "01234567"
    errmsg = varname + " has wrong format. Should be a octal number."
    okmsg = varname + " has correct format."
    if len(number) == 0:
        result.setFailed(varname + " is an empty string")
    elif number[:2].upper() == "0O":
        if len(number) == 2 or not all(c in symbols for c in number[2:]):
            result.setFailed(errmsg)
        else:
            result.setSucceeded(okmsg)
    elif number[:1].upper() == "0":
        if len(number) == 1 or not all(c in symbols for c in number[1:]):
             result.setFailed(errmsg)
        else:
            result.setSucceeded(okmsg)
    else:
        if len(number) == 0 or not all(c in symbols for c in number):
            result.setFailed(errmsg)
        else:
            result.setSucceeded(okmsg)


def check_format_hex(varname, number, result):
    symbols = "0123456789ABCDEFabcdef"
    errmsg = varname + " has wrong format. Should be a hexadecimal number."
    okmsg = varname + " has correct format."
    if len(number) == 0:
        result.setFailed(varname + " is an empty string")
    elif number[:2].upper() == "0X":
        if len(number) == 2 or not all(c in symbols for c in number[2:]):
            result.setFailed(errmsg)
        else:
            result.setSucceeded(okmsg)
    else:
        if len(number) == 0 or not all(c in symbols for c in number):
            result.setFailed(errmsg)
        else:
            result.setSucceeded(okmsg)

def check_format_dec(varname, number, result):
    symbols = "0123456789"
    errmsg = varname + " has wrong format. Should be a decimal number."
    okmsg = varname + " has correct format."
    if len(number) == 0:
        result.setFailed(varname + " is an empty string")
    else:
        if len(number) == 0 or not all(c in symbols for c in number):
            result.setFailed(errmsg)
        else:
            result.setSucceeded(okmsg)


# ---
# ## 4.1 Zahlensysteme - Algorithmus zur Umrechnung (40 %)
# 
# Schreiben Sie eine Funktion `convertNumber(n, B)`, welche die übergebene Dezimalzahl `n` in das Zahlensystem mit der Basis `B` konvertiert. Das Ergebnis soll in Form einer Zeichenkette zurückgegeben werden. Dies kann durch folgende Schritte erreicht werden:
# 1. Berechne n : B (n dividiert durch b) = y Rest z
# 2. Solange y > 0 (größer 0): Mache y zum neuen n und wiederhole Schritt 1.
# 3. Die Restwerte z ergeben von unten nach oben gelesen die gesuchte Zahlendarstellung.
# 
# Gehen Sie am besten folgendermaßen vor:
# 1. Berechnen Sie den Rest der Division.
# 2. Konvertieren Sie den Rest zu einem String und hängen Sie ihn an den bestehenden String aus Restwerten an.
# 3. Berechnen sie das neue "y"
# 4. Reversieren Sie den String
# 
# Zur Lösung der Aufgabe benötigen Sie folgende Informationen:
# * Eine Zahl kann in Python mittels `str(zahl)` in einen String umgewandelt werden.
# * Strings können mithilfe des `+` aneinandergereiht (= konkatenieren) werden - z.B. folgt aus `x = "a" + "b"` das Ergebnis `x == "ab"`
# * Strings können wie folgt reversiert ("umgedreht") werden:
#   * `result = "abc"`
#   * `result = result[::-1]`
#   * Die Variable "result" enthält nun "cba"
# * Man kann diese Aufgabe auch lösen, ohne den String am Ende umdrehen zu müssen. Finden Sie diese Lösung?
#   
# <div class="alert alert-block alert-info">
#     <b>Info:</b> Die Umrechnung muss nur für Zahlensysteme der Basis <b>kleiner</b> 10 funktionieren.
# </div>

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 1")


# In[6]:


# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Die Zahl, die umgewandelt werden kann wird an die untenstehende Funktion als "n" und die Basis des
# Zahlensystems als "B" übergeben.
# Die Variable "result" soll die Lösung als String enthalten.

def convertNumber(n, B):
    result = ''
    
    while n > 0:
        rest = n % B
        result = str(rest) + result
        n = n // B
    
    return result


# In[ ]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_4_1_solved = True


# In[7]:


# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.

convertNumber(128, 2)


# In[8]:


# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.

convertNumber(24, 8)


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_1_1(result, suite, case):
    varname = "exercise_4_1_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            result.setSucceeded("Exercise solved.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check Function convertNumber()", deps=["1"])
def testcase_1_2(result, suite, case):
    jagl.check_variable_exists_and_has_type(result, globals(), "convertNumber", types.FunctionType)
    if result.isSucceeded():
        def _convertNumber_(n, B):
            result = ''
            z = n % B
            while n > 0:
                z = str(n % B)
                result = z + result
                n = int(n / B)
            return result
        for x in [[128, 2], [0, 3], [2322, 9], [12345, 10], [54321, 2], [2313, 4]]:
            res1 = convertNumber(*x)
            truth = _convertNumber_(*x)
            if not isinstance(res1, type(truth)):
                result.setFailed(f"Return value of convertNumber({x}) has the wrong type ({type(res1)} instead of {type(truth)})")
            elif res1 == truth:
                result.setSucceeded(f"convertNumber({x}) returns the correct value")
            else:
                result.setFailed(f"convertNumber({x}) returns the wrong value ({res1} instead of {truth})")


# In[ ]:





# In[ ]:





# In[ ]:





# ---
# ## 4.2 Umwandlung von Ganzzahlen (10 %)
# 
# Wandeln Sie die folgende Zahl vom Dezimalsystem ins Binär-, Oktal-, und Hexadezimalsystem um.
# 

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 2")


# ---
# &nbsp; &nbsp; &nbsp; $58_{(10)}$

# In[3]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_4_2_solved = True

# Bitte verwenden Sie die folgende Formatvorlage um Ihre Ergebnisse anzugeben.
# Fügen Sie Ihre Lösungen zwischen die dafür vorgesehenen Anführungszeichen ein.
# Um Fehler in der Auswertung zu vermeiden, verzichten Sie bitte auf führende Nullen.
# exercise_4_2_result_a2 = "<58(10) als Binärzahl>"
# exercise_4_2_result_a8 = "<58(10) als Oktalzahl>"
# exercise_4_2_result_a16 = "<58(10) als Hexadezimalzahl>"

# Datentyp: string
exercise_4_2_result_a2 = "111010"
exercise_4_2_result_a8 = "72"
exercise_4_2_result_a16 = "3A"


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_2_1(result, suite, case):
    varname = "exercise_4_2_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    jagl.check_variable_exists_and_has_type(result, globals(), "exercise_4_2_result_a2", str)
    jagl.check_variable_exists_and_has_type(result, globals(), "exercise_4_2_result_a8", str)
    jagl.check_variable_exists_and_has_type(result, globals(), "exercise_4_2_result_a16", str)
    if result.isSucceeded():
        if eval(varname):
            if exercise_4_2_result_a2 != "" and exercise_4_2_result_a8 != "" and exercise_4_2_result_a16 != "":
                result.setSucceeded("Exercise solved.")
            else:
                result.setFailed("One of the result variables still contains the default value")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check number formats", deps=["1"])
def testcase_2_2(result, suite, case):
    check_format_bin("exercise_4_2_result_a2", exercise_4_2_result_a2, result)
    check_format_oct("exercise_4_2_result_a8", exercise_4_2_result_a8, result)
    check_format_hex("exercise_4_2_result_a16", exercise_4_2_result_a16, result)


# In[ ]:





# In[ ]:





# In[ ]:





# ---
# ## 4.3 Rechnen mit Ganzzahlen (10 %)
# 
# Führen Sie folgende Berechnungen mit Ganzzahlen durch.

# a.&nbsp; &nbsp; &nbsp;Lösen Sie die folgende Addition direkt im Binär-, Oktal-, und Hexadezimalsystem.
# 
# &nbsp; &nbsp; &nbsp; &nbsp;$29_{(10)} + 117_{(10)}$

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 3a")


# In[4]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_4_3a_solved = True

# Bitte verwenden Sie die folgende Formatvorlage um Ihre Ergebnisse anzugeben. 
# Fügen Sie Ihre Lösungen zwischen die dafür vorgesehenen Anführungszeichen ein.
# Um Fehler in der Auswertung zu vermeiden, verzichten Sie bitte auf führende Nullen.
# exercise_4_3_result_a2 = "<Summe als Binärzahl>"
# exercise_4_3_result_a8 = "<Summe als Oktalzahl>"
# exercise_4_3_result_a16 = "<Summe als Hexadezimalzahl>"

# Datentyp: string
exercise_4_3_result_a2 = "10010010"
exercise_4_3_result_a8 = "222"
exercise_4_3_result_a16 = "92"


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_3a_1(result, suite, case):
    varname = "exercise_4_3a_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    jagl.check_variable_exists_and_has_type(result, globals(), "exercise_4_3_result_a2", str)
    jagl.check_variable_exists_and_has_type(result, globals(), "exercise_4_3_result_a8", str)
    jagl.check_variable_exists_and_has_type(result, globals(), "exercise_4_3_result_a16", str)
    if result.isSucceeded():
        if eval(varname):
            if exercise_4_3_result_a2 != "" and exercise_4_3_result_a8 != "" and exercise_4_3_result_a16 != "":
                result.setSucceeded("Exercise solved.")
            else:
                result.setFailed("One of the result variables still contains the default value")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check number formats", deps=["1"])
def testcase_3a_2(result, suite, case):
    check_format_bin("exercise_4_3_result_a2", exercise_4_3_result_a2, result)
    check_format_oct("exercise_4_3_result_a8", exercise_4_3_result_a8, result)
    check_format_hex("exercise_4_3_result_a16", exercise_4_3_result_a16, result)


# In[ ]:





# In[ ]:





# In[ ]:





# ---
# b.&nbsp; &nbsp; &nbsp;Lösen Sie die folgende Subtraktion direkt im Binärsystem. Verwenden Sie dazu das Zweier-Komplement und rechnen Sie mit 8-Bit Zahlen (Füllen Sie dazu die angegebenen Zahlen entsprechend auf). Geben Sie zusätzlich zum Ergebnis der Rechnung auch an, wie oft es zu einem Übertrag kommt.
# 
# &nbsp; &nbsp; &nbsp; &nbsp;$(-58_{(10)}) - 29_{(10)}$

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 3b")


# In[ ]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_4_3b_solved = True

# Bitte verwenden Sie die folgende Formatvorlage um Ihre Ergebnisse anzugeben. 
# exercise_4_3_result_b2 = "<Differenz als 8-Bit Binärzahl>"
# exercise_4_3_result_b10 = <Anzahl der Überträge als Dezimalzahl>

# Datentyp: string
exercise_4_3_result_b2 = "10101001"
# Datentyp: int
exercise_4_3_result_b10 = 4


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_3b_1(result, suite, case):
    varname = "exercise_4_3b_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    jagl.check_variable_exists_and_has_type(result, globals(), "exercise_4_3_result_b2", str)
    jagl.check_variable_exists_and_has_type(result, globals(), "exercise_4_3_result_b10", int)
    if result.isSucceeded():
        if eval(varname):
            if exercise_4_3_result_b2 != "" and exercise_4_3_result_b10 != -1:
                result.setSucceeded("Exercise solved.")
            else:
                result.setFailed("One of the result variables still contains the default value")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check number formats", deps=["1"])
def testcase_3b_2(result, suite, case):
    check_format_bin("exercise_4_3_result_b2", exercise_4_3_result_b2, result)


# In[ ]:





# In[ ]:





# In[ ]:





# ---
# ## 4.4 Umwandeln von Festkommazahlen ins Binärsystem (10 %)
# 
# Wandeln Sie folgende Festkommazahlen vom Dezimalsystem ins Binärsystem um. Verwenden Sie für Ihre Rechnung ein Format mit exakt 8 Vorkommastellen und exakt 8 Nachkommastellen. Geben Sie zusätzlich zum Ergebnis der Umwandlung an, ob die erhaltene binäre Festkommazahl in diesem Format korrekt dargestellt werden kann (sowohl im Vorkomma-, als auch im Nachkommabereich).

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 4")


# a.&nbsp;&nbsp;&nbsp;$103,8125_{(10)}$

# In[ ]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_4_4_solved = True

# Bitte verwenden Sie die folgende Formatvorlage um Ihre Ergebnisse anzugeben.
# Fügen Sie Ihre Lösungen zwischen die dafür vorgesehenen Anführungszeichen ein.
# exercise_4_4_result1 = "<Ergebnis der Umwandlung>"
# exercise_4_4_result2 = <Exakte Darstellung Vorkommabereich ::= True | False>
# exercise_4_4_result3 = <Exakte Darstellung Nachkommabereich ::= True | False>

# Datentyp: string
exercise_4_4_result1 = "01100111.11010000"
# Datentyp: bool
exercise_4_4_result2 = True
# Datentyp: bool
exercise_4_4_result3 = True


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_4_1(result, suite, case):
    varname = "exercise_4_4_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    jagl.check_variable_exists_and_has_type(result, globals(), "exercise_4_4_result1", str)
    jagl.check_variable_exists_and_has_type(result, globals(), "exercise_4_4_result2", bool)
    jagl.check_variable_exists_and_has_type(result, globals(), "exercise_4_4_result3", bool)
    if result.isSucceeded():
        if eval(varname):
            if exercise_4_4_result1 != "":
                result.setSucceeded("Exercise solved.")
            else:
                result.setFailed("The result variable still contains the default value")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:



@jagl.testcase("2", desc="Check number formats", deps=["1"])
def testcase_4_2(result, suite, case):
    check_format_bin_comma("exercise_4_4_result1", exercise_4_4_result1, result)


# In[ ]:





# In[ ]:





# In[ ]:





# ---
# ## 4.5 Umwandeln von Gleitkommazahlen ins Binärsystem (10 %)
# 
# Wandeln Sie die folgende Gleitkommazahl vom Dezimalsystem ins Binärsystem um. Stellen Sie die Lösung als binäre Gleitkommazahl mit einfacher Genauigkeit im IEEE 754 Format dar. Geben Sie zusätzlich zum Ergebnis der Umwandlung an, ob die erhaltene binäre Gleitkommazahl in diesem Format korrekt dargestellt werden kann.
# 
# &nbsp; &nbsp; &nbsp; &nbsp;$-2,5 * 10^{-2}$

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 5")


# In[ ]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_4_5_solved = True

# Bitte verwenden Sie die folgende Formatvorlage um Ihre Ergebnisse anzugeben.
# exercise_4_5_result1 = "<Binäre Gleitkommazahl mit einfacher Genauigkeit>"
# exercise_4_5_result2 = <Exakte Darstellung ::= True | False>

# Datentyp: string
exercise_4_5_result1 = "10111100110011001100110011001100"
# Datentyp: bool
exercise_4_5_result2 = False


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_5_1(result, suite, case):
    varname = "exercise_4_5_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    jagl.check_variable_exists_and_has_type(result, globals(), "exercise_4_5_result1", str)
    jagl.check_variable_exists_and_has_type(result, globals(), "exercise_4_5_result2", bool)
    if result.isSucceeded():
        if eval(varname):
            if exercise_4_5_result1 != "":
                result.setSucceeded("Exercise solved.")
            else:
                result.setFailed("The result variable still contains the default value")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check number formats", deps=["1"])
def testcase_5_2(result, suite, case):
    check_format_bin("exercise_4_5_result1", exercise_4_5_result1, result)


# In[ ]:





# In[ ]:





# In[ ]:





# ---
# ## 4.6 Rechnen mit Festkommazahlen im Binärsystem (10 %)
# 
# Lösen Sie die folgende Addition direkt im Binärsystem. Verwenden Sie für Ihre Rechnung ein Format mit exakt 8 Vorkommastellen und exakt 8 Nachkommastellen. Geben Sie zusätzlich zum Ergebnis der Addition an, ob die erhaltene binäre Festkommazahl in diesem Format im Vorkommabereich korrekt dargestellt werden kann. Geben Sie auch an, wie oft es bei dieser Addition zu einem Übertrag kommt.
# 
# &nbsp; &nbsp; &nbsp; &nbsp;$103,8125_{(10)} + 168,675_{(10)}$

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 6")


# In[ ]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_4_6_solved = True

# Bitte verwenden Sie die folgende Formatvorlage um Ihre Ergebnisse anzugeben.
# Fügen Sie Ihre Lösungen zwischen die dafür vorgesehenen Anführungszeichen ein.
# exercise_4_6_result1 = "<Summe als Binärzahl>"
# exercise_4_6_result2 = <Exakte Darstellung Vorkommabereich ::= JA | NEIN>
# exercise_4_6_result3 = <Anzahl der Überträge bei der binären Addition als Dezimalzahl>

# Datentyp: string
exercise_4_6_result1 = "100011000.01111101"
# Datentyp: bool
exercise_4_6_result2 = False
# Datentyp: int
exercise_4_6_result3 = 3


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_6_1(result, suite, case):
    varname = "exercise_4_6_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    jagl.check_variable_exists_and_has_type(result, globals(), "exercise_4_6_result1", str)
    jagl.check_variable_exists_and_has_type(result, globals(), "exercise_4_6_result2", bool)
    jagl.check_variable_exists_and_has_type(result, globals(), "exercise_4_6_result3", int)
    if result.isSucceeded():
        if eval(varname):
            if exercise_4_6_result1 != "" and exercise_4_6_result3 != -1:
                result.setSucceeded("Exercise solved.")
            else:
                result.setFailed("One of the result variables still contains the default value")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check number formats", deps=["1"])
def testcase_6_2(result, suite, case):
    check_format_bin_comma("exercise_4_6_result1", exercise_4_6_result1, result)


# In[ ]:





# In[ ]:





# In[ ]:





# ---
# ## 4.7 Rechnen mit Gleitkommazahlen im Binärsystem (10 %)
# 
# Lösen Sie die folgende Addition direkt im Binärsystem. Gegeben sind zwei binäre Gleitkommazahlen mit einfacher Genauigkeit im IEEE 754 Format. Stellen Sie Ihre Lösung ebenfalls in diesem Format dar.
# 
# $01000001001110010000000000000000 + 01000010101011011000000000000000$

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 7")


# In[ ]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_4_7_solved = True

# Bitte verwenden Sie die folgende Formatvorlage um Ihre Ergebnisse anzugeben.
# exercise_4_7_result = "<Summe als binäre Gleitkommazahl mit einfacher Genauigkeit>"

# Datentyp: string
exercise_4_7_result = "01000010010110110100000000000000"


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_7_1(result, suite, case):
    varname = "exercise_4_7_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    jagl.check_variable_exists_and_has_type(result, globals(), "exercise_4_7_result", str)
    if result.isSucceeded():
        if eval(varname):
            if exercise_4_7_result != "":
                result.setSucceeded("Exercise solved.")
            else:
                result.setFailed("One of the result variables still contains the default value")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check number formats", deps=["1"])
def testcase_7_2(result, suite, case):
    check_format_bin("exercise_4_7_result", exercise_4_7_result, result)


# In[ ]:





# In[ ]:




