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

# In[1]:


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
# # Übungsblatt 3

# ---
# Abgabe bis <b>Sonntag, 27. Oktober 2024, 23:55 Uhr</b>

# In[ ]:


import jagl
import os
import re
import types


# ---
# ## 3.1 Bestimmung von ungeraden Zahlen (14%)
# 
# Implementieren Sie eine Funktion, welche für jede beliebige Integer-Zahl bestimmen kann, ob diese ungerade ist. Falls eine Zahl ungerade ist, soll der Wahrheitswert "True" zurückgegeben werden. Falls es sich um eine gerade Zahl handelt, dann "False".

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 1")


# In[1]:


# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Die Zahl die untersucht werden soll wird an die untenstehende Funktion als Variable "x" übergeben.
# Die Variable "result" soll die Lösung als booleschen Wert enthalten.

def is_odd(x):
    result = None
    
    #if x % 2 == 0:
    #    result = False
    #else:
    #    result = True
        
    return False if x%2 == 0 else True


# In[4]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_3_1_solved = True

# DEINE ANTWORT HIER


# In[5]:


# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.

is_odd(13)


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_1_1(result, suite, case):
    varname = "exercise_3_1_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            result.setSucceeded("Exercise solved.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check Function is_odd()", deps=["1"])
def testcase_1_2(result, suite, case):
    jagl.check_variable_exists_and_has_type(result, globals(), "is_odd", types.FunctionType)
    if result.isSucceeded():
        def _is_odd_(x):
            return x % 2 != 0
        for x in [13, 44, 1, 0, -1, -15, -10]:
            res1 = is_odd(x)
            truth = _is_odd_(x)
            if not isinstance(res1, bool):
                result.setFailed(f"Return value of is_odd({x}) has the wrong type ({type(res1)} instead of {bool})")
            elif res1 == truth:
                result.setSucceeded(f"is_odd({x}) returns the correct value")
            else:
                result.setFailed(f"is_odd({x}) returns the wrong value ({res1} instead of {truth})")


# In[ ]:





# In[ ]:





# In[ ]:





# ---
# ## 3.2 Summenberechnung (14%)
# 
# Implementieren Sie eine Funktion, welche bei der Zahl 3 startet und jede fünfte Zahl, die noch kleiner als die übergeben Zahl `x` ist, zu der bisherigen Summe (d.h. 3 + 8 + 13 + 18 + ...) hinzuaddiert. Am Ende soll die Summe dieser Berechnung zurückgegeben werden.
# 

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 2")


# In[2]:


# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Die Variable "sum" soll die Lösung als Integer enthalten.

def my_sum(x):
    
    # DEINE ANTWORT HIER
    sum = 0
    num = 3
    
    while (num < x and x >=3):
        sum += num
        num += 5
    
    return sum


# In[1]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_3_2_solved = True

# DEINE ANTWORT HIER


# In[ ]:


# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.

my_sum(132)


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_2_1(result, suite, case):
    varname = "exercise_3_2_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            result.setSucceeded("Exercise solved.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check Function my_sum()", deps=["1"])
def testcase_1_2(result, suite, case):
    jagl.check_variable_exists_and_has_type(result, globals(), "is_odd", types.FunctionType)
    if result.isSucceeded():
        def _my_sum_(x):
            return sum([x for x in range(3, x, 5)])
        for x in [-10, 0, 1, 2, 3, 4, 5, 13, 203, 1024, 10320]:
            res1 = my_sum(x)
            truth = _my_sum_(x)
            if not isinstance(res1, type(truth)):
                result.setFailed(f"Return value of my_sum({x}) has the wrong type ({type(res1)} instead of {type(truth)})")
            elif res1 == truth:
                result.setSucceeded(f"my_sum({x}) returns the correct value")
            else:
                result.setFailed(f"my_sum({x}) returns the wrong value ({res1} instead of {truth})")


# In[ ]:





# In[ ]:





# In[ ]:





# ---
# ## 3.3 Zahlenvergleich (14%)
# 
# Implementieren Sie eine Funktion, welche das Maximum und das Minimum von 6 Integer-Zahlen ermittelt und zurückgibt. Verwenden Sie dafür möglichst wenige Vergleiche zwischen den einzelnen Zahlen.
# 
# Die von Python bereitgestellten Funktionen *min()* und *max()* dürfen nicht verwendet werden.

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 3")


