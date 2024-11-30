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
# # Übungsblatt 5

# ---
# Abgabe bis <b>Sonntag, 24. November 2024, 23:55 Uhr</b>

# In[ ]:


import jagl
import os
import re
import types
import sys


# ---
# ### Achtung:
# 
# *Bitte verwenden Sie für dieses Übungsblatt nur Funktionen und Datenstrukturen, die im Rahmen dieser Lehrveranstaltung (Notebook-Sheets "Strukturierte Programmierung mit Python" und "Datentypen in Python") besprochen wurden, es sei denn es wird explizit anders angegeben.*

# ---
# ## 5.1 Suchen (14%)
# 
# Implementieren sie eine Funktion, welche ein Integer-Array und einen Integer als Parameter übergeben bekommt, dieses Array dann nach dem übergebenen Integer durchsucht und im Falle eines Erfolgs den Index des gesuchten Integers im Array zurückgibt. Falls der Integer nicht gefunden wird, so soll `None` zurückgegeben werden. Falls der gesuchte Integer mehr als einmal im Array zu finden ist, dann soll der Index des ersten Auftretens zurückgegeben werden.

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 1")


# In[ ]:


# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Das Array das untersucht werden soll, wird an die untenstehende Funktion als Variable "array" übergeben.
# Der Integer nach dem gesucht werden soll, wird an die untenstehende Funktion als Variable "x" übergeben.
# Die Funktion soll den Index der gesuchten Zahl zurückgeben, oder "None" falls diese nicht gefunden werden konnte.


def search_array(array, x):
    for i in range(len(array)):
        if array[i] == x:  
            return i 
    return None 


# In[ ]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_5_1_solved = True


# In[ ]:


# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.
# Damit Sie den Wert None in der Ausgabe sehen können, müssen Sie den Rückgabewert mit print() ausgeben.

print(search_array([1,2,3,3, 4,5 ,3 ], 3))


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_1_1(result, suite, case):
    varname = "exercise_5_1_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            result.setSucceeded("Exercise solved.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check Function search_array()", deps=["1"])
def testcase_1_2(result, suite, case):
    jagl.check_variable_exists_and_has_type(result, globals(), "search_array", types.FunctionType)
    if result.isSucceeded():
        def _search_array_(array, n):
            for i in range(len(array)):
                if array[i] == n:
                    return i
            return None
        for x in [[[1, 2, 3, 4, 3, 2, 4, 8, 9, 4], 4], [[123, 54, 1234, 878, 234], 2], [[23, 54, 42, 43], 43], [[10, 2, 3, 4], 10]]:
            res1 = search_array(*x)
            truth = _search_array_(*x)
            if not isinstance(res1, type(truth)):
                result.setFailed(f"Return value of search_array({x}) has the wrong type ({type(res1)} instead of {type(truth)})")
            elif res1 == truth:
                result.setSucceeded(f"search_array({x}) returns the correct value")
            else:
                result.setFailed(f"search_array({x}) returns the wrong value ({res1} instead of {truth})")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ---
# ## 5.2 Sortieren (14%)
# 
# Implementieren sie eine Funktion, welche ein unsortiertes Integer-Array als Parameter übergeben bekommt, dieses dann sortiert und wieder zurückgibt. Verwenden Sie dazu den Sortieralgorithmus ["**Selectionsort**"](https://de.wikipedia.org/wiki/Selectionsort). Wird `True` als zweiter Parameter an die Funktion übergeben, dann soll das Array aufsteigend sortiert werden, wird `False` übergeben, dann absteigend.
# 
# *Hinweis*: Selectionsort lässt sich am einfachsten implementieren, wenn Sie mit zwei getrennten Arrays S und U (gleiche Notation wie im verlinkten Wikipedia-Artikel) arbeiten. Dann brauchen Sie auch keine Vertausche-Funktion.

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 2")


# In[ ]:


# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Das Array das sortiert werden soll, wird an die untenstehende Funktion als Variable "array" übergeben.
# Besitzt der Parameter "asc" den Wahrheitswert "True", dann soll ein aufsteigend sortiertes Array zurückgegeben werden.
# Besitzt der Parameter "asc" den Wahrheitswert "False", dann soll ein absteigend sortiertes Array zurückgegeben werden.
# Die Funktion soll das sortierte Array zurückgeben.

