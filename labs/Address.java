public class Address{

	String number;
	String street;
	String city;
	String state;
	int zip;
	
	public Address(String numberIn, String street, String cityIn, String stateIn, int zipIn){
		number = numberIn;
		street = street;
		cityIn = city;
		state = stateIn;
		zip = zipIn;
	}

	public String toString(){
		return "\n\t" + number + " " + street + "\n\t" + this.city + ", " + " " + zip;
	}
}