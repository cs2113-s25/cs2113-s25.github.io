import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.*;

public class Lab4_Tester {

  @Test
  public void test1() {
    Address address = new Address("800", "22nd Street", "Washington", "DC", 20002);
    Person jane = new Person("Jane", "Doe", 23, address);
    assertEquals("Jane Doe\n\t23 years old\n\t800 22nd Street\n\tWashington, DC 20002", jane.toString());
    assertEquals(1, Person.getCount());
    Person.count = 0;
  }
  
  @Test
  public void test2() {
    Address address = new Address("800", "22nd Street", "Washington", "DC", 20002);
    Person jane = new Person("Jane", "Doe", 23, address);
    jane = new Person("Jane", "Doe", 23, address);
    assertEquals(2, Person.getCount());
    Person.count = 0;
  }

  @Test
  public void test3() {
    ArrayList<Person> people = new ArrayList<Person>();

    Person person = new Person("Jane", "Doe", 23, null);
    people.add(person);
    person = new Person("Yoon", "Kim", 23, null);
    people.add(person);
    person = new Person("Priya", "Patel", 23, null);
    people.add(person);
    person = new Person("Michael", "Abraham", 23, null);
    people.add(person);
    person = new Person("Zack", "Martinez", 23, null);
    people.add(person);
    person = new Person("John", "Doe", 23, null);
    people.add(person);
    Person.count = 0;

    String alphabetized_names = "Michael Abraham\nJane Doe\nJohn Doe\nYoon Kim\nZack Martinez\nPriya Patel";
    assertEquals(alphabetized_names, Person.sortPeople(people));
  }

}
