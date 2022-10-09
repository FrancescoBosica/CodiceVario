//lettura da un file copiare il contenuto e scriverlo all'interno di un nuovo file
#include<stdio.h>
#include<stdlib.h>
int main(void){
    FILE * fp, * fp2;
    char * line = NULL;
    size_t len = 0;//grandezza blocco di memoria allocata 
    ssize_t read;//grandezza blocco di memoria allocata con segno permette di rappresentare il numero -1
    //apertura in memoria dei due file
    fp = fopen("./prova.txt", "r");//modalità lettura
    fp2 = fopen("./prova1.txt", "w");//modalità scrittuta
    //controllo dell'esistenza dei file
    if (fp == NULL && fp2 == NULL)
        exit(EXIT_FAILURE);//invio dell'errore
    //lettura all'interno del primo file
    while ((read = getline(&line, &len, fp)) != -1) {
        fprintf(fp2,"%s",line);//scrittura all'interno del secondo file
    }
}