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

# In[3]:


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
# # Übungsblatt 2

# ---
# Abgabe bis <b>Sonntag, 13. Oktober 2024, 23:55 Uhr</b>

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


# # 2.1 - Bilder extrahieren (40 %)
# 
# Sie möchten einen [web crawler](https://en.wikipedia.org/wiki/Web_crawler) für eine Suchmaschine implementieren, welcher die Bilder von Webseiten speichert. Dabei soll nicht das Bild selbst heruntergeladen werden, sondern nur dessen Beschreibung, Dateityp und Link. Um diese Anforderung zu erfüllen, soll zuerst kurz darauf eingegangen werden, wie Bilder auf Webseiten dargestellt werden.
# 
# Webseiten werden mithilfe der Auszeichnungssprache [HTML](https://www.w3schools.com/html/) erzeugt, welche sogenannte HTML-`Tags` nutzt, um die Seitenstruktur aufzubauen. Bilder werden durch einen `img`-Tag repräsentiert, welcher folgendermaßen aussieht:
# 
# Beispiel: `<img src="img_chania.jpg" alt="Flowers in Chania">`<br />
# Erklärung: Der Tag wird durch eine Spitzklammer (`Kleiner`-Zeichen) geöffnet und mit dem Tagnamen `img` als Bild Identifiziert. Attribute (`src` und `alt`) stehen immer alleine - sie sind also durch Leerzeichen getrennt). Die Zuweisung eines Wertes zum Attribut erfolgt mit einem `=`. Bei den Werten handelt es sich um Strings (= Zeichenketten), was durch die Anführungszeichen (") festgehalten wird. Am Ende wird der Tag durch eine Spitzklammer geschlossen.
# 
# Das Attribut `src` verweist auf den Speicherort der Bilddatei, welche sich auf dem lokalen Webserver oder irgendwo im Internet befinden kann. Ganz am Ende des Links befindet sich immer die Dateiendung (in diesem Fall jpg), welche durch einen Punkt vom Rest der Adresse getrennt wird.
# 
# Das Attribut `alt` enthält eine **alt**ernative Beschreibung. Diese wird angezeigt, wenn die Quelldatei aus `src` nicht gefunden werden kann oder wenn die Seite durch einen Screenreader für Menschen mit eingeschränktem Sehvermögen vorgelesen wird.
# 
# **Ihre Aufgabe:**<br />
# Ihr web crawler wird die Quelldateien von Webseiten analysieren und soll nun folgende Informationen von Bildern festhalten:
# * Die Beschreibung (aus dem `alt`-Attribut)
# * Das Dateiformat (die Dateiendung der Bilddatei)
# * Den Link zur Bilddatei (aus dem `src`-Attribut)
# 
# Setzen Sie diese Anforderungen mithilfe von `Regular Expressions` und deren [Capturing Groups](https://pynative.com/python-regex-capturing-groups) um.
# 
# **Hinweise:**<br />
# * Sie müssen **keinen** web crawler entwickeln, sondern nur die Regular Expression für die oben beschriebene Aufgabe.
# * Sie können davon ausgehen, dass am Ende des Links immer ein Punkt und die Dateieindung (z. B. `.jpg` oder `.gif`) steht.
# * Wenn ein `img`-Tag kein `alt`-Attribut oder dieses einen leeren String (`alt=""`), soll das entsprechende Element **nicht** festgehalten werden - wir möchten nur Bilder mit Alternativbeschreibungen speichern!
# * Die Reihenfolge von `src` und `alt` ist beliebig - das oben beschriebene Bild könnte also auch so dargestellt werden:<br />`<img alt="Flowers in Chania" src="img_chania.jpg">` 
# * Das Angaben zum `img`-Tag in HTML wurden zum Zwecke dieser Aufgabe vereinfacht.
# 
# Weitere, optionale Informationen zum `img`-Tag: [hier](https://www.w3schools.com/html/html_images.asp)

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 1")


# In[1]:



