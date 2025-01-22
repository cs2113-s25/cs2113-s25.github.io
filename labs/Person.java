import java.util.*;

public class Person{
	
	String firstname;
	String lastname;
	int age;
	Address address;
	public static int count;

	public Person(String first, String last, int age, Address address){
		this.firstname = first;
		this.lastname = last;
		this.age = age;
		this.address = address;

		count++;
	}

	public static int getCount(){
		return count;
	}

	public String toString(){
		return firstname + " " + lastname + "\n\t" + age + " years old";
	}

	public String getFirstName(){
		return firstname;
	}

	public String getLastName(){
		return lastname;
	}

	public static String sortPeople(ArrayList<Person> people){
        for (int i = 0; i < people.size() - 1; i++) {
            int minIndex = i;

            for (int j = i + 1; j < people.size(); j++) {
                Person current = people.get(j);
                Person minPerson = people.get(minIndex);

                if (current.getFirstName().compareTo(minPerson.getFirstName()) < 0 ||
                    (current.getFirstName().equals(minPerson.getFirstName()) && current.getLastName().compareTo(minPerson.getLastName()) < 0)) {
                    minIndex = j;
                }
            }

            if (minIndex != i) {
                Person temp = people.get(i);
                people.set(i, people.get(minIndex));
                people.set(minIndex, temp);
            }
        }

        String result = "";
        for (Person p : people){
        	result = result + p.getFirstName() + " " + p.getLastName() + "\n";
        }

        return result.substring(0, result.length());
    }		
}