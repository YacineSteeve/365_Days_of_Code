#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//#include <windows.h>


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
    B->nom[2] ='\0';
    B->score = 0;
    int j=0;
    while(j<7)
    {
        B->tab[j]=x;
        j++;
    }
    printf("\nIA prête!\n\n");

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
    //Color(2,0);
    printf("\n               ****** %s ******",A->nom);

    printf("\n\n\t (%3d) ",A->score);

    int i=1;
    while(i<=6)
    {
        printf("| %2d", A->tab[i]);
        i++;
    }
    printf("|");

    printf("\n \n");

    //Color(8,0);
    printf("\t       ");
    int j=6;
    while(j>=1)
    {
        printf("| %2d", B->tab[j]);
        j--;
    }
    printf ("| (%3d)  ", B->score);
    printf("\n\n\n               ******  %s  ******",B->nom);
    //Color(15,0);
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

int choixMenu()
{
     int m;

    printf("\n--------  Menu  --------\n");
    printf("\n   1. Nombre de graines par défaut.");
    printf("\n   2. Choisir un nombre de graines.");

    do
    {
        printf("\n\n Choisissez un menu (entre 1 et 2) : ");
        scanf("%d", &m);

        if (m<1 || m>2)
        {
            printf("Non défini!");
        }
    } while (m<1 || m>2);

    return m;
}


int choixNiveau()
{
    int m;

    printf("\n--------  Niveau d'IA  --------\n");
    printf("\n   1. Facile.");
    printf("\n   2. Difficile.");

    do
    {
        printf("\n\n Choisissez un niveau (entre 1 et 2) : ");
        scanf("%d", &m);

        if (m<1 || m>2)
        {
            printf("Non défini!");
        }
    } while (m<1 || m>2);

    return m;
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
        printf("\n\n Choisissez un mode (entre 1 et 2) : ");
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

    do
    {
        printf("\n\n Choisissez une partie (entre 1 et 2) : ");
        scanf("%d", &n);

        if (n<1 || n>2)
        {
            printf("Non définie!");
        }
    } while (n<1 || n>2);

    return n;
}


int nb_aleatoire_facile(Joueur *B)
{
    int n;
    srand(time(NULL));
    do
    {
        n = rand()%6 + 1;
    } while (B->tab[n] == 0);

    return n;
}


int nb_aleatoire_difficile(Joueur *B)
{
    int n=6;
    while (n>=1 && (B->tab[n]==0 || B->tab[n]>=n))
    {
        n--;
    }

    if (n==0)
    {
        int k=6;
        while (k>=1 && B->tab[k]==0)
        {
            k--;
        }
        return k;
    }
    else
    {
        return n;
    }
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
             c = 7;
        }

    }

    if (cote == 1 && j1->tab[c+1] == 1)
    {
        j1->score += j2->tab[6-c];
        j2->tab[6-c] = 0;
    }

    return cote;

}


void enregistrement(Joueur A, Joueur B)
{
    FILE * fichier = NULL;
    fichier=fopen("sauvegarde.txt","a+");
    if(fichier != NULL)
    {   
        int h, min, s, jour, mois, an;

        time_t now; //Variable de type temps.

        time(&now); // Renvoie l'heure actuelle

        struct tm *local = localtime(&now);

        h = local->tm_hour;        
        min = local->tm_min;       
        s = local->tm_sec;       
        jour = local->tm_mday;          
        mois = local->tm_mon + 1;     
        an = local->tm_year + 1900;
    
        fprintf(fichier,"**  %02d:%02d:%02d  %02d/%02d/%d\n", h, min, s, jour, mois, an);
        fprintf(fichier,"Joueur 1 : %s , Score = %d ;\n", A.nom, A.score);
        fprintf(fichier,"Joueur 2 : %s , Score = %d ;\n", B.nom, B.score);
        fprintf(fichier,"--------------------------------------------------\n");

        fclose(fichier);
    }
    else
    {
        printf("Échec d'enregistrement!");
    }
}

/*
void Color(int t , int f)
{
    HANDLE H = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(H,f*16+t);
}
*/


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
