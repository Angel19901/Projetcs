#include <bits/stdc++.h>

using namespace std;

int MatrizCifrado[3][3] ={{1,2,3},{0,1,4},{5,6,0}};
int MatrizAdjuntaTranspuesta[3][3];
int MatrizInversa[3][3];

vector<int> VectorCifrada;
vector<int> VectorString;
vector<int> VectorDecifrada;

void Transpuesta()
{
    for(int i = 0; i < 3; i++)
    {
        for(int j = 0; j < 3; j++)
        {
            MatrizInversa[i][j] = MatrizAdjuntaTranspuesta[j][i];
        }
    }
}


void Adjunta()
{
    MatrizAdjuntaTranspuesta[0][0] = MatrizCifrado[1][1] * MatrizCifrado[2][2] - MatrizCifrado[1][2] * MatrizCifrado[2][1];
    MatrizAdjuntaTranspuesta[0][1] = -1 * (MatrizCifrado[1][0] * MatrizCifrado[2][2] - MatrizCifrado[1][2] * MatrizCifrado[2][0]);
    MatrizAdjuntaTranspuesta[0][2] = MatrizCifrado[1][0] * MatrizCifrado[2][1] - MatrizCifrado[1][1] * MatrizCifrado[2][0];
    MatrizAdjuntaTranspuesta[1][0] = -1 * (MatrizCifrado[0][1] * MatrizCifrado[2][2] - MatrizCifrado[0][2] * MatrizCifrado[2][1]);
    MatrizAdjuntaTranspuesta[1][1] = MatrizCifrado[0][0] * MatrizCifrado[2][2] - MatrizCifrado[0][2] * MatrizCifrado[2][0];
    MatrizAdjuntaTranspuesta[1][2] = -1 * (MatrizCifrado[0][0] * MatrizCifrado[2][1] - MatrizCifrado[0][1] * MatrizCifrado[2][0]);
    MatrizAdjuntaTranspuesta[2][0] = MatrizCifrado[0][1] * MatrizCifrado[1][2] - MatrizCifrado[0][2] * MatrizCifrado[1][1];
    MatrizAdjuntaTranspuesta[2][1] = -1 * (MatrizCifrado[0][0] * MatrizCifrado[1][2] - MatrizCifrado[0][2] * MatrizCifrado[1][0]);
    MatrizAdjuntaTranspuesta[2][2] = MatrizCifrado[0][0] * MatrizCifrado[1][1] - MatrizCifrado[0][1] * MatrizCifrado[1][0];

}

int Determinante()
{
    int n;
    
    n = MatrizCifrado[0][0] * (MatrizCifrado[1][1] * MatrizCifrado[2][2] - MatrizCifrado[1][2] * MatrizCifrado[2][1]) - MatrizCifrado[0][1] * (MatrizCifrado[1][0] * MatrizCifrado[2][2] - MatrizCifrado[1][2] * MatrizCifrado[2][0]) + MatrizCifrado[0][2] * (MatrizCifrado[1][0] * MatrizCifrado[2][1] - MatrizCifrado[1][1] * MatrizCifrado[2][0]); 

    return n;
    
}

int *euclidesExtendidoMCD(int a, int b)
{
    int d,x,y;

    int x1,x2,y1,y2;

    int q,r;
    int *rpts=new int[3];

  

    if(b==0)
    {
        d=a;
        x=1;
        y=0;   
        rpts[0]=d; rpts[1]=x; rpts[2]=y;
        
        return rpts;
    }
    
    x1=0; x2=1;

    y1=1; y2=0;
    while(b >0)
    {

        q=(a/b); r=a-q*b;
    
        x=x2-q*x1; y=y2-q*y1;
        
        a=b; b=r;
        
        x2=x1; x1=x;
        
        y2=y1; y1=y;   
    }
    rpts[0]=a; rpts[1]=x2; rpts[2]=y2;
    
    return rpts;
 
}

void AplicacionModulo(char n)
{
    switch(n - '0')
    {
        case 1:
            for(int i = 0; i < VectorCifrada.size(); i++)
            {
                VectorCifrada[i] = ((VectorCifrada[i] % 255) + 255) % 255;
            }
           break;
        case 2:
            for(int i = 0; i < 3; i++)
            {
                for(int j = 0; j < 3; j++)
                {

                    if(MatrizInversa[i][j] < 0)
                        MatrizInversa[i][j] = ((MatrizInversa[i][j] % 255) + 255) % 255;
                    else
                        MatrizInversa[i][j] = MatrizInversa[i][j] % 255;

                }
            }
           break;
        case 3:
            for(int  i = 0; i < VectorDecifrada.size(); i++)
            {
                VectorDecifrada[i] = ((VectorDecifrada[i] % 255) + 255 ) % 255;
            }
    }    
    
}


