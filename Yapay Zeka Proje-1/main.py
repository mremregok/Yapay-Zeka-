import bfs
import dfs
import ucs

print("PacMan oyununa hoşgeldiniz...\n")

print("Breadth First Search: 1 \nDepth First Search: 2 \nUniform Cost Search: 3")

controller = int(input("Seçiminiz:"))

if controller == 1:
    print("\nBaşlangıç için seçebileceğiniz düğüm listesi:\n['1,1','1,2','1,3','1,4','2,1','2,4','2,6','2,7','3,2','3,4','3,7','4,2','4,4','4,5','4,6','4,7','5,2','5,3','5,4','5,6','5,8','6,1','6,2','6,6','6,7','6,8','7,1','7,4','7,6','8,1','8,3','8,4','8,5','8,6','8,7','8,8']")

    x = input("\nBaşlangıç düğümünü seçiniz:")

    y = input("\nBitiş düğümünü seçiniz:")

    while x == y:
        print("Düğümler birbirinden farklı seçilmeli!")
        x = input("\nBaşlangıç düğümünü seçiniz:")

        y = input("\nBitiş düğümünü seçiniz:")
    
    bfs.PacFinder(x,y)

elif controller == 2:
    print("\nBaşlangıç için seçebileceğiniz düğüm listesi:\n['1,1','1,2','1,3','1,4','2,1','2,4','2,6','2,7','3,2','3,4','3,7','4,2','4,4','4,5','4,6','4,7','5,2','5,3','5,4','5,6','5,8','6,1','6,2','6,6','6,7','6,8','7,1','7,4','7,6','8,1','8,3','8,4','8,5','8,6','8,7','8,8']")

    x = input("\nBaşlangıç düğümünü seçiniz:")

    y = input("\nBitiş düğümünü seçiniz:")

    while x == y:
        print("Düğümler birbirinden farklı seçilmeli!")
        x = input("\nBaşlangıç düğümünü seçiniz:")

        y = input("\nBitiş düğümünü seçiniz:")
    
    dfs.PacFinder(x,y)
elif controller == 3:
    print("\nBaşlangıç için seçebileceğiniz düğüm listesi:\n['1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '2.8', '3.8', '4.8', '4.7', '5.8', '6.8', '6.7', '6.6', '6.5', '5.5', '4.5', '3.5', '2.5', '3.4', '3.3', '3.2', '3.1', '2.1', '4.1', '5.1', '6.1', '6.2', '6.3', '5.3', '4.3', '6.4', '7.1', '8.1', '8.2', '8.3', '8.4', '8.5', '8.6', '8.7', '8.8', '7.8', '3.6']")

    x = input("\nBaşlangıç düğümünü seçiniz:")

    y = input("\nBitiş düğümünü seçiniz:")

    while x == y:
        print("Düğümler birbirinden farklı seçilmeli!")
        x = input("\nBaşlangıç düğümünü seçiniz:")

        y = input("\nBitiş düğümünü seçiniz:")

    ucs.PacFinder(x,y)
else:
    print("\nHatalı tuşlama")
