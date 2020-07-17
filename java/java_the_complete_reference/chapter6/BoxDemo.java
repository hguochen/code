class Box {
    double width;
    double height;
    double depth;
}

class BoxDemo {
    public static void main(String args[]) {
        Box myBox = new Box();
        Box myBox2 = new Box();
        double vol;
        double vol2;

        myBox.width = 10;
        myBox.height = 20;
        myBox.depth = 15;

        myBox2.width = 5;
        myBox2.height = 30;
        myBox2.depth = 20;

        vol = myBox.width * myBox.height * myBox.depth;
        System.out.println("Volume is " + vol);

        vol2 = myBox2.width * myBox2.height * myBox2.depth;
        System.out.println("Volume is " + vol2);
    }
}