def selection_sort(array, asc):

    if asc:
        for i in range(len(array)):
            min_index = i
            for j in range(i + 1, len(array)):
                if array[j] < array[min_index]:
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]
            
    else:
        for i in range(len(array)):
            max_index = i
            for j in range(i + 1, len(array)):
                if array[j] > array[max_index]:
                    max_index = j
            array[i], array[max_index] = array[max_index], array[i]
    
    return array


# In[ ]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_5_2_solved = True


# In[ ]:


# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.

selection_sort([2,4,6,5,3,1], True)


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_2_1(result, suite, case):
    varname = "exercise_5_2_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            result.setSucceeded("Exercise solved.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check Function selection_sort()", deps=["1"])
def testcase_2_2(result, suite, case):
    jagl.check_variable_exists_and_has_type(result, globals(), "selection_sort", types.FunctionType)
    if result.isSucceeded():
        def _selection_sort_(array, asc):
            array.sort(reverse=not asc)
            return array
        for x in [[[1, 2, 3, 4, 3, 2, 4, 8, 9, 4], True], [[123, 54, 1234, 878, 234], False], [[23, 54, 42, 43], True], [[10, 2, 3, 4], False]]:
            l1 = list(x[0])
            l2 = list(x[0])
            res1 = selection_sort(l1, x[1])
            truth = _selection_sort_(l2, x[1])
            if not isinstance(res1, type(truth)):
                result.setFailed(f"Return value of selection_sort({x}) has the wrong type ({type(res1)} instead of {type(truth)})")
            elif res1 == truth:
                result.setSucceeded(f"selection_sort({x}) returns the correct value")
            else:
                result.setFailed(f"selection_sort({x}) returns the wrong value ({res1} instead of {truth})")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ---
# ## 5.3 Summieren (14%)
# 
# Implementieren Sie eine Funktion, welche ein Array mit Elementen beliebiger Datentypen als Parameter übergeben bekommt. Iterieren Sie mit einer **While**-Schleife durch dieses Array, addieren Sie die Werte aller Elemente, die den Datentyp Integer besitzen, und geben Sie die Summe dieser Addition zurück. Falls kein Integer gefunden wurde, soll 0 zurückgegeben werden.
# 
# *Hinweis:* Normalerweise würde man in diesem Fall eine Mengenschleife verwenden, aber manche Programmiersprachen kennen keine Mengenschleife und wie man in so einem Fall vorgeht wollen wir hier üben.

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 3")


# In[ ]:


# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Das Array das untersucht werden soll, wird an die untenstehende Funktion als Variable "array" übergeben.
# Die Funktion soll die Summe aller Integer im untersuchten Array zurückgeben.


def sum_array(array):
    summe = 0
    index = 0
    while index < len(array):
        if isinstance(array[index], int) and not isinstance(array[index], bool):
            summe += array[index]
        index += 1
        
    return summe


# In[ ]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_5_3_solved = True


# In[ ]:


# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.

sum_array(["Hello", 2, "World", True, 3, 4.5])


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_3_1(result, suite, case):
    varname = "exercise_5_3_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            result.setSucceeded("Exercise solved.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check Function sum_array()", deps=["1"])
def testcase_2_2(result, suite, case):
    jagl.check_variable_exists_and_has_type(result, globals(), "sum_array", types.FunctionType)
    if result.isSucceeded():
        def _sum_array_(array):
            return sum([x for x in array if isinstance(x, int)])
        for x in [
                [1, 2, 3, 4, 3, 2, 4, 8, 9, 4], 
                [123, 54, 1234, "a", 878, 4.3, 234], 
                [23, "hallo", 54.34, 42, 43.32], 
                [10.3, "a", 2.4, "b", 3.4, "c", 4.3]
            ]:
            res1 = sum_array(x)
            truth = _sum_array_(x)
            if not isinstance(res1, type(truth)):
                result.setFailed(f"Return value of sum_array({x}) has the wrong type ({type(res1)} instead of {type(truth)})")
            elif res1 == truth:
                result.setSucceeded(f"sum_array({x}) returns the correct value")
            else:
                result.setFailed(f"sum_array({x}) returns the wrong value ({res1} instead of {truth})")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ---
