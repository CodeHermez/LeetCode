public class Solution {
    public IList<int> MajorityElement(int[] nums) {
        int times = nums.Length/3;
        Dictionary<int,int> f = new Dictionary<int,int>();
        List<int> r =  new List<int>();

        foreach(int item in nums)
        {    if(!f.ContainsKey(item))
                f[item] =0;
            f[item]++;
        }

        foreach(var i in f)
            if(i.Value>times)
                r.Add(i.Key);
        
        return r;
    }
}