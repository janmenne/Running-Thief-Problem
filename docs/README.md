# Python Documentation

## Classes

**[FileManager](FileManager.md)**: Einlesen der gegebene Datein aus src/data 

**[Node](Node.md)**: Node Klasse. Bildet die Funktionalitaet von Knotenpunkten im Rahmen des Running Thief Problems ab. 

**[Graph](Graph.md)**: Graph welcher unser Problem darstellt, abspeichert und verarbeitet 


## Functions

### calculate_distance


Berechnet die Distanz aus den Koordinaten zweier Knotenpunkte :param v1: Liste der Koordinaten von Knotenpunkt-1 :param v2: Liste der Koordinaten von Knotenpunkt-2 :return: Distanz zwischen uebergebenen Koordinaten 
#### Parameters
name | description | default
--- | --- | ---
v1 |  | 
v2 |  | 





### calculateWDG


Berechnet den WDG-Wert als gewichtetes Entscheidungskriterium. :param wert: Wert der Beute :param distance: kuerzeste Distanz zum Endknoten (Distanz zum naechsten Knoten + Dijkstra) :param gewicht: Gewicht der Beute :return: gewichteter Wert 
#### Parameters
name | description | default
--- | --- | ---
wert |  | 
distance |  | 
gewicht |  | 





### dijkstra


Interne Implementation des Dijkstra-Algorithmus zur weiteren Verwendung in 'shortest_path' :param graph: gefuellte Instanz eines Graph-Objekts :param initial: Initialer Wert standartmaeßig 0. :return: besuchte Knoten, Pfad 
#### Parameters
name | description | default
--- | --- | ---
graph |  | 
initial |  | 





### shortest_path


Berechnet den kuerzesten Pfad von einem Start- zu einem Endknoten. :param graph: gefuellte Instanz eines Graph-Objekts :param origin: Startknoten :param destination: Zielknoten :return: Liste aus besuchten Knoten bzw. vollstaendigem, kuerzesten Pfad. 
#### Parameters
name | description | default
--- | --- | ---
graph |  | 
origin |  | 
destination |  | 





### best_path


Berechnet den besten Pfad von einem gegebenen Startpunkt zu einem Endpunkt. :param e: Endknoten :param a: Anfangsknoten :param filename: Name der .txt Vorlage. :return: Liste mit Reihenfolge der besuchten Knoten + Beute (True/False) 
#### Parameters
name | description | default
--- | --- | ---
filename |  | 
a |  | 
e |  | 





### getPerfectRoute


Nimmt die Route und packt den Rucksack solange voll, bis das maximal Gewicht erreicht ist. Der ALgorithmus sortiert nach Wert/Gewicht Verhältnis, heisst: Der Knoten mit dem besten W/G, wird zuerst in den Rucksack gepackt bzw. mitgenommen. :param route: Unsere errechnete Route vom Start-/ zum Endknoten :param max_capacity: Das maximal Gewicht unseres Rucksacks :return: Die neue errechnete Route mit der jeweiligen Anweisung 'mitnehmen'=ja/nein 
#### Parameters
name | description | default
--- | --- | ---
route |  | 
max_capacity |  | 
start |  | 
end |  | 





### sortV_W


Sortierung nach dem Wert/Gewicht Verhaehltnis :param element: Wert und Gewicht :return: W/G 
#### Parameters
name | description | default
--- | --- | ---
element |  | 





### sortNode


Sortierung nach dem Knoten :param element: Knoten :return: Knoten 
#### Parameters
name | description | default
--- | --- | ---
element |  | 





### getRoute


Erstelle Beste Route aus gegebenem Graphen/Knoten vom Starknoten zum Endknoten nach dem Kriterium Wert/Distanz/Gewicht :param graph: Graph fuer Dijkstra (shortest_path) :param node: Unser aktueller Knoten :param route: Unsere bisherig aufgebaute Route :param last_element: Das letzte ELement des Graphen :param visited: Bereits besuchte Elemente :return: aufgebaute beste Route nach Wert/Distanz/Gewicht von allen Knoten 
#### Parameters
name | description | default
--- | --- | ---
graph |  | 
node |  | 
route |  | 
last_element |  | 
visited |  | 