# ## 5.4 Stack (14%)
# 
# Implementieren Sie einen Stack, welcher auf einem dynamischen Array operiert und Elemente mit beliebigen Datentypen beinhalten kann. Dieser Stack soll die Funktionen "push", "pop", "top", "is_empty" und "size" anbieten. Elemente sollen immer am Ende des Arrays hinzugefügt werden. Es ist erlaubt Elemente mit Hilfe der "[append](https://www.w3schools.com/python/ref_list_append.asp)"-Funktion zu diesem Array hinzuzufügen.

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 4")


# In[ ]:


# Schreiben Sie Ihren Code in die untenstehenden Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# "stack" ist ein Array und "element" ist ein Element, welches hinzugefügt werden soll.
# Es ist nicht nötig einen Rückgabewert zu definieren.
def push(stack, element):
    stack.append(element)
    


# In[ ]:


# Schreiben Sie Ihren Code in die untenstehenden Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# "stack" ist ein Array. Falls "stack" keine Elemente besitzt, dann soll "None" zurückgegeben werden.
# Ansonsten soll das letzte Element, das zu "stack" hinzugefügt worden ist, zurückgegeben und aus "stack" entfernt werden.
def pop(stack):
    if not stack:
        return None
    return stack.pop()
    


# In[ ]:


# Schreiben Sie Ihren Code in die untenstehenden Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# "stack" ist ein Array. Falls "stack" keine Elemente besitzt, dann soll "None" zurückgegeben werden.
# Ansonsten soll das letzte Element, das zu "stack" hinzugefügt worden ist, zurückgegeben werden.
def top(stack):
    if len(stack) == 0:
        return None
    # Otherwise, return the last element
    return stack[-1]


# In[ ]:


# Schreiben Sie Ihren Code in die untenstehenden Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# "stack" ist ein Array. Falls "stack" keine Elemente besitzt, dann soll "True" zurückgegeben werden, andernfalls "False".
def is_empty(stack):
    return len(stack) == 0
    


# In[ ]:


# Schreiben Sie Ihren Code in die untenstehenden Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# "stack" ist ein Array. Die Anzahl der Elemente von "stack" soll als Integer zurückgegeben werden.
def size(stack):
    return len(stack)
    


# In[ ]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_5_4_solved = True


# In[ ]:


# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zellen mit den entsprechenden Funktionen aus.

#Create an empty stack
stack = []

#Print the stack - expected output: []
print("Stack: " + str(stack))

#Pushing an element onto the stack
print("Pushing element: \"Hello\"");
push(stack, "Hello")

#Print the stack - expected output: ['Hello']
print("Stack: " + str(stack))

#Check if the stack is empty
print("Empty?: " + str(is_empty(stack)))

#Pushing an element onto the stack
print("Pushing element: 5");
push(stack, 5)

#Print the stack - expected output: ['Hello', 5]
print("Stack: " + str(stack))

#Check the size of the stack
print("Size: " + str(size(stack)))

#Retrieve the top element of the stack
print("Top: " + str(top(stack)))

#Print the stack - expected output: ['Hello', 5]
print("Stack: " + str(stack))

#Retrieve the top element of the stack and delete it
print("Pop: " + str(pop(stack)))

#Print the stack - expected output: ['Hello']
print("Stack: " + str(stack))

#Check the size of the stack
print("Size: " + str(size(stack)))

#Retrieve the top element of the stack and delete it
print("Pop: " + str(pop(stack)))

#Check if the stack is empty
print("Empty?: " + str(is_empty(stack)))

#Print the stack - expected output: []
print("Stack: " + str(stack))


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_4_1(result, suite, case):
    varname = "exercise_5_4_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            result.setSucceeded("Exercise solved.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check Stack Functions", deps=["1"])
