public class Lab11_Thread extends Thread {
    private static ArrayList<String> data = new ArrayList<String>();
    private String name;
    private int runs; 

    public Lab11_Thread(String name, int runs) {
      this.name = name;
      this.runs = runs;
    }

    public void run() {
      for(int i = 0; i < runs; i++){
        this.sleep(10);
        data.add( name + " " + i);
      }
    }

    public ArrayList getData(){
      return data;
    }
}