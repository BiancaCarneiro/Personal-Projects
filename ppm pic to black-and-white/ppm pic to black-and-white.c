#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#define N_THREADS 8

typedef struct {
    int red, green, blue;
} PPMPixel;

typedef struct {
    int linhas, colunas, max;
    int numPixels;
    PPMPixel *cores;
} PPMImage;

PPMImage *image;

//Lê o arquivo da imagem
PPMImage *readPPM(const char *filename){ 
    char buff[4];
    PPMImage *img;
    FILE *fp;
    int i;

    //Abre arquivo no modo leitura
    fp = fopen(filename, "rb");

    fscanf(fp, "%s\n", buff); //Le o tipo do arquivo

    //Aloca memória para img
    img = (PPMImage *)malloc(sizeof(PPMImage));

    //Lê as primeiras informações
    fscanf(fp, "%d %d", &img->colunas, &img->linhas);
    fscanf(fp, "%d", &img->max);
    img->numPixels = img->linhas * img->colunas;

    //printf("Linhas: %d\nColunas: %d\nRGB: %d\n", img->linhas, img->colunas, img->max);

    while (fgetc(fp) != '\n');//lê o \n para ir para as informações das cores


    //Lê as cores:
    img->cores = (PPMPixel*)malloc(img->numPixels * sizeof(PPMPixel));

    for(i = 0; i < img->numPixels; i++){   
        fscanf(fp, "%d %d %d ", &img->cores[i].red, &img->cores[i].green, &img->cores[i].blue);
    }

    fclose(fp);
    return img;
}

//Escreve a imagem nova
void writePPM(const char *filename, PPMImage *img){
    FILE *fp;
    int i;

    //Abre arquivo para modo escrita (se for a primeira vez executando o programa, ele vai criar cinza.ppm)
    fp = fopen(filename, "wb");
    
    //Escreve:
    fprintf(fp, "P3\n");
    fprintf(fp, "%d %d\n", img->colunas, img->linhas);
    fprintf(fp, "%d\n", img->max);

    for(i = 0; i < img->numPixels; i++){//i < número de cores   
        fprintf(fp, "%d %d %d\n", img->cores[i].red, img->cores[i].green, img->cores[i].blue);
    }
    fclose(fp);
}

//Converte os pixels para preto e branco
void *ConvertePixel(void *threadid){
    int i = *((int *)threadid);
    float red, green, blue; 
    int cinza;

    //printf("Sou eu a thread %d modificando o pixel %d\n", i, i);
    
    red =  0.3*image->cores[i].red;
    green = 0.59*image->cores[i].green;
    blue = 0.11*image->cores[i].blue;
    cinza = red + green + blue;

    image->cores[i].red = cinza;
    image->cores[i].green = cinza;
    image->cores[i].blue = cinza;
   
    pthread_exit(NULL);
}

int main(){
    int i, index, count = 0;
    int rc;

    //ESCREVA O NOME DO ARQUIVO AQUI:
    char NomeArquivo[] = "ex1.ppm";
    //
    
    image = readPPM(NomeArquivo);

    //printf("N threads: %d\n", image->numPixels);
    pthread_t thread[N_THREADS];
    int *id[image->numPixels];
    //Conversão de cores:
    for(i = 0; i < image->numPixels; i++){
        id[i] = (int *)malloc(sizeof(int));
        *id[i] = i;
        index = i%N_THREADS;
        //printf("id = %d\n", index);
        if(count >= N_THREADS) pthread_join(thread[index], NULL); //Verifica se já foram criadas o número de threads, se sim, espera a thread desejada acabar
        else count++;

        rc = pthread_create(&thread[index], NULL, ConvertePixel, (void *)id[i]);      
        if (rc){         
            printf("ERRO; código de retorno é %d\n", rc);         
            exit(-1);      
        }
    }

    char str[] = "Cinza_";
    strcat(str, NomeArquivo);

    writePPM(str,image);
    printf("Conversão de cores concluida com sucesso.\n");
    pthread_exit(NULL);
}