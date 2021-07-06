# Node


Node Klasse. Bildet die Funktionalitaet von Knotenpunkten im Rahmen des Running Thief Problems ab. 

## Methods


### __init__


Erzeugt eine neue Knotenpunktinstanz unter Angabe von Name, Wert, Gewicht und Koordinaten. :param name: Name des Knotenpunkts :param value: Wert der Beute :param weight: Gewicht der Beute :param coordinates: Koorinaten des Knotenpunktes. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
name |  | 
value |  | 
weight |  | 
coordinates |  | 





### setValue


Setzt den Wert der an dem Knotenpunkt befindlichen Beute. :param value: Neuer Wert der Beute :return: 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
value |  | 





### getValue


Gibt den Wert der an dem Knotenpunkt befindlichen Beute zurueck. :return: Aktueller Wert der Beute 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### setWeight


Setzte das Gewicht der an dem Knotenpunkt befinflichen Beute. :param weight: neues Gewicht. :return: 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
weight |  | 





### getWeight


Gibt den Wert der an dem Knotenpunkt befindlichen Beute zurueck. :return: Aktuelles Gewicht der Beute 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### setNeighbour


Fuegt zum Knotenpunkt einen Nachbarknoten hinzu und berechnet die Distanz zwischen beiden Punkten. :param node: Node-Objekt, dass als Nachbar gesetzt werden soll. :return: 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
node |  | 





### getDistanceTo


Gibt die Distanz zu einem beliebigen Nachbarknoten zurueck. :param node: Node-Objekt, zu dem die Distanz bestimmt werden soll. :return: Distanz zu uebergebenem Node-Objekt. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
node |  | 





### set_distance_to




#### Parameters
name | description | default
--- | --- | ---
self |  | 
node |  | 
distance |  | 





### getNeighbours


Gibt die bestehenden Nachbarknoten zurueck. :return: dictionary der existierenden Nachbarknoten 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### getNeighbour


Gibt einen Nachbarknoten unter Angabe des Namens zurueck. :param name: Name des Node-Objekts :return: Node mit entsprechendem Namen 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
name |  | 





### getCoordinates


Gibt die Koordinaten des Knotenpunktes zurueck. :return: List mit Koordinaten. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 




