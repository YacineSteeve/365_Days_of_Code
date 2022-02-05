#include <stdio.h>
#include <stdlib.h>

/*

The game description on https://en.wikipedia.org/wiki/Mancala .

*/


typedef struct Joueur Joueur;
struct Joueur
{
    char nom[60];
    int score;
    int tab[6];
};


void init(Joueur *A, int n)
{
    printf("Nom du joueur %d : ", n);
    scanf("%60s", A->nom);
    A->score = 0;
    int i=0;
    while(i<7)
    {
        A->tab[i]=4;
        i++;
    }
}


void affiche(Joueur *A, Joueur *B)
{
    printf("|%2d",A->score);
    int i=1;
    while(i<=6)
    {
        printf("| %2d",A->tab[i]);
        i++;
    }
    printf("|  |  %s\n|  ",  A->nom);

    int j=6;
    while(j>0)
    {
        printf("| %2d",B->tab[j]);
        j--;
    }
    printf ("|%2d|  %s",B->score, B->nom);
}


int choix(Joueur *A)
{
    int c;
    
    printf("\n\n--Tour de %s--\n", A->nom);
    
    do
    {
        printf("Quel est votre choix (entre 1 et 6): ");
        scanf("%d", &c);

        if(c<=0 || c>6)
        {
            printf("Numéro de case invalide!\n");
        }
        else if(A->tab[c]==0)
        {
            printf("Case vide! Choisissez-en une autre.\n");
        }
    } while (c<=0 || c>6 || A->tab[c]==0);
    
    return c;
}


int full_zero(Joueur *A)
{
    int n=0, i=0;

    while (i<7)
    {
        if (A->tab[i] == 0)
        {
            n++;
        }       
        i++;
    }
    
    if (n == 6)
    {
        return 1; // True
    }
    else
    {
        return 0; //False
    }
}


int arret(Joueur *A, Joueur *B)
{
    if ((full_zero(A)==1) || (full_zero(B)==1))
    {
        return 1; // au moins l'un des deux est en full zeros.
    }
    else
    {
        return 0; // aucun des deux n'est en full zeros.
    }
}


int move(Joueur *j1, Joueur *j2, int c)
{

    int Main, cote; // cote=1 pour j1, 2 pour j2 et 0 pour le grenier
    
    Main = j1->tab[c];
    j1->tab[c] = 0;

    while (Main > 0)
    {
        cote = 1;
        c--;

        while (c>=1 && Main>0)
        {
            j1->tab[c]++;
            Main--;
            c--;
        }

        c++;
        
        if (Main > 0)
        {
            cote = 0;

            j1->score++;
            Main--;
        }

        if (Main > 0)
        {
            cote = 2;

            int j=6;
            while (j>=1 && Main >0)
            {
                j2->tab[j]++;
                Main--;
                j--;
            }
        }

        if (Main > 0)
        {
            cote = 0;
            j2->score++;
            Main--;
            
            c = 7;
        }

    }

    // c contient l'indice de la dernière case visitée (côté joueur) 
    // 7-c sera donc l'indice de la case adverse en face.

    if (cote == 1 && j1->tab[c] == 1)
    {
        j1->score += j2->tab[7-c];
        j2->tab[7-c] = 0;
    }

    return cote;

}


int main()
{
    Joueur A, B;
    int tourDeQui=1, game=0, choice, dans_grenier;

    printf("\n");

    init(&A, 1);
    printf("Vous comptez de 1 à 6 de la gauche vers la droite.\n\n");

    init(&B, 2);
    printf("Vous comptez de 1 à 6 de la droite vers la gauche.\n\n");
    
    affiche(&A,&B);
    
    printf("\n");

    while (game==0)
    {
        if (tourDeQui == 1)
        {
            choice = choix(&A);
            dans_grenier = move(&A, &B, choice);
        }
        else
        {
            choice = choix(&B);
            dans_grenier = move(&B, &A, choice);
        }

        printf("\n");

        affiche(&A, &B);

        game = arret(&A, &B);

        if (dans_grenier != 0)
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
        
    }

    printf("\n\n**  Fin de la partie!  **\n\n");

    return 0;
}
