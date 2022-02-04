#include <stdio.h>
#include <stdlib.h>

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
    printf("%d", n);
    if (n == 6)
    {
        return 1; //True
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
        return 1; //au moins l'un des deux est en full zeros
    }
    else
    {
        return 0; //aucun des deux n'est en full zeros.
    }
}

/*void move(Joueur *A,Joueur *B,int c)
{
    int i;
    i=c;
    int Main =A->tab[i];
    int x=A->score;
    A->tab[i] = 0;
    while(i>1 && Main>0)
    {
        A->tab[i-1]++;
        Main--;
        i--;
    }
    if (Main != 0)
    {
        A->score++;
        Main--;
    }
     int j=6;
    while(j>0 && Main>0)
    {
       B->tab[j]++;
       Main--;
        j--;
    }
}*/

/* ----------------------------------------------------------*/

int move2(Joueur *j1, Joueur *j2, int tourDeQui)
{
    Joueur *A, *B;

    int idJoueurAdverse;

    if(tourDeQui==1)
    {
        A = j1;
        B = j2;
        idJoueurAdverse = 2;
    }
    else
    {
        A = j2;
        B = j1;
        idJoueurAdverse = 1;
    }

    int c = choix(A);

    int i;
    i=c;

    int Main = A->tab[i];

    A->tab[i] = 0;

    while(i>1 && Main>0)
    {
        A->tab[i-1]++;
        Main--;
        i--;
    }

    if(Main==0)
    {
        tourDeQui=idJoueurAdverse;
    }

    if(Main==1)
    {
        A->score++;
        Main--;
    }

    if(Main != 0 && Main != 1)
    {
        A->score++;
        Main--;

        int j=6;
        while(j>0 && Main>0)
        {
            B->tab[j]++;
            Main--;
            j--;
        }
        tourDeQui=idJoueurAdverse;
    }

    return tourDeQui;
}


int main()
{
    Joueur A, B;
    int tourDeQui=1, game=0;

    printf("\n");

    init(&A, 1);
    printf("Vous comptez de 1 à 6 de la gauche vers la droite.\n\n");

    init(&B, 2);
    printf("Vous comptez de 1 à 6 de la droite vers la gauche.\n\n");
    
    affiche(&A,&B);
    
    printf("\n");

    while (game==0)
    {
        tourDeQui = move2(&A,&B, tourDeQui);

        printf("\n");

        affiche(&A, &B);

        game = arret(&A, &B);
    }

    printf("\nFin de la partie!\n\n");

    return 0;
}
