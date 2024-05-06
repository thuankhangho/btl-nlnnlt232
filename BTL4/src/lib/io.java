import java.io.*;
import java.io.IOException;

public class io {
	public static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	public static Writer writer = new BufferedWriter(new OutputStreamWriter(System.out));

    public static float readNumber() {
        float tmp = 0;
		try {
			tmp = Float.parseFloat(input.readLine());
            return tmp;
		} catch (IOException e) {
			e.printStackTrace();
		}
		return tmp;
    }
    public static void writeNumber(float i) {
        System.out.print(i);	
    }
   
	public static boolean readBool() {
        boolean tmp = false;
		try {
            tmp = Boolean.parseBoolean(input.readLine());
            return tmp;
		} catch (IOException e) {
			e.printStackTrace();
		}
		return tmp;
	}
    public static void writeBool(boolean b)  {
    	System.out.print(b);
    }

    public static String readString() {
        String tmp = "";
        try {
            tmp = input.readLine();
            return tmp;
        } 
        catch (IOException e) {
            e.printStackTrace();
        }
        return tmp;
    }
    public static void writeString(String a)  {
    	System.out.print(a);
    }
    
    public static void close() {
    	try {
    		writer.close();
    	} catch (IOException e) {
			 e.printStackTrace();
		}
    }
}

