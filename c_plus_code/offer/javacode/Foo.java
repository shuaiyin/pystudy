public class Foo {
    int i = 5;
    static double k = 0;
    
    public static void main(String[] args){
        Foo f = new Foo();
        f.setK(2.0);
        System.out.println("k = " + k);
    }
    void setI(int i){
        this.i = i;
    }
    
    public static void setK(double k){
        Foo.k = k;
    }
}