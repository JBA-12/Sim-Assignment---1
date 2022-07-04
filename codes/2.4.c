#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) 
{
 

//Gaussian random numbers
gaussian("gau.dat", 1000000);
Mean of Gaussian random numbers
printf("Mean is %lf\n",mean("uni.dat"));
Variance of Gaussian random numbers
printf("Variance is %lf",variance("uni.dat"));

return 0;
 
}