def testcase_4_2(result, suite, case):
    jagl.check_variable_exists_and_has_type(result, globals(), "push", types.FunctionType)
    jagl.check_variable_exists_and_has_type(result, globals(), "pop", types.FunctionType)
    jagl.check_variable_exists_and_has_type(result, globals(), "top", types.FunctionType)
    jagl.check_variable_exists_and_has_type(result, globals(), "is_empty", types.FunctionType)
    jagl.check_variable_exists_and_has_type(result, globals(), "size", types.FunctionType)


# In[ ]:


@jagl.testcase("3", desc="Test Stack Functions", deps=["2"])
def testcase_4_3(result, suite, case):
    stack = []
    try:
        push(stack, "Hello")
        assert stack == ["Hello"]
        result.setSucceeded("\"push(stack, \"Hello\")\" seems to produce a correct result.")
    except:
        result.setFailed("\"push(stack, \"Hello\")\" produced a wrong result.")

    try:
        assert is_empty(stack) == False
        result.setSucceeded("\"is_empty(stack)\" seems to produce a correct result.")
    except:
        result.setFailed("\"is_empty(stack)\" produced a wrong result.")

    try:
        push(stack, 5)
        assert stack == ["Hello", 5]
        result.setSucceeded("\"push(stack, 5)\" seems to produce a correct result.")
    except:
        result.setFailed("\"push(stack, 5)\" produced a wrong result.")

    try:
        assert size(stack) == 2
        result.setSucceeded("\"size(stack)\" seems to produce a correct result.")
    except:
        result.setFailed("\"size(stack)\" produced a wrong result.")

    try:
        assert top(stack) == 5
        result.setSucceeded("\"top(stack)\" seems to produce a correct result.")
    except:
        result.setFailed("\"top(stack)\" produced a wrong result.")

    try:
        assert pop(stack) == 5
        result.setSucceeded("\"pop(stack)\" seems to produce a correct result.")
    except:
        result.setFailed("\"pop(stack)\" produced a wrong result.")

    try:
        assert size(stack) == 1
        result.setSucceeded("\"size(stack)\" seems to produce a correct result.")
    except:
        result.setFailed("\"size(stack)\" produced a wrong result.")

    try:
        assert pop(stack) == "Hello"
        result.setSucceeded("\"pop(stack)\" seems to produce a correct result.")
    except:
        result.setFailed("\"size(stack)\" produced a wrong result.")

    try:
        assert is_empty(stack) == True
        result.setSucceeded("\"is_empty(stack)\" seems to produce a correct result.")
    except:
        result.setFailed("\"is_empty(stack)\" produced a wrong result.")


# In[ ]:





# In[ ]:





# In[ ]:





# ---
# ## 5.5 Ziffernpotenzsumme (16%)
# 
# Die positive Ganzzahl $512$ ist interessant (in der Mathematik nennt man eine Zahl interessant, wenn sie besondere Eigenschaften erfüllt) weil sie gleich der [Ziffernsumme](https://de.wikipedia.org/wiki/Quersumme) potentiert mit einer natürlichen Zahl ist: $5 + 1 + 2 = 8$, und $8^3 = 512$.
# 
# Ein anderes Beispiel ist $614656$: $6 + 1 + 4 + 6 + 5 + 6 = 28$, und $28^4 = 614656$
# 
# Implementieren Sie ein Programm, welches alle interessanten Zahlen (d.h. alle Zahlen, welche die oben demonstrierten Eigenschaften besitzt) innerhalb eines angegebenen Zahlenbereichs findet.
# 
# ---
# 
# Beim Lösen solcher Aufgaben wendet man das **Teile-und-Herrsche** Prinzip an, d.h. man zerlegt ein komplexes Problem in mehrere leichter zu lösende Teilprobleme. Zur Erleichterung der Aufgabe haben wir das Zerlegen der Aufgabe in Teilprobleme für Sie schon vorgenommen:
# 
# 1. Implementieren Sie die Funktion `get_digits(n)`, welche eine positive Ganzzahl `n` in die einzelnen Ziffern zerlegt und diese als Liste zurückgibt. Zum Beispiel, der Aufruf von `get_digits(13442)` liefert die Liste `[1, 3, 4, 4, 2]`. Die Reihenfolge der einzelnen Ziffern in dieser Liste ist dabei egal.
# 
# 
# 2. Implementieren Sie die Funktion `digit_power_sum(digits, power)`, welche die Summe der Ziffern in der übergebenen Liste (1.Argument) berechnet und mit dem angegebenen Exponenten (2. Argument) potentiert (Zur Berechnung der Potenz können Sie in Python den Operator `**` verwenden). Das Ergebnis wird anschließend zurückgegeben. Zum Beispiel, der Aufruf von `digit_power_sum([2, 3, 1], 3)` liefert als Ergebnis `216`.
# 
# 
# 3. Implementieren Sie die Funktion `is_interesting_number(n)`, welche die Funktion `get_digits(n)` verwendet, um die Zahl `n` in ihre Ziffern zerlegt. Anschließend wird `digit_power_sum(digits, power)` mit unterschiedlichen Exponenten aufgerufen und überprüft, ob das Ergebnis gleich der Zahl `n` ist. Wenn die Zahl interessant ist, soll `True` zurückgegeben werden, ansonsten `False`. Zum Beispiel, der Aufruf von `is_interesting_number(512)` liefert als Ergebnis `True`.
# 
# 
# 4. Implementieren Sie die Funktion `get_interesting_numbers(l, u)`, welche für alle Zahlen im Interval von `l` bis `u` (beide Grenzen inklusive) überprüft, ob diese interessant sind. Alle gefundenen interessanten Zahlen sollen als Liste zurückgegeben werden. Zum Beispiel, der Aufruf von `get_interesting_number(400, 600)` liefert als Ergebnis `[512]`.
# 
# ---
# 
# Tipps:
# 
# Zu 1: 
# * Verwenden Sie die Operatoren `%` und `//`.
# 
# 
# Zu 3: 
# * Wenn die Ziffernsumme 1 ist, dann können Sie die dazugehörige Zahl ignorieren, da 1 potentiert mit irgendeinem Exponenten immer 1 ergibt. 
# 
# * Wenn die Ziffernpotenzsumme mit einem Exponenten e größer als die Zahl n ist, dann ist die Überprüfung aller Exponenten größer als e sinnlos, da deren Ziffernpotenzsumme immer größer als n sein wird.

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 5")


# In[ ]:


# Schreiben Sie Ihren Code in die untenstehenden Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# "n" ist eine positive Ganzzahl
def get_digits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return digits


# In[ ]:


# Schreiben Sie Ihren Code in die untenstehenden Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# "digits" ist eine Liste von positiven Ganzzahlen und "power" ist eine positive Ganzzahl


def digit_power_sum(digits, power):
    total = 0
    for digit in digits:
        total += digit ** power 
    return total  


# In[ ]:


# Schreiben Sie Ihren Code in die untenstehenden Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# "n" ist eine positive Ganzzahl

def is_interesting_number(n):
    if n == 0:  
        return False 
    
    digits = get_digits(n)
    digit_sum = sum(digits)  
    
    if digit_sum == 1: 
        return False

    power = 1
    while True:
  
        result = digit_power_sum([digit_sum], power)  
        if result == n: 
            return True
        if result > n:  
            return False
        power += 1 


# In[ ]:


# Schreiben Sie Ihren Code in die untenstehenden Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# "l" und "u" sind positive Ganzzahlen
def get_interesting_numbers(l, u):
    interesting_numbers = []
    for n in range(l, u + 1):  
        if is_interesting_number(n):  
            interesting_numbers.append(n)  
    return interesting_numbers


# In[ ]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_5_5_solved = True


# In[ ]:


# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zellen mit den entsprechenden Funktionen aus.

get_digits(13442)


# In[ ]:


# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zellen mit den entsprechenden Funktionen aus.

digit_power_sum([2, 3, 1], 3)


# In[ ]:


# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zellen mit den entsprechenden Funktionen aus.

is_interesting_number(513)


# In[ ]:


# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zellen mit den entsprechenden Funktionen aus.

get_interesting_numbers(19000, 1000000)


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_5_1(result, suite, case):
    varname = "exercise_5_5_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            result.setSucceeded("Exercise solved.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check Functions", deps=["1"])