# In[ ]:


# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Die Zahlen die sortiert werden sollen, werden an die untenstehende Funktion 
# als Variablen "a", "b", "c", "d", "e" und "f" übergeben.
# Die Variablen "_min_" und "_max_" sollen die Lösungen als Integer enthalten.

def get_min_max(a, b, c, d, e, f):
    _max_ = None
    _min_ = None
    
    
    # DEINE ANTWORT HIER
    list = (b,c ,d ,e ,f)
    _max_ = a
    _min_ = a
    
    
def get_min_max(a, b, c, d, e, f):
    _max_ = None
    _min_ = None
    
    # DEINE ANTWORT HIER
    list = [a, b,c ,d ,e ,f]
    
    list.sort()
            
    _min_ = list[0]
    _max_ = list[-1]
    
    return _min_, _max_


# In[ ]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_3_3_solved = True

# DEINE ANTWORT HIER


# In[ ]:


# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.

get_min_max(21, 23, 13, 44, 5, 26)


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_3_1(result, suite, case):
    varname = "exercise_3_3_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            result.setSucceeded("Exercise solved.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check Function get_min_max()", deps=["1"])
def testcase_3_2(result, suite, case):
    jagl.check_variable_exists_and_has_type(result, globals(), "get_min_max", types.FunctionType)
    if result.isSucceeded():
        def _get_min_max_(a, b, c, d, e, f):
            return min(a, b, c, d, e, f), max(a, b, c, d, e, f)
        for x in [
                [1,2,3,4,5,6],
                [-2, -4, -99, 0, 12, 88],
                [-8, -8, 0, 0, 8, 8],
            ]:
            res1 = get_min_max(*x)
            truth = _get_min_max_(*x)
            if not isinstance(res1, type(truth)):
                result.setFailed(f"Return value of get_min_max({x}) has the wrong type ({type(res1)} instead of {type(truth)})")
            elif res1 == truth:
                result.setSucceeded(f"get_min_max({x}) returns the correct value")
            else:
                result.setFailed(f"get_min_max({x}) returns the wrong value ({res1} instead of {truth})")


# In[ ]:


@jagl.testcase("3", desc="Check Usage of min() and max()", deps=["2"])
def testcase_3_3(result, suite, case):
    global max, min
    oldmax = max
    oldmin = min
    def _myminmax_(*args, **kwargs):
        raise Exception("Detected usage of forbidden function min() or max()")
    try:
        max = _myminmax_
        min = _myminmax_
        get_min_max(1, 2, 3, 4, 5, 6)
        result.setSucceeded("min()/max() were not used.")
    except Exception as e:
        result.setFailed(f"{e}")
    max = oldmax
    min = oldmin
    


# In[ ]:





# In[ ]:





# In[ ]:





# ---
# ## 3.4 Teilen von Ganzzahlen (14%)
# 
# Implementieren Sie eine Funktion, welche für eine beliebige positive Integer-Zahl ermittelt, wie oft diese ohne Entstehung eines Restbetrages durch 2 geteilt werden kann (nur gerade Zahlen können ohne Restbetrag geteilt werden) und das Ergebnis anschließend zurückgibt. Verwenden Sie dazu die in Aufgabe 3.1 implementierte Funktion "is_odd".
# 

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 4")


# In[2]:


# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Die Zahl die untersucht werden soll wird an die untenstehende Funktion als Variable "x" übergeben.
# Die Variable "count" soll Ihre Lösung als Integer enthalten.
# Bitte achten Sie darauf die in Aufgabe 4.1 implementierte Funktion is_odd zu verwenden.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der Funktion is_odd aus.

def count_loop(x):
    count = 0
    while is_odd(x) == False:
        x = x/2
        count += 1
    return count


# In[ ]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_3_4_solved = True

# DEINE ANTWORT HIER


# In[ ]:


# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.

count_loop(48)


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_4_1(result, suite, case):
    varname = "exercise_3_4_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            result.setSucceeded("Exercise solved.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check Function count_loop()", deps=["1"])
