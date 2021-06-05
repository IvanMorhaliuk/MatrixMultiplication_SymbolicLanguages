__declspec(dllexport) float float_summa(float** matrix1,float** matrix2, int row,int col,int n){
    float s = 0;
    for(int i = 0;i<n;++i){
        s+=matrix1[row][i]*matrix2[i][col];
    }
    return s;
}

__declspec(dllexport) void float_mnoz(float** matrix1,float** matrix2,float** matrix3, int m3rows,int m3cols,int m1cols) {
    for(int i = 0;i<m3rows;++i){
        for(int j=0;j<m3cols;++j){
            matrix3[i][j] = float_summa(matrix1,matrix2,i,j,m1cols);
        }
    }
}

__declspec(dllexport) int int_summa(int** matrix1,int** matrix2, int row,int col,int n){
    int s = 0;
    for(int i = 0;i<n;++i){
        s+=matrix1[row][i]*matrix2[i][col];
    }
    return s;
}

__declspec(dllexport) void int_mnoz(int** matrix1,int** matrix2,int** matrix3, int m3rows,int m3cols,int m1cols) {
    for(int i = 0;i<m3rows;++i){
        for(int j=0;j<m3cols;++j){
            matrix3[i][j] = int_summa(matrix1,matrix2,i,j,m1cols);
        }
    }
}