def testcase_5_2(result, suite, case):
    jagl.check_variable_exists_and_has_type(result, globals(), "get_digits", types.FunctionType)
    jagl.check_variable_exists_and_has_type(result, globals(), "digit_power_sum", types.FunctionType)
    jagl.check_variable_exists_and_has_type(result, globals(), "is_interesting_number", types.FunctionType)
    jagl.check_variable_exists_and_has_type(result, globals(), "get_interesting_numbers", types.FunctionType)
    if result.isSucceeded():
        def _get_digits_(n):
            digits = []
            while n > 0:
                digits.append(n % 10)
                n = n // 10
            return digits
        def _digit_power_sum_(digits, power):
            result = 0
            for e in digits:
                result += e
            result = result ** power
            return result
        def _is_interesting_number_(n):
            digits = _get_digits_(n)
            i = 1
            tmp = _digit_power_sum_(digits, i)
            while tmp > 1 and tmp <= n:
                if tmp == n:
                    return True
                i += 1
                tmp = _digit_power_sum_(digits, i)
            return False
        def _get_interesting_numbers_(l, u):
            interesting_numbers = []
            for i in range(l, u+1):
                if _is_interesting_number_(i):
                    interesting_numbers.append(i)
            return interesting_numbers
        for x in [
                [400, 600], 
                [100, 1000], 
                [0, 100], 
                [10, 10000]
            ]:
            res1 = get_interesting_numbers(*x)
            truth = _get_interesting_numbers_(*x)
            if not isinstance(res1, type(truth)):
                result.setFailed(f"Return value of get_interesting_numbers({x}) has the wrong type ({type(res1)} instead of {type(truth)})")
            elif res1 == truth:
                result.setSucceeded(f"get_interesting_numbers({x}) returns the correct value")
            else:
                result.setFailed(f"get_interesting_numbers({x}) returns the wrong value ({res1} instead of {truth})")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ---
# ## 5.6 Fakultäten der Ziffern (16%)
# 
# 
# Die Zahl 145 ist eine Zahl mit einer interessanten Eigenschaft: $1! + 4! + 5! = 1 + 24 + 120 = 145$.
# 
# Finden Sie die **Summe aller Zahlen** (bis zu einer gegebenen Obergrenze `n`), bei denen die Summe der Fakultäten ihrer Ziffern die Zahl selber ergibt.
# 
# Hinweis :1!=1 und 2!=2 sind nicht damit gemeint, da hier keine Summe gebildet wird.
# 
# Diesmal müssen Sie das Teile-und-Herrsche Prinzip selber anwenden. Versuchen Sie dieses Problem in Teilprobleme aufzuteilen und diese getrennt voneinander zu implementieren, bevor Sie dann am Ende die Teillösungen zu einem gesamten Programm zusammenfügen.
# 
# Tipp: Sie können bestehene Teillösungen von diesem Übungszettel und den Jupyter Notebook Sheets auf Sakai wiederverwenden.
# 
# Bonusaufgabe: Wie kann man die Berechnung beschleunigen?

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 6")


# In[ ]:


# Schreiben Sie Ihren Code in die untenstehenden Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# "n" ist eine positive Ganzzahl
# Rückgabewert: Ganzzahl
# Schreiben Sie bitte auch alle zusätzlichen Funktionen in diese Zelle und fügen Sie keine neuen Zellen hinzu.


def digits_factorial(n):
    def factorial(x):
        if x == 0 or x == 1:
            return 1
        else:
            result = 1
            for i in range(1, x + 1):
                result *= i
            return result

    # Gesamtsumme initialisieren
    total_sum = 0

    for number in range(10, n + 1):
        digit_sum = 0
        for digit in str(number):
            digit_sum += factorial(int(digit))


        if digit_sum == number:
            total_sum += number

    return total_sum


# In[ ]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_5_6_solved = True


# In[ ]:


# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zellen mit den entsprechenden Funktionen aus.

digits_factorial(1000)


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_6_1(result, suite, case):
    varname = "exercise_5_6_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            result.setSucceeded("Exercise solved.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check Functions", deps=["1"])