def testcase_4_2(result, suite, case):
    jagl.check_variable_exists_and_has_type(result, globals(), "count_loop", types.FunctionType)
    if result.isSucceeded():
        def _count_loop_(x):
            count = 0;
            while x % 2 == 0:
                count += 1
                x = x/2
            return count
        for x in [1, 32, 12, 11, -12, -60, -33]:
            res1 = count_loop(x)
            truth = _count_loop_(x)
            if not isinstance(res1, type(truth)):
                result.setFailed(f"Return value of count_loop({x}) has the wrong type ({type(res1)} instead of {type(truth)})")
            elif res1 == truth:
                result.setSucceeded(f"count_loop({x}) returns the correct value")
            else:
                result.setFailed(f"count_loop({x}) returns the wrong value ({res1} instead of {truth})")


# In[ ]:


@jagl.testcase("3", desc="Check Usage of is_odd()", deps=["2"])
def testcase_4_3(result, suite, case):
    global is_odd
    old_is_odd = is_odd
    class MyException(Exception):
        pass
    def my_is_odd(*args, **kwargs):
        raise MyException("Detected usage of is_odd()")
    try:
        is_odd = my_is_odd
        is_odd(11)
        result.setFailed("is_odd() was not used.")
    except MyException as e:
        result.setSucceeded(f"{e}")
    except Exception as e:
        result.setFailed(f"Unknown exception: {e}")
    is_odd = old_is_odd
    


# In[ ]:





# In[ ]:





# In[ ]:





# ---
# ## 3.5 Division mit Rest (14%)
# 
# Implementieren Sie eine Funktion, welche die Division mit Rest für den Dividenten `x` und den Divisor `y` berechnet und zurückgibt. 
# 
# Der Divisions-Operator `/` bzw. `//` und der Modulo-Operator `%` dürfen nicht verwendet werden.

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 5")


# In[1]:


# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Der Divident und der Divisor werden an die untenstehende Funktion als Variablen "x" und "y" übergeben.
# Die Variable "result" soll das Ergebnis der Division und die Variable "remainder" den Rest der Division enthalten.

def division_mit_rest(x, y):
    result = 0
    remainder = 0
    
    # DEINE ANTWORT HIER
    remainder = x

    while remainder >= y:
        remainder -= y
        result +=1
    
    return result, remainder


# In[2]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_3_5_solved = True

# DEINE ANTWORT HIER


# In[ ]:


# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.

division_mit_rest(7, 2)


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_5_1(result, suite, case):
    varname = "exercise_3_5_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            result.setSucceeded("Exercise solved.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check Function division_mit_rest()", deps=["1"])
def testcase_5_2(result, suite, case):
    jagl.check_variable_exists_and_has_type(result, globals(), "division_mit_rest", types.FunctionType)
    if result.isSucceeded():
        def _division_mit_rest_(x, y):
            return x // y, x % y
        for x in [[1, 1], [1, 2], [4, 2], [8, 4], [5, 3], [13, 3]]:
            res1 = division_mit_rest(*x)
            truth = _division_mit_rest_(*x)
            if not isinstance(res1, type(truth)):
                result.setFailed(f"Return value of division_mit_rest({x}) has the wrong type ({type(res1)} instead of {type(truth)})")
            elif res1 == truth:
                result.setSucceeded(f"division_mit_rest({x}) returns the correct value")
            else:
                result.setFailed(f"division_mit_rest({x}) returns the wrong value ({res1} instead of {truth})")


# In[ ]:





# In[ ]:





# ---
# ## 3.6 Bestimmung von Primzahlen (15%)
# 
# Implementieren Sie eine Funktion, welche für die übergebene Zahl `x` bestimmt, ob diese Zahl eine Primzahl ist. Wenn es sich um eine Primzahl handelt, dann soll `True` zurückgegeben werden, ansonsten `False`.
# 
# Mathematisch gesehen ist eine Primzahl eine natürliche Zahl, die größer als 1 und ausschließlich durch sich selbst und durch 1 teilbar ist.
# 
# Zur Überprüfung Ihrer Lösung finden Sie z.B. [auf Wikipedia](https://de.wikipedia.org/wiki/Primzahl) eine Liste von Primzahlen zum Testen.

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 6")


# In[5]:


# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Die zu überprüfende Zahl wird an die untenstehende Funktion als Variable "x" übergeben.
# Der Rückgabewert soll entweder True oder False sein

