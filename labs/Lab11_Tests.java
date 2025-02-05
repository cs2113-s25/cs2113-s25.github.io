import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.*;
import java.io.*;
import java.net.*;
import java.time.*;

public class Lab11_Tests {
    /*
        Complete the test case below that checks to see that threads A and B have both contributed 1000 entries respectively
        to the shared ArrayList when they have both finished running.
    */
    @Test
    public void test1() {
        Lab11_Thread threadA = new Lab11_Thread("A", 1000);
        Lab11_Thread threadB = new Lab11_Thread("B", 1000);

        threadA.start();
        threadB.start();
    }

    /*
        Complete the test case below that checks to see if threads A and B have at least 1000 entries each after 50ms of system time
    */
    @Test
    public void test2() {
        Lab11_Thread threadA = new Lab11_Thread("A", 100000);
        Lab11_Thread threadB = new Lab11_Thread("B", 100000);

        threadA.start();
        threadB.start();
    }

    /*
        Complete the test case below that checks to see if thread A finishes adding its 1000 entries before thread B was allowed to 
        add anything to the shared ArrayList
    */
    @Test
    public void test3() {
        Lab11_Thread threadA = new Lab11_Thread("A", 1000);
        Lab11_Thread threadB = new Lab11_Thread("B", 1000);

        threadA.start();
        threadA.join();
        threadB.start();
    }
}
