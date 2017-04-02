# PicoCTF_2017: Coffee

**Category:** Reverse Engineering
**Points:** 115
**Description:**

>You found a suspicious USB drive in a jar of pickles. It contains this file file.

**Hint:**

>Is there a way to get the source of the program?

## Write-up
Using something like JD-GUI, we get the source of the class file

    import java.io.PrintStream;
    import java.util.Arrays;
    import java.util.Base64;
    import java.util.Base64.Decoder;

    public class problem
    {
      public static String get_flag()
      {
        String str1 = "Hint: Don't worry about the schematics";
        String str2 = "eux_Z]\\ayiqlog`s^hvnmwr[cpftbkjd";
        String str3 = "Zf91XhR7fa=ZVH2H=QlbvdHJx5omN2xc";
        byte[] arrayOfByte1 = str2.getBytes();
        byte[] arrayOfByte2 = str3.getBytes();
        byte[] arrayOfByte3 = new byte[arrayOfByte2.length];
        for (int i = 0; i < arrayOfByte2.length; i++) {
          arrayOfByte3[i] = arrayOfByte2[(arrayOfByte1[i] - 90)];
        }
        System.out.println(Arrays.toString(Base64.getDecoder().decode(arrayOfByte3)));
        return new String(Base64.getDecoder().decode(arrayOfByte3));
      }
      
      public static void main(String[] paramArrayOfString)
      {
        System.out.println("Nothing to see here");
      }
    }

Like the source says, I'm way too lazy to work out the schematics, so lets try calling the `get_flag()` method from another file. This is where my [solver](solve.java) comes in! Just compile and run!

    $ javac solve.java 
    $ java solve
    [102, 108, 97, 103, 95, 123, 112, 114, 101, 116, 116, 121, 95, 99, 111, 111, 108, 95, 104, 117, 104, 125]
    flag_{pretty_cool_huh}

Therefore, the flag is `flag_{pretty_cool_huh}`.