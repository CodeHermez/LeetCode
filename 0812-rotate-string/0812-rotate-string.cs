public class Solution {
    public bool RotateString(string s, string goal) {
        bool test = false;
        int i=0;
        
        if(s.Equals(goal))
            return true;

        while (!s.Equals(goal) && i!=goal.Length)
        {
            s = s.Substring(1) + s[0];
            // Console.WriteLine(s);
            if(s.Equals(goal))
                test=true;
            i+=1;
        }
        return test;
    }
}