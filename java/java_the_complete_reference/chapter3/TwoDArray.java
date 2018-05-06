class TwoDArray {
    public static void main(String args[]) {
        int row=4, col=5;
        int twoD[][] = new int[row][col];
        int i, j, k = 0;

        for (i=0; i<row; i++) {
            for (j=0; j<col; j++) {
                twoD[i][j] = k;
                k++;
            }
        }
        for (i=0; i<row; i++) {
            for (j=0; j<col; j++) {
                System.out.print(twoD[i][j] + " ");
            }
            System.out.println();
        }

        int x, y, z;
        x = y = z = 100;
        x++;
        y--;
        z++;
        z++;
        System.out.println(x);
        System.out.println(y);
        System.out.println(z);

    }
}