def is_prime(x):
    # DEINE ANTWORT HIER

    if x <= 1:
        return False

    for i in range (2, x-1):
        if x % i == 0:
            return False

    return True
            
    


# In[3]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_3_6_solved = True

# DEINE ANTWORT HIER


# In[4]:


# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.

is_prime(-5)


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_6_1(result, suite, case):
    varname = "exercise_3_6_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            result.setSucceeded("Exercise solved.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check Function is_prime()", deps=["1"])
def testcase_6_2(result, suite, case):
    jagl.check_variable_exists_and_has_type(result, globals(), "is_prime", types.FunctionType)
    if result.isSucceeded():
        def _is_prime_(x):
            if x >= -1 and x <= 1:
                return False
            for i in range(2, x):
                if x % i == 0:
                    return False
            return True
        for x in [0, 1, 2, 3, 4, 5, 6, 10, 13, 16, 22, 199, 301, 400]:
            res1 = is_prime(x)
            truth = _is_prime_(x)
            if not isinstance(res1, type(truth)):
                result.setFailed(f"Return value of is_prime({x}) has the wrong type ({type(res1)} instead of {type(truth)})")
            elif res1 == truth:
                result.setSucceeded(f"is_prime({x}) returns the correct value")
            else:
                result.setFailed(f"is_prime({x}) returns the wrong value ({res1} instead of {truth})")


# In[ ]:





# In[ ]:





# ---
# ## 3.7 Bestimmung von Dreieckszahlen (15%)
# 
# Implementieren Sie eine Funktion, welche für die übergebene Zahl `x` bestimmt, ob diese Zahl eine Dreieckszahl ist. Wenn es sich um eine Dreieckszahl handelt, dann soll `True` zurückgegeben werden, ansonsten `False`.
# 
# Eine [Dreieckszahl](https://de.wikipedia.org/wiki/Dreieckszahl) ist eine Zahl, die der Summe aller Zahlen von 1 bis zu einer Obergrenze `n` entspricht. Die 10 ist beispielsweise eine Dreieckszahl, da $1+2+3+4 = 10$, die 28 ist auch eine Dreieckszahl, da $1+2+3+4+5+6+7 = 28$.
# 

# In[ ]:


# new test suite
jagl.testsuite_begin("Exercise 6")


# In[ ]:


# Schreiben Sie Ihren Code in die untenstehende Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# Die zu überprüfende Zahl wird an die untenstehende Funktion als Variable "x" übergeben.
# Der Rückgabewert soll entweder True oder False sein


def is_triangular(x):
    # DEINE ANTWORT HIER
    summe = 0

    for i in range (x+1):
        print(i)
        summe += i
        if summe == x:
            return True
        elif summe > x:
            break

    return False
    


# In[ ]:


# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!

# Datentyp: bool
exercise_3_7_solved = True

# DEINE ANTWORT HIER


# In[ ]:


# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zelle mit der entsprechenden Funktion aus.

is_triangular(28)


# In[ ]:


@jagl.testcase("1", desc="Exercise Solved")
def testcase_7_1(result, suite, case):
    varname = "exercise_3_7_solved"
    result.setSucceeded()
    jagl.check_variable_exists_and_has_type(result, globals(), varname, bool)
    if result.isSucceeded():
        if eval(varname):
            result.setSucceeded("Exercise solved.")
        else:
            result.setFailed("Exercise not solved.")


# In[ ]:


@jagl.testcase("2", desc="Check Function is_triangular()", deps=["1"])
def testcase_7_2(result, suite, case):
    jagl.check_variable_exists_and_has_type(result, globals(), "is_triangular", types.FunctionType)
    if result.isSucceeded():
        def _is_triangular_(x):
            sum = 0
            i = 1
            while sum < x:
                sum += i
                i += 1
            return sum == x
        for x in [0, 1, 2, 3, 10, 13, 16, 22, 28, 199, 201, 400]:
            res1 = is_triangular(x)
            truth = _is_triangular_(x)
            if not isinstance(res1, type(truth)):
                result.setFailed(f"Return value of is_triangular({x}) has the wrong type ({type(res1)} instead of {type(truth)})")
            elif res1 == truth:
                result.setSucceeded(f"is_triangular({x}) returns the correct value")
            else:
                result.setFailed(f"is_triangular({x}) returns the wrong value ({res1} instead of {truth})")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




