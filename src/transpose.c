#include  <stdio.h>
void transpose(const double  *input,double * output, int w, int l)
{
    for(int i = 0;i < w;i++){
        for(int j=0; j < l;j++) {
            output[j*w+i] = input[i*l+j];
        }
   }
}
void printArray(const double *a, int w,int l)
{
    for ( int i = 0;i < w; i++){
        for ( int j = 0;j < l;j++){
            printf("%f,",a[i*l+j]);
                    }
        printf("\n");
     }
 }

int main()
{
    printf("test");

}