def testcase_6_2(result, suite, case):
    try:
        jagl.check_variable_exists_and_has_type(result, globals(), "digits_factorial", types.FunctionType)
        if result.isSucceeded():
            def _fact_(n):
                fact = 1
                for i in range(1, n+1):
                    fact = fact * i
                return fact
            precalc = []
            for i in range(0, 10):
                precalc.append(_fact_(i))
            def _get_digits_(n):
                digits = []
                while n > 0:
                    digits.append(n % 10)
                    n = n // 10
                return digits
            def _digits_factorial_(n):
                sum = 0
                interesting_numbers = []
                for i in range(3, n):
                    dsum = 0
                    for d in _get_digits_(i):
                        dsum += precalc[d]
                    if dsum == i:
                        sum += i
                return sum
            for x in [
                    100, 1000, 100000
                ]:
                res1 = digits_factorial(x)
                truth = _digits_factorial_(x)
                if not isinstance(res1, type(truth)):
                    result.setFailed(f"Return value of digits_factorial({x}) has the wrong type ({type(res1)} instead of {type(truth)})")
                elif res1 == truth:
                    result.setSucceeded(f"digits_factorial({x}) returns the correct value")
                else:
                    result.setFailed(f"digits_factorial({x}) returns the wrong value ({res1} instead of {truth})")
    except:
        import traceback
        traceback.print_exc()


# In[ ]:





# In[ ]:





# In[ ]:





# ---
# ## 5.7 Genauigkeit von Gleitkommazahlen im Binärsystem (12%)
# 
# Geben Sie an welche der folgenden Zahlen ohne Verlust an Genauigkeit im IEEE 754 Format mit einfacher Genauigkeit im Binärsystem dargestellt werden können.
# <br/><br/>
# &nbsp; &nbsp; &nbsp;a.&nbsp; &nbsp; &nbsp; $0,1_{(10)}$<br/><br/>
# &nbsp; &nbsp; &nbsp;b.&nbsp; &nbsp; &nbsp; $0,5_{(10)}$<br/><br/>
# &nbsp; &nbsp; &nbsp;c.&nbsp; &nbsp; &nbsp; $0,625_{(10)}$<br/><br/>
# &nbsp; &nbsp; &nbsp;d.&nbsp; &nbsp; &nbsp; &nbsp;$(2^{24}+1)_{(10)}$<br/><br/>
# &nbsp; &nbsp; &nbsp;e.&nbsp; &nbsp; &nbsp; $(2^{24}+2)_{(10)}$<br/><br/>
# &nbsp; &nbsp; &nbsp;f.&nbsp; &nbsp; &nbsp; $0,0005_{(10)}$<br/><br/>
# &nbsp; &nbsp; &nbsp;g.&nbsp; &nbsp; &nbsp; $-0_{(10)}$<br/><br/>
# &nbsp; &nbsp; &nbsp;h.&nbsp; &nbsp; &nbsp; $(2^{142})_{(10)}$<br/><br/>
# &nbsp; &nbsp; &nbsp;i.&nbsp; &nbsp; &nbsp; $(666 * 2^{-6})_{(10)}$<br/><br/>
# &nbsp; &nbsp; &nbsp;j.&nbsp; &nbsp; &nbsp; $(\frac{1}{3})_{(10)}$<br/><br/>

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 6")


# In[ ]:


# Beantworten Sie die Frage, indem Sie die KORREKTEN Antworten in die unten stehende Liste einfügen. 
# Sind Ihrer Meinung nach die Antworten 'a', 'c' und 'e' korrekt, so sollte das Ergebnis so aussehen:
#
#         exercise_5_6_result = ["a", "c", "e"]

# Datentyp: list of strings
exercise_5_7_result = ["b", "c", "g", "j"]

# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_5_7_solved = True


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_6_1(result, suite, case):
    result.setSucceeded()
    varname = "exercise_5_7_solved"
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    jagl.check_variable_exists_and_has_type(result, globals(), "exercise_5_7_result", list)
    if result.isSucceeded():
        if eval(varname):
            result.setSucceeded("Exercise solved.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




