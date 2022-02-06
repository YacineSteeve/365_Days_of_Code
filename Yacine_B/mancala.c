#include <stdio.h>
#include <stdlib.h>
#include <time.h>


typedef struct Joueur Joueur;
struct Joueur
{
    char nom[60];
    int score;
    int tab[6];
};


void init(Joueur *A, int n, int x)
{
    printf("Nom du joueur %d : ", n);
    scanf("%60s", A->nom);
    A->score = 0;
    int i=0;
    while(i<7)
    {
        A->tab[i]=x;
        i++;
    }
}

void init_IA(Joueur *A, Joueur *B, int x)
{
    B->nom[0] = 'I';
    B->nom[1] = 'A';
    B->score = 0;
    int j=0;
    while(j<7)
    {
        B->tab[j]=x;
        j++;
    }
    printf("IA prête!\n\n");

    printf("Nom du joueur : ");
    scanf("%60s", A->nom);
    A->score = 0;
    int i=0;
    while(i<7)
    {
        A->tab[i]=x;
        i++;
    }
}


void affiche(Joueur *A, Joueur *B)
{
    printf("|%3d",A->score);

    int i=1;
    while(i<=6)
    {
        printf("| %2d", A->tab[i]);
        i++;
    }

    printf("|   |  %s\n|   ", A->nom);

    int j=6;
    while(j>=1)
    {
        printf("| %2d", B->tab[j]);
        j--;
    }
    printf ("|%3d|  %s", B->score, B->nom);
}


int choix(Joueur *A)
{
    int c;

    printf("\n\n--- Tour de %s ---\n", A->nom);

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


int nombre_de_grains()
{
    int x;
    printf("Avec combien de grains par case voulez-vous jouer? : ");
    scanf("%d", &x);
    return x;
}


int game_mode()
{
    int n;

    printf("\n--------  Mode de jeu  --------\n");
    printf("\n   1. J vs J");
    printf("\n   2. J vs IA");
    
    do
    {
        printf("\n\nChoisissez un mode (entre 1 et 2) : ");
        scanf("%d", &n);

        if (n<1 || n>2)
        {
            printf("Non défini!");
        }
    } while (n<1 || n>2);

    return n;
}


int partie()
{
    int n;

    printf("\n--------  Type de Partie  --------\n");
    printf("\n   1. Normal");
    printf("\n   2. Jeu en N coups");
    printf("\n   3. Contre-la-montre");
    
    do
    {
        printf("\n\nChoisissez une partie (entre 1 et 3) : ");
        scanf("%d", &n);

        if (n<1 || n>3)
        {
            printf("Non définie!");
        }
    } while (n<1 || n>3);

    return n;
}


int nb_aleatoire(Joueur *B)
{
    int n;
    srandom(time(NULL));
    do
    {    
        n = random()%6 + 1;
    } while (B->tab[n] == 0);

    return n;
}


void attendre(int temps)
{
    clock_t arrivee = clock() + (temps*CLOCKS_PER_SEC);

    while(clock() < arrivee);
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
        return 1;
    }
    else
    {
        return 0;
    }
}


int arret(Joueur *A, Joueur *B)
{
    if ((full_zero(A)==1) || (full_zero(B)==1))
    {
        return 1;
    }
    else
    {
        return 0;
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

        c = 7;

    }

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
    int tourDeQui=1, nb, mode, party, game=0, coups=1, coups_max=1000, choice, dans_grenier;

    printf("\n*******************************************");
    printf("\n*************** MANCALA 2.0 ***************");
    printf("\n*******************************************");
    printf("\n\n");

    mode = game_mode();
    printf("\n");
    nb = nombre_de_grains();
    party = partie();

    if (party == 2)
    {
        printf("\nEn combien de coups (par joueur) voulez-vous jouer? : ");
        scanf("%d", &coups_max);
    }

    printf("\n");

    if (mode == 1)
    {
        init(&A, 1, nb);
        printf("Vous comptez de 1 à 6 de la gauche vers la droite.\n\n");

        init(&B, 2, nb);
        printf("Vous comptez de 1 à 6 de la droite vers la gauche.\n\n\n");
    }
    else if (mode == 2)
    {
        init_IA(&A, &B, nb);
        printf("Vous comptez de 1 à 6 de la droite vers la gauche.\n\n\n");
    }
    
    printf("       ********************       ");
    printf("\n*******    C'est parti!    *******\n");
    printf("       ********************       \n\n\n");

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
                choice = nb_aleatoire(&B);
                printf("Je choisis la case %d\n", choice);
            }
            dans_grenier = move(&B, &A, choice);
        }

        printf("\n");

        attendre(1);
        affiche(&A, &B);

        game = arret(&A, &B);

        if (dans_grenier != 0 || party==2)
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

    printf("\n\n\n       *********************       ");
    printf("\n*******  Fin de la partie!  *******\n");
    printf("       *********************       \n\n\n");

    int i=1;
    while(i<7)
    {
        A.score += B.tab[i];
        B.score += A.tab[i];
        A.tab[i] = 0;
        B.tab[i] = 0;
        i++;
    }

    affiche(&A, &B);

    return EXIT_SUCCESS;
}