# Beantworten Sie die Frage, indem Sie den korrekten String für die RegEx als Wert der Variable 'exercise2_1' 
# angeben. Eine Beispielantwort sieht so aus:
#
#         exercise_2_1_result = r"(\d{3}) (.*)"
# 
# Bitte vergessen Sie nicht, Ihre Antwort mit Anführungszeichen zu umgeben und vor das erste Anführungszeichen
# ein 'r' zu schreiben, so wie im obigen Beispiel zu sehen ist.
#
# Für Interessierte: das 'r' vor dem Anführungszeichen kennzeichnet in Python einen sog. Raw String (siehe 
# https://www.journaldev.com/23598/python-raw-string). Dadurch muss man den Backslash \ nicht zusätzlich escapen.

# Datentyp: string
exercise_2_1_result = r'<img\s+(?:alt="([^"]+)"\s+src="([^"]+\.(jpg|png|gif|bmp))"|src="([^"]+\.(jpg|png|gif|bmp))"\s+alt="([^"]+)")'


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_2_1_solved = True


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_4_1(result, suite, case):
    varname = "exercise_2_1_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            jagl.check_variable_exists_and_has_type(result, globals(), "exercise_2_1_result", str)
            if result.isSucceeded():
                if len(exercise_2_1_result) > 0:
                    result.setSucceeded("Exercise solved.")
                else:
                    result.setFailed("exercise_2_1_result still contains the default value.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:



@jagl.testcase("3", desc="Check result", deps=["1"])
def testcase_4_2(result, suite, case):
    test = ('<img src="img_chania.jpg" alt="Flowers in Chania">', 'Flowers in Chania', 'jpg', 'img_chania.jpg')
    try:
        p = re.compile(exercise_2_1_result)
        m = p.match(test[0])
        if not m:
            result.setFailed("Expression \"" + str(test[0]) + "\" was evaluated as not being valid despite being valid.")
        else:
            result.setSucceeded("Expression \"" + str(test[0]) + "\" was correctly evaluated as valid.")
            alt_found = False
            for i in range(1, p.groups+1):
                if m.group(i) == test[1]:
                    alt_found = True
                    break
            if alt_found:
                result.setSucceeded("A capture group was found containing the alt-attribute.")
            else:
                result.setFailed("No capture group was found containing the alt-attribute.")
            de_found = False
            for i in range(1, p.groups+1):
                if m.group(i) == test[2] or m.group(i) == '.' + test[2]:
                    de_found = True
                    break
            if de_found:
                result.setSucceeded("A capture group was found containing the file extension.")
            else:
                result.setFailed("No capture group was found containing the file extension.")
            img_found = False
            for i in range(1, p.groups+1):
                if m.group(i) == test[3]:
                    img_found = True
                    break
            if img_found:
                result.setSucceeded("A capture group was found containing the image")
            else:
                result.setFailed("No capture group was found containing the image.")
    except re.error as e:
        result.setFailed("Given regular expression is not valid: " + str(e))
    except Exception as e:
        result.setFailed("Unknown error during autograding: " + str(e))


# In[ ]:



@jagl.testcase("4", desc="Check result", deps=["1"])
def testcase_4_3(result, suite, case):
    test = ('<img src="panda.gif" alt="Some Pandas">', 'Some Pandas', 'gif', 'panda.gif')
    try:
        p = re.compile(exercise_2_1_result)
        m = p.match(test[0])
        if not m:
            result.setFailed("Expression \"" + str(test[0]) + "\" was evaluated as not being valid despite being valid.")
        else:
            result.setSucceeded("Expression \"" + str(test[0]) + "\" was correctly evaluated as valid.")
            alt_found = False
            for i in range(1, p.groups+1):
                if m.group(i) == test[1]:
                    alt_found = True
                    break
            if alt_found:
                result.setSucceeded("A capture group was found containing the alt-attribute.")
            else:
                result.setFailed("No capture group was found containing the alt-attribute.")
            de_found = False
            for i in range(1, p.groups+1):
                if m.group(i) == test[2] or m.group(i) == '.' + test[2]:
                    de_found = True
                    break
            if de_found:
                result.setSucceeded("A capture group was found containing the file extension.")
            else:
                result.setFailed("No capture group was found containing the file extension.")
            img_found = False
            for i in range(1, p.groups+1):
                if m.group(i) == test[3]:
                    img_found = True
                    break
            if img_found:
                result.setSucceeded("A capture group was found containing the image")
            else:
                result.setFailed("No capture group was found containing the image.")
    except re.error as e:
        result.setFailed("Given regular expression is not valid: " + str(e))
    except Exception as e:
        result.setFailed("Unknown error during autograding: " + str(e))


# In[ ]:



@jagl.testcase("5", desc="Check result", deps=["1"])
def testcase_4_4(result, suite, case):
    test = ('<img src="snakes on a plane.bmp" alt="Some Snakes on a Plane">', 'Some Snakes on a Plane', 'bmp', 'snakes on a plane.bmp')
    try:
        p = re.compile(exercise_2_1_result)
        m = p.match(test[0])
        if not m:
            result.setFailed("Expression \"" + str(test[0]) + "\" was evaluated as not being valid despite being valid.")
        else:
            result.setSucceeded("Expression \"" + str(test[0]) + "\" was correctly evaluated as valid.")
            alt_found = False
            for i in range(1, p.groups+1):
                if m.group(i) == test[1]:
                    alt_found = True
                    break
            if alt_found:
                result.setSucceeded("A capture group was found containing the alt-attribute.")
            else:
                result.setFailed("No capture group was found containing the alt-attribute.")
            de_found = False
            for i in range(1, p.groups+1):
                if m.group(i) == test[2] or m.group(i) == '.' + test[2]:
                    de_found = True
                    break
            if de_found:
                result.setSucceeded("A capture group was found containing the file extension.")
            else:
                result.setFailed("No capture group was found containing the file extension.")
            img_found = False
            for i in range(1, p.groups+1):
                if m.group(i) == test[3]:
                    img_found = True
                    break
            if img_found:
                result.setSucceeded("A capture group was found containing the image")
            else:
                result.setFailed("No capture group was found containing the image.")
    except re.error as e:
        result.setFailed("Given regular expression is not valid: " + str(e))
    except Exception as e:
        result.setFailed("Unknown error during autograding: " + str(e))


# In[ ]:



@jagl.testcase("6", desc="Check result", deps=["1"])
def testcase_4_5(result, suite, case):
    test = ('<img alt="Some Pandas" src="panda.gif">', 'Some Pandas', 'gif', 'panda.gif')
    try:
        p = re.compile(exercise_2_1_result)
        m = p.match(test[0])
        if not m:
            result.setFailed("Expression \"" + str(test[0]) + "\" was evaluated as not being valid despite being valid.")
        else:
            result.setSucceeded("Expression \"" + str(test[0]) + "\" was correctly evaluated as valid.")
            alt_found = False
            for i in range(1, p.groups+1):
                if m.group(i) == test[1]:
                    alt_found = True
                    break
            if alt_found:
                result.setSucceeded("A capture group was found containing the alt-attribute.")
            else:
                result.setFailed("No capture group was found containing the alt-attribute.")
            de_found = False
            for i in range(1, p.groups+1):
                if m.group(i) == test[2] or m.group(i) == '.' + test[2]:
                    de_found = True
                    break
            if de_found:
                result.setSucceeded("A capture group was found containing the file extension.")
            else:
                result.setFailed("No capture group was found containing the file extension.")
            img_found = False
            for i in range(1, p.groups+1):
                if m.group(i) == test[3]:
                    img_found = True
                    break
            if img_found:
                result.setSucceeded("A capture group was found containing the image")
            else:
                result.setFailed("No capture group was found containing the image.")
    except re.error as e:
        result.setFailed("Given regular expression is not valid: " + str(e))
    except Exception as e:
        result.setFailed("Unknown error during autograding: " + str(e))


# In[ ]:



@jagl.testcase("7", desc="Check result", deps=["1"])
def testcase_4_6(result, suite, case):
    test = ('<img alt="Some Snakes on a Plane" src="snakes on a plane.bmp">', 'Some Snakes on a Plane', 'bmp', 'snakes on a plane.bmp')
    try:
        p = re.compile(exercise_2_1_result)
        m = p.match(test[0])
        if not m:
            result.setFailed("Expression \"" + str(test[0]) + "\" was evaluated as not being valid despite being valid.")
        else:
            result.setSucceeded("Expression \"" + str(test[0]) + "\" was correctly evaluated as valid.")
            alt_found = False
            for i in range(1, p.groups+1):
                if m.group(i) == test[1]:
                    alt_found = True
                    break
            if alt_found:
                result.setSucceeded("A capture group was found containing the alt-attribute.")
            else:
                result.setFailed("No capture group was found containing the alt-attribute.")
            de_found = False
            for i in range(1, p.groups+1):
                if m.group(i) == test[2] or m.group(i) == '.' + test[2]:
                    de_found = True
                    break
            if de_found:
                result.setSucceeded("A capture group was found containing the file extension.")
            else:
                result.setFailed("No capture group was found containing the file extension.")
            img_found = False
            for i in range(1, p.groups+1):
                if m.group(i) == test[3]:
                    img_found = True
                    break
            if img_found:
                result.setSucceeded("A capture group was found containing the image")
            else:
                result.setFailed("No capture group was found containing the image.")
    except re.error as e:
        result.setFailed("Given regular expression is not valid: " + str(e))
    except Exception as e:
        result.setFailed("Unknown error during autograding: " + str(e))


# In[ ]:



@jagl.testcase("8", desc="Check result", deps=["1"])
def testcase_4_7(result, suite, case):
    test = ('<img alt="Flowers in Chania" src="img_chania.jpg">', 'Flowers in Chania', 'jpg', 'img_chania.jpg')
    try:
        p = re.compile(exercise_2_1_result)
        m = p.match(test[0])
        if not m:
            result.setFailed("Expression \"" + str(test[0]) + "\" was evaluated as not being valid despite being valid.")
        else:
            result.setSucceeded("Expression \"" + str(test[0]) + "\" was correctly evaluated as valid.")
            alt_found = False
            for i in range(1, p.groups+1):
                if m.group(i) == test[1]:
                    alt_found = True
                    break
            if alt_found:
                result.setSucceeded("A capture group was found containing the alt-attribute.")
            else:
                result.setFailed("No capture group was found containing the alt-attribute.")
            de_found = False
            for i in range(1, p.groups+1):
                if m.group(i) == test[2] or m.group(i) == '.' + test[2]:
                    de_found = True
                    break
            if de_found:
                result.setSucceeded("A capture group was found containing the file extension.")
            else:
                result.setFailed("No capture group was found containing the file extension.")
            img_found = False
            for i in range(1, p.groups+1):
                if m.group(i) == test[3]:
                    img_found = True
                    break
            if img_found:
                result.setSucceeded("A capture group was found containing the image")
            else:
                result.setFailed("No capture group was found containing the image.")
    except re.error as e:
        result.setFailed("Given regular expression is not valid: " + str(e))
    except Exception as e:
        result.setFailed("Unknown error during autograding: " + str(e))


# In[ ]:



@jagl.testcase("9", desc="Check result", deps=["1"])
def testcase_4_8(result, suite, case):
    tests = [
        '<img>',
        '<img src="" alt="">',
        '<img src="pandas.gif" alt="">',
        '<img src="" alt="Some Pandas">',
        '<img alt="Some Pandas">',
        '<img src="pandas.gif">'
    ]
    
    try:
        p = re.compile(exercise_2_1_result)
        for t in tests:
            if p.match(t):
                result.setFailed("Expression \"" + str(t) + "\" was evaluated as being valid despite not being valid.")
            else:
                result.setSucceeded("Expression \"" + str(t) + "\" was correctly evaluated as not valid.")
    except re.error as e:
        result.setFailed("Given regular expression is not valid: " + str(e))
    except Exception as e:
        result.setFailed("Unknown error during autograding: " + str(e))


# In[ ]:





# In[ ]:





# In[ ]:





# # 2.2 - Division mit Rest: Problemspezifikation (20 %)
# 
# Es soll ein Algorithmus für das Problem der [Division mit Rest](https://de.wikipedia.org/wiki/Division_mit_Rest) formuliert werden. Wie wir ja schon gehört haben, ist der erste Schritt auf dem Weg vom Problem zum Algorithmus das vollständige Verstehen der Problemstellung.
# 
# Daher soll in dieser Aufgabe eine Problemspezifikation für die Division mit Rest gefunden und in natürlicher Sprache niedergeschrieben werden. Die Problemspezifikation soll alle notwendigen Eigenschaften wie Eindeutigkeit, Vollständigkeit und Detailliertheit erfüllen (siehe Folie 8 und 9 des Foliensatzes der Lesson 2). Zusätzlich sollen auch die Vor- und Nachbedingungen der Division mit Rest niedergeschrieben werden.
# 
# Schreiben Sie Ihre Problemspezifikation und die Vor- und Nachbedingungen unten in die dafür vorgesehenen Zellen.

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 2")


# #### Problemspezifikation:

# Bei Division mit Rest müssen zwei ganze Zahlen verwendet werden um eine Division auszuführen.
# Dabei wird der Dividend durch den Divisor geteilt. 
# Dabei soll ein Ergebnis (Quotient) und ein Rest als Ergebnis ermittelt werden.
# 

# #### Vorbedingung:

# Dividend und Divisor müssen ganze Zahlen sein.
# Der Divisor darf nicht 0 sein.
# 

# #### Nachbedingung:

# Das Ergebnis muss größer oder gleich 0 sein.Der Rest muss größer oder 0 sein und muss gleichzeitig kleiner als der Divisor sein.

# In[ ]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_2_2_solved = True


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_2_1(result, suite, case):
    varname = "exercise_2_2_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            result.setSucceeded("Exercise solved.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:





# In[ ]:





# In[ ]:





# # 2.3 - Division mit Rest: Algorithmus (20 %)
# 
# Nachdem wir die Problemstellung der Division mit Rest in Aufgabe 2.2 vollständig verstanden haben, können wir in dieser Aufgabe als nächsten Schritt einen Algorithmus formulieren und niederschreiben, der die Problemstellung löst. Der Algorithmus soll wieder alle notwendigen Eigenschaften (siehe Definition nach Kübe auf dem Foliensatz der Lesson 2) erfüllen.
# 
# Ein Algorithmus kann auf verschiedenste Arten und Weisen niedergeschrieben werden. Für diese Aufgabe wollen wir den Algorithmus in zwei verschiedenen Formen niederschreiben: (1) in natürlicher Sprachen und (2) in Form eines Flußdiagramms (auf Folie 21 des Foliensatzes der Lesson 2 finden Sie ein Beispiel für beide Formen). Geben Sie auch noch zusätzlich mit an, welche Grundelemente in Ihrem Algorithmus vorkommen.
# 
# Für die Erstellung des Flußdiagramms können Sie jedes Programm Ihrer Wahl verwenden. Wenn Ihnen kein Programm bekannt ist, dann empfehlen wir Ihnen die Verwendung von [draw.io](https://draw.io) (Flußdiagramme heißen dort Flowcharts).
# 
# Geben Sie ein PDF Dokument namens `Divisionsalgorithmus.pdf` mit den beiden Formen der Algorithmusbeschreibung und der Auflistung der Grundelemente ab. Kopieren Sie das PDF Dokument in den Ordner dieses Übungszettels, dann wird es automatisch mit dem Übungszettel abgegeben.

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 3")


# In[ ]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_2_3_solved = True


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_3_1(result, suite, case):
    varname = "exercise_2_3_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            result.setSucceeded("Exercise solved.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check files", deps=["1"])
def testcase_3_2(result, suite, case):
    result.setSucceeded()
    jagl.check_path_exists(result, files=["Divisionsalgorithmus.pdf"], message = "Did you upload all necessary files?")
    if result.isSucceeded():
        result.addMessage("All files were found.")


# In[ ]:





# In[ ]:





# In[ ]:





# # 2.4 Ausführungsmodelle (20 %)
# Geben Sie zu jedem der folgenden Szenarien an, welches Ausführungsmodell Sie dafür einsetzen würden. Begründen Sie Ihre Wahl in wenigen Sätzen.

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 4")


# In[ ]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_2_4_solved = True


# a.   Für Windows und für Linux soll ein Gerätetreiber für eine Webcam implementiert werden. Überlegen Sie sich noch zusätzlich, ob ein und derselbe Treiber für beide Betriebssysteme verwendet werden kann, oder ob für jedes Betriebssystem ein eigener Treiber implementiert werden muss (wenn ja, wieso).

# Ausführungsmodell: Betriebssystemabhängiger Kernel-Modus
# Begründung: Windows und Linux haben unterschiedliche Kernel-Architekturen und API-Schnittstellen, weshalb separate Treiber für jedes Betriebssystem implementiert werden müssen.

# b. Es soll eine Simulations-Software zur Wettervorhersage implementiert werden. Diese Software besitzt sehr hohe Ressourcen-Anforderungen und sollte daher möglichst effizient und parallelisiert ausgeführt werden.

# Ausführungsmodell: Parallelisiertes, verteiltes Modell
# Begründung: Wettervorhersagen sind sehr rechenintensiv ist und und es müssen sehr viele Daten verarbeitet werden.
# Mehrere Prozesse und Threads können auf verschiedenen Prozessoren und oder über Cluster hinweg verteilt laufen, um die Rechenlast effizient zu verteilen und die Leistung zu optimieren.

# c. Es soll ein Embedded System zur Steuerung eines Personenaufzugs implementiert werden. Dabei gilt zu beachten, dass die vorhandenen Ressourcen durch die Hardware stark limitiert sind.

# Ausführungsmodell: Echtzeitmodell (Real-Time Operating System, RTOS)
# Begründung: In einem Embedded System für einen Aufzug sind Ressourcen begrenzt, und das System muss in Echtzeit reagieren können, um sicherheitskritische Operationen auszuführen. Ein Echtzeitbetriebssystem (RTOS) ist erforderlich, um sicherzustellen, dass alle Vorgänge innerhalb fester Zeitrahmen ausgeführt werden, unabhängig von den begrenzten Ressourcen.

# d. Es soll eine E-Mail Anwendung implementiert werden, welche sowohl auf Windows, als auch auf Linux und macOS eingesetzt werden kann. Außerdem soll jeder Benutzer in der Lage sein, möglichst einfach die Anwendung eigenhändig auf seine Anforderungen anzupassen und neue Features zu implementieren.

# Ausführungsmodell: Plattformunabhängiges Modell (z. B. Web-basiert oder plattformübergreifendes Framework wie Electron)
# Begründung: Da die Anwendung auf mehreren Betriebssystemen laufen soll und leicht erweiterbar sein muss, ist ein plattformunabhängiges Modell sinnvoll. Frameworks wie Electron oder Web-basierte Technologien ermöglichen die Erstellung von Anwendungen, die auf Windows, Linux und macOS gleichermaßen laufen, und bieten Flexibilität bei der Anpassung durch die Benutzer.

# e. Angetrieben vom Erfolg der E-Mail Anwendung von oberhalb, beschließt eine weitere Organisation eine ähnliche Software zu entwickeln. Diese soll ebenfalls auf allen gängigen Betriebssystemen laufen, zudem jedoch diverse Features enthalten, welche die Einhaltung des Betriebsgeheimnisses erfordern. Infolgedessen ist es notwendig, dass [Reverse Engineering](https://de.wikipedia.org/wiki/Reverse_Engineering) möglichst erschwert wird.

# Ausführungsmodell: Plattformunabhängiges, aber stark verschlüsseltes Modell (z. B. Native Anwendungen mit Obfuskation und Verschlüsselung)
# Begründung: Um das Reverse Engineering zu erschweren, muss die Software auf allen Plattformen zwar verfügbar sein, aber zusätzliche Schutzmaßnahmen wie Code-Obfuskation und Verschlüsselung enthalten. Dabei kann man die Sicherheit zb. durch verschlüsselte Kommunikation und schwer nachvollziehbare Strukturen stärken.

# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_4_1(result, suite, case):
    varname = "exercise_2_4_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            result.setSucceeded("Exercise solved.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:





# In[ ]:




