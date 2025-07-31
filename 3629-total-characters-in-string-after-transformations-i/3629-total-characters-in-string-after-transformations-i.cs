public class Solution {
    const int fix = 26;
    const int mmd = 1_000_000_007;
    public int LengthAfterTransformations(string str, int t) {
        //attempt1
        // for(int i = 0; i<t; i++)
        // {
        //     for(int j = 0; j<str.Length; j++)
        //     {
        //         if(str[j]=='z')
        //         {
        //             str = str.Substring(0,j) + "ab" + str.Substring(j+1,str.Length-j-1);
        //             j = j+1;
        //             continue;
        //         }
        //         str = str.Substring(0,j) + (char) (str[j] + 1) + str.Substring(j+1,str.Length-j-1);
        //     }
        //     Console.WriteLine(str);//debugging
        // }
        // return str.Length;

        //attempt 2
        // for(int i =0; i<t; i++)
        // {
        //     var ss = new StringBuilder(str.Length + 10);
        //     foreach(char c in str)
        //     {
        //         if(c=='z')
        //             ss.Append("ab");
        //         else
        //             ss.Append((char)(c + 1));
        //     }
        //     str = ss.ToString();
        // }
        // return str.Length;

        long[] f = new long[fix];
        foreach(char c in str)
            f[c - 'a']++;

        for(int s = 0; s<t;++s)
        {
            long[] nf=new long[fix];

            for (int j = 0; j <fix-1;j++)
                nf[j+1]=(nf[j+1]+f[j])%mmd;

            nf[0]=(nf[0]+f[25])%mmd;
            nf[1]=(nf[1]+f[25])%mmd;
            f=nf;
        }
        long eq=0;
        foreach(long inc in f)
            eq = (eq+inc)%mmd;
        return (int)eq;
    }
}