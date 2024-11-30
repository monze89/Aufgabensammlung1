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
# # Übungsblatt 1

# ---
# Abgabe bis <b>Sonntag, 29. September 2024, 23:55 Uhr</b>

# ---
# ### Achtung:
# 
# - *Bitte speichern Sie Ihre Quellcode-Dateien (&ast;.c, &ast;.h, &ast;.cpp, &ast;.py, ...) im selben Ordner wie dieses Übungsblatt. Beachten Sie außerdem die Kommentare zur richtigen Benennung Ihrer Dateien. Nur so ist eine korrekte Abgabe und Auswertung Ihrer Lösungen möglich.*
# <br><br>
# - *Wenn Sie den angegebenen Variablen Werte zuweisen, dann stellen Sie sicher, dass diese Werte den richtigen Datentypen besitzen!*

# In[ ]:


import jagl
import os
import re


# # 1.1 Backus Normalform (25 %)
# 
# Welche der untenstehenden Möglichkeiten wird von der folgenden Backus Normalform abgedeckt?
# 
# `<mathFunction> ::= <string> "(" <number> <operation> <number> ")"`<br />
# `<functionName> ::= <string> | <string> "." <string>`<br />
# `<string> ::= <char> | <char> <string>`<br />
# `<char> ::= "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" | "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z"
# <operation> ::= "+" | "-" | "*" | "/"`<br />
# `<number> ::= <integer> | <float>`<br />
# `<integer> ::= <digit> | <digit> <integer>`<br />
# `<float> ::= <integer> "." <integer>`<br />
# `<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"`
# 
# Optionen:
# 
# a) print(4+9)<br />
# b) calc(13/7)<br />
# c) abs(12)<br />
# d) math.sqrt(62+2)<br />
# e) abs(23-65)<br />
# f) quadriere(19*7)<br />
# g) groesserHundert(13.37+86.63)<br />
# h) dividiertDurch0(12*3)

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 1")


# In[4]:


# Beantworten Sie die Frage, indem Sie die KORREKTEN Antworten in die unten stehende Liste einfügen. 
# Sind Ihrer Meinung nach die Antworten 'a', 'c' und 'e' korrekt, so sollte das Ergebnis **genau so** aussehen:
#
#         exercise_1_1_result = ["a", "c", "e"]
#
# Bitte vergessen Sie nicht, die einzelnen Antworten mit Anführungsstrichen zu umgeben 
# und durch Beistriche zu trennen, so wie es im obigen Beispiel zu sehen ist.

