#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "functions.c"
//#include <windows.h>


int main()
{
    Joueur A, B;
    int tourDeQui=1, menu, niveau, mode, party, game=0, coups=1, coups_max=1000, choice, dans_grenier;

    //Color(3,0);
    printf("\n*******************************************");
    printf("\n*************** MANCALA 2.0 ***************");
    printf("\n*******************************************");
    printf("\n\n");
    //Color(15,0);
    printf("Mancala est en fait une famille de jeux similaires, et pas juste un nom specifique de jeu.\nLa partie se joue sur le plateau de 6 x 2 (avec deux greniers de chaque cote) et chaque trou contient 4 graines au depart (Menu par defaut).\n");
    printf("\nLe but du jeu est d'obtenir plus de points que son adversaire en deplaçant des graines de son camp ou en capturant celles de l'adversaire.\n");
    
    mode = game_mode();
    printf("\n");

    if (mode == 2)
    {
        niveau = choixNiveau();
    }

    printf("\n");
    menu = choixMenu();

    printf("\n");
    party = partie();

    if (party == 2)
    {
        printf("\nEn combien de coups (par joueur) voulez-vous jouer? : ");
        scanf("%d", &coups_max);
    }

    printf("\n");

    if (mode == 1)
    {
        if(menu == 1)
        {
            init(&A, 1, 4);
            printf("Vous comptez de 1 a 6 de la gauche vers la droite.\n\n");

            init(&B, 2, 4);
            printf("Vous comptez de 1 a 6 de la droite vers la gauche.\n\n\n");
        }
        else if (menu == 2)
        {
            int nb =nombre_de_grains();
            init(&A, 1,nb);
            printf("Vous comptez de 1 a 6 de la gauche vers la droite.\n\n");

            init(&B, 2, nb);
            printf("Vous comptez de 1 a 6 de la droite vers la gauche.\n\n\n");
        }
    }
    else if (mode == 2)
    {
        if(menu == 1)
        {
            init_IA(&A, &B, 4);
            printf("Vous comptez de 1 a 6 de la droite vers la gauche.\n\n\n");
        }
        else if(menu==2)
        {
            init_IA(&A, &B, nombre_de_grains());
            printf("Vous comptez de 1 a 6 de la droite vers la gauche.\n\n\n");
        }

    }

    //Color(5,0);
    printf("       ********************       ");
    printf("\n*******    C'est parti!    *******\n");
    printf("       ********************       \n\n");
    
    //Color(15,0);
    affiche(&A,&B);

    printf("\n");

    while (game==0 && coups<=(2*coups_max))
    {
        if (tourDeQui == 1)
        {
            choice = choix(&A);
            dans_grenier = move(&A, &B, choice);
        }
        else
        {
            if (mode == 1)
            {
                choice = choix(&B);
            }
            else if (mode == 2)
            {
                printf("\n\n--- Tour de l'IA ---\n");
                attendre(4);
                
                if (niveau == 1)
                {
                    choice = nb_aleatoire_facile(&B);
                }
                else if (niveau == 2)
                {
                    choice = nb_aleatoire_difficile(&B);
                }
                printf("Je choisis la case %d\n", choice);
            }
            dans_grenier = move(&B, &A, choice);
        }

        printf("\n");

        attendre(1);
        affiche(&A, &B);

        game = arret(&A, &B);

        if (dans_grenier != 0 )
        {
            if (tourDeQui == 1)
            {
                tourDeQui = 2;
            }
            else
            {
                tourDeQui = 1;
            }
        }

        coups += 1;
    }

    //Color(2,0);
    printf("\n\n\n       *********************       ");
    printf("\n*******  Fin de la partie!  *******\n");
    printf("       *********************       \n\n");

    if (game==1 && tourDeQui == 1 )
    {
        int i=1;
        while(i<7)
        {
            A.score += A.tab[i];
            A.tab[i] = 0;
            i++;

        }
    }
    else if (game==1 && tourDeQui == 2)
    {
        int j=1;
        while(j<7)
        {
            B.score += B.tab[j];
            B.tab[j] = 0;
            j++;
        }
    }

    affiche(&A, &B);

    if(A.score>B.score)
    {
        printf("\nFélicitations %s, vous avez gagné", A.nom);
    }
    else if(A.score<B.score)
    {
         printf("\nFélicitations %s, vous avez gagné", B.nom);
    }
    else
    {
        printf("\nMatch nul !");
    }

    enregistrement(A, B);

    return EXIT_SUCCESS;
}
