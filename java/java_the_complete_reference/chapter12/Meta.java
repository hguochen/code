import java.lang.annotation.*;
import java.lang.reflect.*;

@Retention(RetentionPolicy.RUNTIME)
@interface MyAnno {
    String str();
    int val();
}

class Meta {
    // Annotate a method.
    @MyAnno(str = "Annotation Example", val = 100)
    public static void myMeth() {
        Meta ob = new Meta();

        // Obtain the annotation for this method
        // and display the values of the members.
        try {
            // First, get a Class obbject that represents this class.
            Class<?> c = ob.getClass();

            // Now, get a method object that represents this method.
            Method m = c.getMethod("myMeth");

            // Next, get the annotation for this class.
            MyAnno anno = m.getAnnotation(MyAnno.class);

            // Finally, display the values 
            System.out.println(anno.str() + " " + anno.val());
        } catch ( NoSuchMethodException exc) {
            System.out.println("Method Not Found.");
        }
    }

    public static void main(String args[]) {
        myMeth();
    }
}