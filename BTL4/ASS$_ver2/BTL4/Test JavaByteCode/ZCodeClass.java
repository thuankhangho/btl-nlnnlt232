//! lệnh dịch sang .class -> javac ZCodeClass.class
//! lệnh dịch .class sang .j -> java -jar classfileanalyzer.jar -file ZCodeClass.class
//! lệnh dịch print kết quả -> java ZCodeClass
//! lệnh dịch từ .j sang .class -> java  -jar ./external/jasmin.jar ZCodeClass.j

public class ZCodeClass {
    
    public static void main(String[] args) {
        String a[] = {"1"};
        String b[][] = {{"1"}};
    }
    
}