# Datentyp: list of strings
exercise_1_1_result = ["a", "b", "e", "g"]


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_1_1_solved = True


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_1_1(result, suite, case):
    varname = "exercise_1_1_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            jagl.check_variable_exists_and_has_type(result, globals(), "exercise_1_1_result", list)
            if result.isSucceeded():
                if len(exercise_1_1_result) > 0:
                    result.setSucceeded("Exercise solved.")
                else:
                    result.setFailed("exercise_1_1_result still contains the default value.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # 1.2 Erstellen einer Backus Normalform (25 %)
# 
# Erstellen Sie eine Backus Normalform (BNF), welche die folgenden drei URLs abdeckt:
#   * https://mars.mci4me.at:8000/test/test2/test3
#   * http://www.google.com
#   * https://www.mci.edu/en/university/the-mci/team-faculty
# 
# Hinweise:
#    * "/test/test2/test3" bzw. "en/university/the-mci/team-faculty" beschreiben den Serverpfad (`path`). Dieser kann beliebig lang sein und besteht immer aus einem führenden Schrägstrich (/) und einem `string` (= Zeichenkette).
#    * "http" bzw. "https" bezeichnen das Protokoll (`protocol`).
#    * ":8000" bezeichnet den angesteuerten Port (`port`). Dieser ist optional und wird meistens nicht angeführt.
#    * Sie müssen keine BNF erstellen, welche sämtliche URLs abdeckt, sondern **nur die drei oben angeführten**.
#    * Für Ihre Lösung bietet es sich an, die markierten Begriffe als Klassen der BNF zu verwenden.
#   
# Laden Sie Ihre Lösung als PDF-Datei mit dem Namen `BNF.pdf` auf JupyterHub hoch. Vergessen Sie nicht, das Übungsblatt mithilfe der `Submit`-Funktion abzugeben!

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 2")


# In[1]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!


# Datentyp: bool
exercise_1_2_solved = True


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_2_1(result, suite, case):
    varname = "exercise_1_2_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            result.setSucceeded("Exercise solved.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check files", deps=["1"])
def testcase_2_2(result, suite, case):
    result.setSucceeded()
    jagl.check_path_exists(result, files=["BNF.pdf"], message = "Did you upload all necessary files?")
    if result.isSucceeded():
        result.addMessage("All files were found.")


# In[ ]:





# In[ ]:





# In[ ]:





# # 1.3 Regular Expressions (25 %)
# 
# Gegeben sei folgende RegEx:
# 
# `^(00|\+)[0-9]{1,2} [\d]{1,3}( [\d]{2,3}){3}$`
# 
# Welche der folgenden Eingaben werden zu einem "Match" führen?
# 
# a) 0043 660 12 34 567<br />
# b) +18660 19 33 147<br />
# c) +43 699 9838712<br />
# d) +43 512 2070 991<br />
# e) 0043 512 20 70 512<br />
# f) +987654321<br />
# g) +0 99 67 18 210<br />
# h) 0033 1 919 533 12

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 3")


# In[ ]:


# Beantworten Sie die Frage, indem Sie die KORREKTEN Antworten in die unten stehende Liste einfügen. 
# Sind Ihrer Meinung nach die Antworten 'a', 'c' und 'e' korrekt, dann sollte das Ergebnis **genau so** aussehen:
#
#         exercise_1_3_result = ["a", "c", "e"]
#
# Bitte vergessen Sie nicht, die einzelnen Antworten mit Anführungsstrichen zu umgeben 
# und durch Beistriche zu trennen, so wie es im obigen Beispiel zu sehen ist.

# Datentyp: list of strings
exercise_1_3_result = ["a"]

# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_1_3_solved = True


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_3_1(result, suite, case):
    varname = "exercise_1_3_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            jagl.check_variable_exists_and_has_type(result, globals(), "exercise_1_3_result", list)
            if result.isSucceeded():
                if len(exercise_1_3_result) > 0:
                    result.setSucceeded("Exercise solved.")
                else:
                    result.setFailed("exercise_1_3_result still contains the default value.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # 1.4 Regular Expressions zur Eingabeüberprüfung (25 %)
# Sie wurden zur Erstellung eines Onlineshops beauftragt, bei welchem sich Kunden mit ihrer Email-Adresse registrieren können.
# Um fehlerhafte Einträge gar nicht erst in die Datenbank aufzunehmen, soll bei der Eingabe überprüft werden, ob es sich um eine
# gültige Email-Adresse handelt. Lösen Sie dies mithilfe einer Regular Expression.
# 
# Um die Aufgabe besser verstehen zu können, folgt zunächst eine kurze Einführung in die Syntax von Email-Adressen.
# 
# Eine Email-Adresse muss auf eine Domain verweisen, was durch das @-Symbol erreicht wird. Die Domain (alles hinter dem @-Symbol) besteht wiederum aus einem Hostnamen (z.B. mci4me),
# einer Top-Level-Domain (z.B. at) und ggf. einer Second-Level-Domain (z.B. bei .co.uk -> .co stellt in diesem Fall die Second-Level-Domain dar). Die Second-Level-Domain ist also
# optional und muss nicht zwangsläufig vorkommen! Sowohl Top-, als auch Second-Level-Domain sind strikt nicht-numerisch und bestehen daher ausschließlich aus lateinischen Kleinbuchstaben
# von a bis z (keine Umlaute, kein ß).
# Der Hostname unterliegt folgenden Restriktionen:
#    * Groß- und Kleinbuchstaben (keine Umlaute, kein ß) dürfen verwendet werden.
#    * Zahlen von 0-9 dürfen verwendet werden.
#    * Bindestriche (-) dürfen verwendet werden, sofern diese NICHT zu Beginn oder am Ende des Hostnamens stehen.
# 
# Zusammenfassend besteht die Domain demnach aus drei Teilen - dem Hostnamen (mci4me), einer Second-Level-Domain (.co) und einer Top-Level-Domain (.uk).
# Die komplette Domain, inklusive dem @-Symbol würde also so lauten: @mci4me.co.uk. Wie aus dem Beispiel schön hervorgeht können Zahlen lediglich im Hostnamen vorkommen, nicht aber in der Second- bzw. Top-Level-Domain.
# 
# Beim lokalen Teil der Email-Adresse (vor dem @-Symbol) sind folgende Zeichen zulässig:
#    * Groß- und Kleinbuchstaben (keine Umlaute, ß)
#    * Zahlen von 0-9
#    * Diese Sonderzeichen: <span>&+-=_~</span>
#    * Punkte, sofern diese NICHT zu Beginn oder am Ende des lokalen Teils stehen
# 
# Hinweis: Die oben beschriebene Syntax spiegelt nicht exakt die Realität wieder, sondern eine Vereinfachung zum Zwecke dieser Übungsaufgabe. Detaillierte Informationen zur "Beschaffenheit" von Email-Adressen
# finden Sie [hier](https://en.wikipedia.org/wiki/Email_address).
# 

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 4")


# In[ ]:


# Beantworten Sie die Frage, indem Sie den korrekten String für die RegEx als Wert der Variable 
# 'exercise_1_4_result' angeben. Eine Beispielantwort sieht so aus:
#
#         exercise_1_4_result = r"(\d{3}) (.*)"
# 
# Bitte vergessen Sie nicht, Ihre Antwort mit Anführungszeichen zu umgeben und vor das erste Anführungszeichen
# ein 'r' zu schreiben, so wie im obigen Beispiel zu sehen ist.
#
# Für Interessierte: das 'r' vor dem Anführungszeichen kennzeichnet in Python einen sog. Raw String (siehe 
# https://www.journaldev.com/23598/python-raw-string). Dadurch muss man den Backslash \ nicht zusätzlich escapen.

# Datentyp: string
exercise_1_4_result = r"^[a-zA-Z0-9&+\-=_~]+(\.[a-zA-Z0-9&+\-=_~]+)*@[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*\.[a-z]{2,}(?:\.[a-z]{2,})?$"

# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_1_4_solved = True


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_4_1(result, suite, case):
    varname = "exercise_1_4_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            jagl.check_variable_exists_and_has_type(result, globals(), "exercise_1_4_result", str)
            if result.isSucceeded():
                if len(exercise_1_4_result) > 0:
                    result.setSucceeded("Exercise solved.")
                else:
                    result.setFailed("exercise_1_4_result still contains the default value.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:



@jagl.testcase("2", desc="Check result", deps=["1"])
def testcase_4_2(result, suite, case):
    tests = [
        "a@mci4me.at",
        "a@somedomain.co.uk",
        "a@some-domain.at",
        "a@some-domain.co.uk",
        "a@some-other-domain.at",
        "a@some-other-domain.co.uk",
        "a@some-4-domain.at",
        "a@some-4-domain.co.uk",
        "a@DOMAIN.co.uk"
    ]
    
    try:
        p = re.compile(exercise_1_4_result)
        for t in tests:
            if not p.match(t):
                result.setFailed("Expression \"" + str(t) + "\" was evaluated as not being valid despite being valid.")
            else:
                result.setSucceeded("Expression \"" + str(t) + "\" was correctly evaluated as valid.")
    except re.error as e:
        result.setFailed("Given regular expression is not valid: " + str(e))
    except Exception as e:
        result.setFailed("Unknown error during autograding: " + str(e))


# In[ ]:



@jagl.testcase("3", desc="Check result", deps=["1"])
def testcase_4_3(result, suite, case):
    tests = [
        "a@mci4me",
        "a@somedomain.co.uk.tl1.tl2",
        "a@-somedomain.at",
        "a@somedomain-.at",
        "a@-somedomain-.at",
        "a@-some-domain-.at",
        "a@-some-domain-.co.uk",
        "a@some-other-domain,at",
        "a@some-other-domain.co4.u3k",
        "a@some-other-domain.co.uk bla bla",
        "a@some-4-domain.c?o.ußk",
        "a@DOMAIN.CO.UK"
    ]
    
    try:
        p = re.compile(exercise_1_4_result)
        for t in tests:
            if p.match(t):
                result.setFailed("Expression \"" + str(t) + "\" was evaluated as valid despite not being valid.")
            else:
                result.setSucceeded("Expression \"" + str(t) + "\" was correctly evaluated as not valid.")
    except re.error as e:
        result.setFailed("Given regular expression is not valid: " + str(e))
    except Exception as e:
        result.setFailed("Unknown error during autograding: " + str(e))


# In[ ]:



@jagl.testcase("4", desc="Check result", deps=["1"])
def testcase_4_4(result, suite, case):
    tests = [
        "somename@mci4me.at",
        "SomeName@mci4me.at",
        "some.name@mci4me.at",
        "some.other.name@mci4me.at",
        "Some.Other.Name@mci4me.at",
        "Some_Other_Name@mci4me.at",
        "1234567890@mci4me.at",
        "1.2.3.4.5.6.7.8.9.0@mci4me.at",
        "hallo.1.2.3.4.5.6.7.8.9.0.welt@mci4me.at",
        "hallo-1-2-3-4-5-6-7-8-9-0-welt@mci4me.at",
        "hallo.&.+.-.=._.~.welt@mci4me.at"
    ]
    
    try:
        p = re.compile(exercise_1_4_result)
        for t in tests:
            if not p.match(t):
                result.setFailed("Expression \"" + str(t) + "\" was evaluated as not valid despite being valid.")
            else:
                result.setSucceeded("Expression \"" + str(t) + "\" was correctly evaluated as valid.")
    except re.error as e:
        result.setFailed("Given regular expression is not valid: " + str(e))
    except Exception as e:
        result.setFailed("Unknown error during autograding: " + str(e))


# In[ ]:



@jagl.testcase("5", desc="Check result", deps=["1"])
def testcase_4_5(result, suite, case):
    tests = [
        "hallo.@mci4me.at",
        ".hallo@mci4me.at",
        ".hallo.@mci4me.at",
        ".hallo.hallo.@mci4me.at",
        "ä.ö.ü.ß@mci4me.at",
        "Ä.Ö.Ü@mci4me.at",
    ]
    
    try:
        p = re.compile(exercise_1_4_result)
        for t in tests:
            if p.match(t):
                result.setFailed("Expression \"" + str(t) + "\" was evaluated as valid despite not being valid.")
            else:
                result.setSucceeded("Expression \"" + str(t) + "\" was correctly evaluated as not valid.")
    except re.error as e:
        result.setFailed("Given regular expression is not valid: " + str(e))
    except Exception as e:
        result.setFailed("Unknown error during autograding: " + str(e))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