void InvertirMatriz()
{
    int D;
    int *r;
    int inverso;
    
    D = Determinante();
    if(D < 0)
    {
        D = ((D % 255) + 255) % 255;
    }
    
    r = euclidesExtendidoMCD(D,255);
    if(r[0]==1)
    {
        if(r[1]< 0)
        inverso = 255 + r[1];
        else
        if(r[1] >0)
        {
            inverso = r[1];    
        }
    }
    else
        D = 0;
    
    if((D != 0) && (r[0] == 1) && (r[0] != 3) && (r[0] != 5) && (r[0] != 17))
    {    
        delete r;
    }
    else
    {
        system("cls");
        cout<<"\tEsta matriz tiene determinate igual a cero.\n\n";
        system("PAUSE");
        delete r;
        exit(1);
    }
    
    Adjunta();
    Transpuesta();
    AplicacionModulo('2');
    
    for(int i = 0; i < 3; i++)
    {
        for(int j = 0; j < 3; j++)
        {
            MatrizInversa[i][j] = inverso * MatrizInversa[i][j];
        }
    }
    
}

void MultilicacionMatrices(char n)
{
    int k = 0;
    int i = 0;
    int j = 0;
    
    int suma = 0;
    switch(n-'0')
    {
        case 1:
            for(k = 0; k < VectorString.size(); k +=3 )
            {
                for(i = 0; i < 3; i++)
                {
                    for(j = 0; j < 3; j++)
                    {
                        suma = suma + (MatrizCifrado[i][j] * VectorString[k + j]);
                        
                    }
                    VectorCifrada.push_back(suma);
                    suma = 0;

                }
                
            }
           break;
        case 2:
            for(k = 0; k < VectorCifrada.size(); k +=3 )
            {
                for(i = 0; i < 3; i++)
                {
                    for(j = 0; j < 3; j++)
                    {
                        suma = suma + (MatrizInversa[i][j] * VectorCifrada[k + j]);
                        
                    }
                    
                    VectorDecifrada.push_back(suma);
                    suma = 0;

                }
                
            }
           break;
    }

}

void MostrarMensajeEncriptadoDesencriptado(char n)
{
    switch(n -'0')
    {

        case 1:
            for(int i = 0; i < VectorCifrada.size(); i++)
            {
                printf("%d ",VectorCifrada[i]);
            }
    
            printf("\n");
           break;
        case 2:
            for(int i = 0; i < VectorDecifrada.size(); i++)
            {
                printf("%c",char(VectorDecifrada[i]));
            }
           break;

    }
    
}

void LLenadoASCII()
{

    int Dato;

    string Frase;
    stringstream ss;

    while(getline(cin, Frase))
    {

	    ss << Frase;
		
	    while(ss >> Dato)
		VectorCifrada.push_back(Dato);

	    ss.clear();

    }
 
}

void ObtencionCadenaCaracteres()
{

	string Frase;

	getline(cin, Frase);

	int Faltante = 3 - int(Frase.size()) % 3;

	for(int i = 0; i < int(Frase.size()); ++i)
		VectorString.push_back(int(Frase[i]));

	for(int i = 0; i < Faltante; ++i)
	{

		if(i == Faltante - 1)
			VectorString.push_back(10);
		else
			VectorString.push_back(32);

	}
   
}

int main()
{
	int n;

	scanf("%d",&n);
	getchar();

	fflush(stdin);

        switch(n)
        {
            case 1:

                ObtencionCadenaCaracteres();
                
                InvertirMatriz();
                
                MultilicacionMatrices('1');
                
                AplicacionModulo('1');

                MostrarMensajeEncriptadoDesencriptado('1');
                
                VectorCifrada.clear();
                VectorString.clear();
                VectorDecifrada.clear();

               break;
            case 2:

                LLenadoASCII();
                
                InvertirMatriz();
                
                MultilicacionMatrices('2');

                AplicacionModulo('3');

                MostrarMensajeEncriptadoDesencriptado('2');
                
                VectorCifrada.clear();
                VectorString.clear();
                VectorDecifrada.clear();

               break;
            default :
               break;
        }
    
    
    return 0;

}
    
