// Show all annotations for a class and a method.
import java.lang.annotation.*;
import java.lang.reflect.*;

@Retention(RetentionPolicy.RUNTIME)
@interface MyAnnotation {
    String str();
    int val();
}

@Retention(RetentionPolicy.RUNTIME)
@interface What {
    String description();
}

@What(description="An annotation test class")
@MyAnno(str = "Meta2", val=99)
class Meta2 {
    @What(description="An annotation test class")
    @MyAnno(str = "Meta2", val = 99)
    public static void myMeth() {
        Meta2 ob = new Meta2();

        try {
            Annotation annos[] = ob.getClass().getAnnotations();

            // Display all annotations for Meta2.
            System.out.println("All annotations for Meta2");
            for (Annotation a : annos) {
                System.out.println(a);
            }
            System.out.println();

            // display all annotations for myMeth
            Method m = ob.getClass().getMethod("myMeth");
            annos = m.getAnnotations();

            System.out.println("All annotations for myMeth");
            for (Annotation a : annos) {
                System.out.println(a);
            }
        } catch (NoSuchMethodException exc) {
            System.out.println("Method not Found.");
        }
    }

    public static void main(String args[]) {
        myMeth();
    }
}