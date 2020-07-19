class Box2 {
    double width;
    double height;
    double depth;

    // pass object to constructor
    Box2(Box2 ob) {
        width = ob.width;
        height = ob.height;
        depth = ob.depth;
    }

    // constructor used when all dimensions are specified
    Box2(double w, double h, double d) {
        width = w;
        height = h;
        depth = d;
    }

    // constructor used when no dimensions specified
    Box2() {
        width = -1;
        height = -1;
        depth = -1;
    }

    // constructor used when cube is created
    Box2(double len) {
        width = depth = height = len;
    }

    // compute and return volume
    double volume() {
        return width * height * depth;
    }
}
public class OverloadCons2 {
    public static void main(String args[]) {
        // create boxes using the various constructors
        Box2 mybox1 = new Box2(10, 20, 15);
        Box2 mybox2 = new Box2();
        Box2 mybox3 = new Box2(7);

        Box2 myclone = new Box2(mybox1);// create copy of mybox1

        double vol;

        vol = mybox1.volume();
        System.out.println("Volume of mybox1 is " + vol);

        vol = mybox2.volume();
        System.out.println("Volume of mybox2 is " + vol);

        vol = mybox3.volume();
        System.out.println("Volume of mybox3 is " + vol);

        vol = myclone.volume();
        System.out.println("Volume of myclone is " + vol);
    }
}
