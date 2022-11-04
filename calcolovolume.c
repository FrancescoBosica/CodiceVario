/*calcolare il peso volumetrico di un pacco di 12"*10"*8"*/
#include<stdio.h>
int main(void){
    int altezza=12, larghezza=10, spessore=8;
    int volume =0, peso = 0;
    volume = altezza * larghezza * spessore;
    peso = (volume + 165)/166;
    printf("il peso volumetrico è di: %d\n", peso);
    return 0;
}