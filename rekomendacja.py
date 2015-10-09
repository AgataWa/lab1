# # #  Wzorowane na przykladzie Rona Zacharskiego
# #
# #
# # from math import sqrt
# #
# # users = {"Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
# #          "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
# #          "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
# #          "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
# #          "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
# #          "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
# #          "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
# #          "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
# #         }
# #
# #
# #
# # def manhattan(rating1, rating2):
# #     """Oblicz odleglosc w metryce taksowkowej miedzy dwoma  zbiorami ocen
# #        danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
# #        Zwroc -1, gdy zbiory nie maja wspolnych elementow"""
# #
# #     # TODO: wpisz kod
# #     pass
# #
# #
# # def computeNearestNeighbor(username, users):
# #     """dla danego uzytkownika, zwroc liste innych uzytkownikow wedlug bliskosci preferencji"""
# #     distances = []
# #     # TODO: wpisz kod
# #     return distances
# #
# # def recommend(username, users):
# #     """Zwroc liste rekomendacji dla uzytkownika"""
# #     # znajdz preferencje najblizszego sasiada
# #     nearest = computeNearestNeighbor(username, users)[0][1]
# #
# #     recommendations = []
# #     # zarekomenduj uzytkownikowi wykonawce, ktorego jeszcze nie ocenil, a zrobil to jego najblizszy sasiada
# #     # TODO: wpisz kod
# #     # using the fn sorted for variety - sort is more efficient
# #     return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)
# #
# # # przyklady
# #
# # print( recommend('Hela', users))
# # #print( recommend('Celina', users))
# print "Nazywam sie Agata Walicka \nlogin github: AgataWa \ntemat pracy magisterskiej: Modelowanie sygnalu full-waveform w lotniczym skaningu laserowym"
# print "Program oblicza roznice miedzy preferencjami poszczegolnych osob, dla kazdego uzytkownika uklada liste osob o najblizszych mu preferencjach\ni zwraca liste rekomendacji nieocenionych przez osobe zespolow polegajac na preferencjach osob o najbardziej zblizonych upodobaniach."
print("Nazywam sie Agata Walicka \nlogin github: AgataWa \ntemat pracy magisterskiej: Modelowanie sygnalu full-waveform w lotniczym skaningu laserowym")
print("Program oblicza roznice miedzy preferencjami poszczegolnych osob, dla kazdego uzytkownika uklada liste osob o najblizszych mu preferencjach\ni zwraca liste rekomendacji nieocenionych przez osobe zespolow polegajac na preferencjach osob o najbardziej zblizonych upodobaniach.")